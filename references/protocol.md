# Protokol

Dedektör hedefi yok. Burada yazılan 40’lık final, hedef protokoldür. Bugün çalışan pilot 8 sentetik kayıttır (`data/pilot.json`). Final iddiası, tam veri kümesi durunca ve eşik o kümeden önce dondurulunca konuşulur. `score` başarı iddiası yazmaz.

## Pilot, 8

Dört kol: `simple`, `humanizer`, `turkce`, `ours`. Kör kartta A–D. Mevcut rakibi seçme sırası: en az anlam hatası, sonra tercih, sonra `simple`. Rakip pilotta seçilir. Bağımsız finalden önce dondurulur. Pilot örnekleri final kümesine taşınmaz; pilotta geliştirilen yönerge finalden önce sabitlenir. Pilot 24/40 hedefini karşılamaz.

Anlam denetimi elle, artı korunan yüzeylerin otomatik aralığı. Sayı, kod, URL, alıntı kayması anlam hatasıdır.

## Hedef final, 40

A/B: dondurulmuş rakip kola karşı `ours`. Beşli kart desteleri. Finalin içindeki destelerde aileler karışabilir.

Aynı kaynak ailesi geliştirme kümesi ile final kümesine birden girmez. Bir aile yalnız birindedir.

Aday puanı, final tamamsa: yendi 1, berabere 0,5, yenildi veya ikisi de kötü 0. Hedef 24/40 ve sıfır kritik anlam hatası. Biri eksikse üstünlük yazılmaz. Eksik koşu veya eksik oyda `score` durur.

## Gizli kalan

Üst akış istemleri, eşleme, oylar ve insan derlemi yalnız `.local` altındadır. Genel depoya konmaz.

## Komutlar

Stdlib test:

```text
python3 -m unittest discover -s tests -v
```

Pilot koşusu. Kartlar JSON’dur.

```text
python3 evaluate.py run --cases data/pilot.json --out .local/pilot --arms ours,simple,humanizer,turkce --model grok-4.7-medium --workers 2
python3 evaluate.py cards --run .local/pilot --out .local/cards.json --limit 5
python3 evaluate.py vote --run .local/pilot --case p01 --choice A
python3 evaluate.py score --run .local/pilot
```

`run` ayrıca `--stage pilot|test` ve test için `--freeze` alır. Varsayılan stage pilottur. `vote` için `--comment` ve `--errors` vardır. Hata `A:meaning` biçimindedir; seçim bir harfse yalnız etiket de yazılabilir. Etiketler: `meaning`, `omission`, `addition`, `number`, `entity`, `register`. `score` JSON basar; `efficacy_claim` boştur. Pilot skoru eşiği dondurabilir. Final koşusu bu dondurulmuş dosyayla `--stage test` ister. `evaluate.py` bu protokolün uygulayıcısıdır.
