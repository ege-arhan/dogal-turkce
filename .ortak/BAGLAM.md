# Bağlam

Yazar: `SKILL.md`, `references/*.md`, `README.md`, bu dosya. Kod: `evaluate.py`, `tests/`. `evaluator/` yok.

Beceri, Türkçe yapay anlatım için. Düzenlemeden önce `references/examples.md`. Son metin; sıkışan yer. Okur ve tür durur. Son metin kaynakla kıyaslanır. Koru: olgu, kapsam, olumsuz, kip, nezaket, yükümlülük, terim, kod, URL, sayı. `-miş` yalnız aktarım değildir. Kesinliği düşürme, yargıyı tersine çevirme, iletme ricâsını silme.

Pilot: `data/pilot.json`, 8 sentetik, Grok, insan değil. Kollar `simple`, `humanizer`, `turkce`, `ours`. Kör A–D.

Hedef final 40 ayrıdır. Eşik finalden önce donar. Aynı kaynak ailesi geliştirme ve finalde birden durmaz. Pilot 24/40 tutmaz. `score` başarı yazmaz. Kartlar JSON.

```text
python3 -m unittest tests.test_evaluate
python3 evaluate.py run --cases data/pilot.json --out .local/pilot --arms ours,simple,humanizer,turkce --model grok-4.7-medium --workers 2
python3 evaluate.py cards --run .local/pilot --out .local/cards.json --limit 5
python3 evaluate.py vote --run .local/pilot --case p01 --choice A
python3 evaluate.py score --run .local/pilot
```

Planlanan modeller yok. Pilot Grok. Kişisel profil repoda yok; yaklaşık 10 özel ileti temsilî değil, ayrıntı yalnız `.local`. Üst istem, eşleme, oy, insan derlemi `.local`. Lisans özgün MIT, 2026 Ege Arhan. Dış metin kopyalanmaz. TDK üslup ölçütü değildir.
