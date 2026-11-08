#!/usr/bin/env python3
"""Türkçe kalıp tarama ve koruma kontrolü. Stdlib only."""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

GENRES = frozenset({"chat", "explanation", "email", "technical", "formal"})
NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
FENCE_RE = re.compile(r"```[^\n]*\n.*?```", re.DOTALL)
INLINE_RE = re.compile(r"`[^`\n]+`")
PLACEHOLDER_RE = re.compile(r"\[[^\]\n]{1,60}\]")
ELLIPSIS_RE = re.compile(r"…+")
FENCED_STRIP = r"```[^\n]*\n.*?```"
INLINE_STRIP = r"`[^`\n]+`"
URL_STRIP = r"https?://\S+"


def tr_lower(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


def _mask(pattern, text, flags=0):
    out = []
    last = 0
    for m in re.finditer(pattern, text, flags):
        out.append(text[last : m.start()])
        out.append(" " * (m.end() - m.start()))
        last = m.end()
    out.append(text[last:])
    return "".join(out)


def strip_code(text):
    text = _mask(FENCED_STRIP, text, re.DOTALL)
    text = _mask(INLINE_STRIP, text)
    text = _mask(URL_STRIP, text)
    return text


def load_patterns(path=None):
    if path is None:
        path = Path(__file__).resolve().parent.parent / "references" / "kaliplar.json"
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    weights = data.get("agirlik_puani") or {}
    if not weights:
        raise ValueError("agirlik_puani missing")
    raw = data.get("kaliplar") or []
    seen = set()
    patterns = []
    for item in raw:
        pid = item.get("id")
        if not pid or pid in seen:
            raise ValueError(f"duplicate or bad id {pid!r}")
        seen.add(pid)
        agirlik = item.get("agirlik")
        if agirlik not in weights:
            raise ValueError(f"bad agirlik on {pid}")
        tur = item.get("tur") or {}
        for key, val in tur.items():
            if key not in GENRES:
                raise ValueError(f"bad tur key on {pid}")
            if val != "muaf" and val not in weights:
                raise ValueError(f"bad tur value on {pid}")
        compiled = [re.compile(d, re.MULTILINE) for d in item.get("desenler") or []]
        patterns.append({
            "id": pid,
            "ad": item.get("ad", ""),
            "agirlik": agirlik,
            "tur": tur,
            "desenler": compiled,
        })
    return patterns, weights


def effective_weight(pattern, genre):
    if genre is None:
        return pattern["agirlik"]
    return pattern["tur"].get(genre, pattern["agirlik"])


def scan(text, genre=None, patterns=None, weights=None):
    if patterns is None or weights is None:
        patterns, weights = load_patterns()
    hay = tr_lower(strip_code(text))
    hits = []
    seen = set()
    for pat in patterns:
        wt = effective_weight(pat, genre)
        if wt == "muaf":
            continue
        for cre in pat["desenler"]:
            for m in cre.finditer(hay):
                key = (pat["id"], m.start())
                if key in seen:
                    continue
                seen.add(key)
                hits.append({
                    "id": pat["id"],
                    "ad": pat["ad"],
                    "agirlik": wt,
                    "start": m.start(),
                    "end": m.end(),
                    "match": text[m.start() : m.end()],
                })
    hits.sort(key=lambda h: (h["start"], h["end"]))
    accepted = []
    for h in hits:
        if any(
            a["id"] == h["id"] and h["start"] < a["end"] and h["end"] > a["start"]
            for a in accepted
        ):
            continue
        accepted.append(h)
    return accepted


def density(text, genre=None, patterns=None, weights=None):
    if patterns is None or weights is None:
        patterns, weights = load_patterns()
    words = re.findall(r"\w+", strip_code(text))
    if not words:
        return 0.0
    total = 0
    for h in scan(text, genre, patterns, weights):
        total += weights.get(h["agirlik"], 0)
    return round(100.0 * total / len(words), 2)


def _trim_url(u):
    return u.rstrip(".,;:!?")


def _packs(text):
    fences = FENCE_RE.findall(text)
    rest = FENCE_RE.sub(" ", text)
    urls = [_trim_url(u) for u in URL_RE.findall(text)]
    return {
        "number": NUM_RE.findall(text),
        "url": urls,
        "fence": fences,
        "inline": INLINE_RE.findall(rest),
        "placeholder": PLACEHOLDER_RE.findall(text) + ELLIPSIS_RE.findall(text),
    }


def protected_diff(source, output, spans=()):
    src, out = _packs(source), _packs(output)
    flags = []
    for name in ("number", "url", "fence", "inline", "placeholder"):
        if Counter(src[name]) != Counter(out[name]):
            flags.append(name)
    for span in spans or []:
        if span and source.count(span) != output.count(span):
            flags.append("span")
            break
    return flags


def _line_col(text, pos):
    line = text.count("\n", 0, pos) + 1
    last = text.rfind("\n", 0, pos)
    col = pos - last
    return line, col


def _read_file(path):
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def _cmd_tara(args):
    text = _read_file(args.file)
    patterns, weights = load_patterns()
    hits = scan(text, args.tur, patterns, weights)
    dens = density(text, args.tur, patterns, weights)
    if args.json:
        print(json.dumps({"hits": hits, "density": dens}, ensure_ascii=False))
        return 0
    for h in hits:
        line, col = _line_col(text, h["start"])
        print(f"{line}:{col}  {h['id']}  {h['ad']}  ({h['agirlik']})  «{h['match']}»")
    print(f"yoğunluk: {dens} / 100 sözcük")
    return 0


def _cmd_karsilastir(args):
    src = _read_file(args.kaynak)
    out = _read_file(args.cikti)
    patterns, weights = load_patterns()
    diff = protected_diff(src, out)
    d_before = density(src, args.tur, patterns, weights)
    d_after = density(out, args.tur, patterns, weights)
    strong = [h for h in scan(out, args.tur, patterns, weights) if h["agirlik"] == "guclu"]
    if args.json:
        print(json.dumps({
            "protected_diff": diff,
            "density_before": d_before,
            "density_after": d_after,
            "strong_hits": strong,
        }, ensure_ascii=False))
        return 1 if diff else 0
    if diff:
        print(f"koruma: KAYMA -> {', '.join(diff)}")
    else:
        print("koruma: temiz")
    print(f"yoğunluk: önce {d_before} -> sonra {d_after}")
    for h in strong:
        line, col = _line_col(out, h["start"])
        print(f"{line}:{col}  {h['id']}  {h['ad']}  ({h['agirlik']})  «{h['match']}»")
    return 1 if diff else 0


def main(argv=None):
    parser = argparse.ArgumentParser(prog="kontrol")
    sub = parser.add_subparsers(dest="cmd", required=True)

    tara = sub.add_parser("tara")
    tara.add_argument("file")
    tara.add_argument("--tur", default=None)
    tara.add_argument("--json", action="store_true")

    kars = sub.add_parser("karsilastir")
    kars.add_argument("kaynak")
    kars.add_argument("cikti")
    kars.add_argument("--tur", default=None)
    kars.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    if args.cmd == "tara":
        raise SystemExit(_cmd_tara(args))
    if args.cmd == "karsilastir":
        raise SystemExit(_cmd_karsilastir(args))


if __name__ == "__main__":
    main()
