# Değerlendirme protokolü

Amaç, becerinin gerçek model çıktılarını anlamı bozmadan daha doğal hâle getirip getirmediğini, bilinen rakiplere karşı ölçmek. Dedektör atlatmak hedef değil. Başarıyı insan oyu belirler; otomatik ölçümler ve yargıç model yardımcı sinyaldir.

## Veri

Üç ayrı küme var. Bir konu ailesi yalnız birinde bulunur.

| Küme | Dosya | İçerik | Kullanım |
|---|---|---|---|
| Koruma | `data/koruma.json` | 8 sentetik metin (eski pilot) | Sayı, kod, yer tutucu koruma regresyonu |
| Geliştirme | `data/gelistirme.json` | 10 gerçek model çıktısı, her türden 2 | Pilot, beceri ayarı, rakip seçimi |
| Final | `.local/final/final.json` | 30 model çıktısı + 10 insan metni | Tek seferlik A/B testi |

Geliştirme ve final kaynakları 8 Kasım 2026'da aynı yöntemle toplandı: 60 soru (her türden 12) yazıldı, Cursor ask modunda ek yönerge olmadan üç modele dağıtıldı (`cursor-grok-4.5-medium`, `cursor-grok-4.6-medium`, `composer-2.5`) ve varsayılan yanıtlar kaydedildi. İlk 30'u (d01-d30) geliştirme derlemine, son 30'u (h01-h30) finale ayrıldı. Final metinleri beceri yazılırken ve pilot boyunca okunmadı.

Finaldeki 10 insan metni 2019 ve öncesinden, yani yaygın sohbet modellerinden önceden: Debian Türkçe e-posta listeleri (sohbet, e-posta, teknik), 2018 Vikipedi sürümleri (açıklama), 2019 Resmî Gazete ilanları (resmî). Kaynak adresleri, tarih ve lisans her kayıtta durur. Bu metinler iki şeyi ölçer: beceri insan metnini bozmadan bırakabiliyor mu ve yargıç ile insan oyu insan metnini tanıyor mu.

Final kümesi mühürlüdür. Dosyanın SHA-256 özeti:

```text
9298f42ef6fd28de8ab3fe3ca1a6e4126537070a1fa28eae0722c040eeaa73cc  .local/final/final.json
```

Metinler kişisel arşiv içermez ama telifli e-posta ve model çıktıları barındırdığı için depoya konmaz. Özet, dosyanın sonradan değişmediğini göstermek içindir.

## Kollar

| Kol | Yönerge |
|---|---|
| `ours` | `SKILL.md` + `references/kaliplar.md` + `references/ornekler.md` |
| `simple` | İki cümle: düz ve doğal Türkçeyle yeniden yaz; olguları, sayıları, adları, bağlantıları ve kodu koru |
| `humanizer` | blader/humanizer `SKILL.md` (İngilizce) |
| `turkce` | bushrabeg/turkce-humanizer `SKILL.md` |
| `insanca` | tahiryildiz/insanca `SKILL.md` ve kalıp dosyaları, birleştirilmiş |

Sabit sürümler [research.md](research.md) içinde. Her kol aynı yeniden yazma modeliyle (`grok-4.7-medium`), araçlar kapalı, aynı ortak çerçeveyle çalışır. Kaynak metin istemde JSON verisi olarak durur. Her çağrının yönergesi, kaynağı ve modeli parmak iziyle kaydedilir; aynı klasörde farklı bir yönergeyle yeniden koşmak reddedilir.

## Aşamalar

1. Pilot (`--stage pilot`): geliştirme kümesi, beş kol. Kör kartlarda kollar A-E harfleriyle karışık sırada gösterilir.
2. İnsan oyu: her kart için en doğal seçenek ya da `tie`/`bad`; anlam hataları seçenek harfiyle ayrı işaretlenir.
3. Ayar: oylar ve otomatik ölçümlerde becerinin belirgin hatası varsa beceri düzeltilir ve yalnız `ours` kolu yeni klasörde yeniden koşulur (`--reuse-from`).
4. Dondurma (`freeze`): rakip kol seçilir ve becerinin o anki dosya özetleri kaydedilir. Rakip seçimi sırası: en az kritik anlam hatası, sonra en çok tercih, eşitlikte sabit sıra.
5. Final (`--stage test --freeze`): mühürlü 40 metin, `ours` ile donmuş rakip, kör A/B. Dondurulmuş yönergeyle uyuşmayan bir koşu reddedilir.

## Ölçüm

İnsan oyu ana ölçüdür. Final puanı: kazanılan kart 1, berabere 0,5, kaybedilen ya da ikisi de kötü 0. Önceden belirlenen eşik: 40 kartta en az 24 puan ve `ours` için sıfır kritik anlam hatası (anlam, eksik, ekleme, sayı, özel ad). İkisinden biri tutmazsa üstünlük yazılmaz. Eksik koşu ya da eksik oyda `score` durur.

Otomatik ölçümler (`score --auto-only`):

- Kalıp yoğunluğu: önce ve sonra, 100 sözcükte ağırlıklı puan (`scripts/kontrol.py`).
- Korunan parça farkı: sayı, bağlantı, kod bloğu, satır içi kod, yer tutucu ve kayıttaki `protected` ifadeleri.
- Benzerlik: kaynakla karakter düzeyinde oran; çıktının kaynağın aynısı olup olmadığı.

Yargıç model (`judge`): ayrı bir model (`grok-4.7-high`) her çıktıyı kaynağıyla birlikte görür, kolu ve harfi görmez. Doğallık (1-5), anlam durumu (korundu, kayıp, ekleme, değişti) ve kalıp kaldı mı alanlarını JSON olarak döndürür. Yeniden yazma modeliyle aynı aileden olduğu için kendi üslubunu kayırabilir; bu yüzden insan oyunun yerine geçmez.

## Komutlar

```bash
python3 evaluate.py run --cases data/gelistirme.json --out .local/gelistirme-v1 --model grok-4.7-medium --workers 2
```

```bash
python3 evaluate.py judge --run .local/gelistirme-v1 --model grok-4.7-high
```

```bash
python3 evaluate.py score --run .local/gelistirme-v1 --auto-only
```

```bash
python3 evaluate.py cards --run .local/gelistirme-v1 --out .local/kartlar-gelistirme.md --format md
```

```bash
python3 evaluate.py vote --run .local/gelistirme-v1 --case g01 --choice B --errors D:omission
```

```bash
python3 evaluate.py freeze --pilot .local/gelistirme-v1 --out .local/freeze.json
```

```bash
python3 evaluate.py run --cases .local/final/final.json --out .local/final-run --stage test --freeze .local/freeze.json --arms ours,RAKIP --model grok-4.7-medium
```

`RAKIP`, `freeze` çıktısındaki `baseline` değeridir. Başarısız çağrılar `run --retry-failed` ile yeniden denenir; eski deneme arşivlenir. Ham akışlar `private/events/` altında saklanır.

## Gizli kalanlar

Rakip yönergeler, ham model akışları, kart-kol eşlemesi, oylar, final kümesi ve insan metinleri yalnız `.local/` altındadır.

## Bilinen sınırlar

- Kaynak modeller Grok ve Composer ile sınırlı. GPT, Gemini ve Claude çıktıları Cursor kotası nedeniyle toplanamadı.
- Yeniden yazma ve yargıç modeli aynı aileden.
- Cursor'ın kendi gizli sistem istemi tüm kolları etkiler; ortak olduğu için karşılaştırmayı bozmaz ama mutlak sonuçları etkileyebilir.
- Tek insan değerlendirici var.
- Geliştirme kümesi 10 metin; pilot sonuçları eğilim gösterir, kanıt değildir.

## Sonuçlar

### Geliştirme pilotu, 8 Kasım 2026

`.local/gelistirme-v1`: 10 metin, 5 kol, yeniden yazma modeli `grok-4.7-medium`. 50 çağrının 45'i ilk koşuda tamamlandı. 5'i 180 saniyelik zaman aşımına takıldı (4'ü insanca, 1'i ours; uzun yönergeli kollar). Zaman aşımı 480 saniyeye çıkarıldı, bu 5 çağrı `--retry-failed` ile yeniden koşuldu ve 50/50 geçerli çıktı alındı.

Otomatik ölçümler (`score --auto-only`), 10 metnin ortalaması:

| Kol | Yoğunluk önce | Yoğunluk sonra | Korunan parça uyarısı | Benzerlik | Kaynakla aynı |
|---|---:|---:|---:|---:|---:|
| ours | 13,22 | 0,53 | 0 | 0,80 | 0 |
| simple | 13,22 | 10,31 | 1 | 0,82 | 1 |
| humanizer | 13,22 | 1,01 | 4 | 0,48 | 0 |
| turkce | 13,22 | 9,03 | 4 | 0,65 | 0 |
| insanca | 13,22 | 0,18 | 4 | 0,47 | 0 |

Uyarılar elle kontrol edildi. Çoğu zararsız biçim değişikliği: sayıları yazıyla yazmak ("20" yerine "yirmi", "4" yerine "dört"), yer tutucunun içini "/" yerine "veya" ile yazmak, "namespaces, cgroups" ifadesini "namespaces ve cgroups" yapmak. Gerçek sorun turkce kolunda: iki resmî metinde (fatura e-postası, aidat duyurusu) metni düzenlemek yerine "Bu metni hukuki-idari olarak görüyorum. Onaylıyor musun?" diye onay istedi ve metni hiç vermedi. Bu, o becerinin etkileşimli akışının tek seferlik kullanımda takılmasıdır. humanizer bir e-posta şablonundaki yer tutucuları yeniden adlandırdı.

Yoğunluk bu projenin kendi kataloğuyla ölçüldüğü için `ours` lehine yanlıdır: beceri tam olarak bu kalıpları hedefliyor. Bu sütun "beceri kendi kurallarını uyguluyor mu" sorusunu yanıtlar, doğallığı değil.

Yargıç model (`grok-4.7-high`, kör, 50/50 geçerli yanıt):

| Kol | Doğallık (1-5) | Anlam korundu | Kayıp | Değişti | Kalıp kaldı |
|---|---:|---:|---:|---:|---:|
| ours | 4,2 | 10 | 0 | 0 | 0 |
| humanizer | 4,1 | 2 | 3 | 5 | 0 |
| insanca | 4,0 | 5 | 0 | 5 | 1 |
| simple | 3,3 | 7 | 0 | 3 | 8 |
| turkce | 2,9 | 4 | 1 | 5 | 9 |

Okuma: humanizer ve insanca metni daha cesur yeniden yazıyor (benzerlik 0,47-0,48); doğallık puanları bizimkine yakın ama yargıca göre çıktıların yarısında ya da daha fazlasında anlam kayıyor. turkce ve simple kalıpların çoğunu yerinde bırakıyor. `ours` en tutucu düzenleyen kollardan biri (benzerlik 0,80) ve yargıç hiçbir çıktısında anlam sorunu ya da kalan kalıp görmedi.

Sınırlar: 10 metin küçük bir örneklem. Yargıç, yeniden yazma modeliyle aynı aileden ve kaynağa yakın kalan çıktıları "anlam korundu" saymaya yatkın olabilir. Kalan sorunlar elle okumada görülüyor: bazı çıktılarda kaynaktaki çeviri kokan cümleler ("Mevcut teslim tarihi ... olmak üzere planlanan ödev") olduğu gibi kalıyor ve özet paragrafları ilk cümleyi tekrar edebiliyor.

İnsan oyu bekleniyor. Kör kartlar `.local/kartlar-gelistirme.md` dosyasında. Oylardan sonra rakip seçilecek, beceri gerekirse ayarlanıp dondurulacak ve final testi koşulacak.
