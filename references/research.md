# Araştırma notu

Bu depoda ölçülmüş kalite, kullanıcı oyu veya model başarısı iddiası yoktur. Aşağıdaki ayrım kasıtlıdır. Kaynaklar önceki okumadan durur; bu not için yeniden indirilmedi. Başlık ve sonuç uydurulmaz.

## Kanıt diye kullanılanlar

Türkçede özne düşürme dilbilgisidir; açık özne çoğu zaman karşıtlık veya odak taşır. `-miş` ile `-di` aynı geçmiş değildir. `-miş` yalnız aktarım değildir; çıkarım, bitmişlik veya görünüş de olabilir. `-di` kendiliğinden görgü tanığı değildir. Kaynaktaki kip durur. `çoğu`, `bazı`, `tüm`, `hiç` birbirinin yerine geçmez. Bunlar düzenleme yasağımızın gerekçesidir, üslup tercihi değil.

Okuma listesi:

- [Discourse management, reference tracking, speech and gesture in Turkish](https://www.mpi.nl/publications/item2095735/discourse-management-reference-tracking-speech-and-gesture-turkish)
- [arXiv:cmp-lg/9407017](https://arxiv.org/abs/cmp-lg/9407017)
- [arXiv:2207.05008](https://arxiv.org/abs/2207.05008)
- [Benjamins SLCS 175.09](https://www.benjamins.com/catalog/slcs.175.09aks)

TDK yazım kılavuzu imla içindir. Doğallık veya üslup ölçütü sayılmaz.

## Hipotez

Model metninde sıkışmanın bir bölümü boş açılış, boş kapanış, çevrilmiş kalıp ve aynı haberin tekrarı olabilir. Açık özneyi, edilgeni, bağlacı veya sözcük sırasını toplu silmek anlam götürebilir. Bu hipotezdir. Pilot ve tam 40’lık küme ölçülmeden kural haline gelmez.

## Önceki iş

İnceleme hedefi, kopya değil: [blader/humanizer](https://github.com/blader/humanizer) 3.1.0, `0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0`, MIT, © 2025 Siqi Chen; [bushrabeg/turkce-humanizer](https://github.com/bushrabeg/turkce-humanizer) `65a1a4107029ed5b5a72bc226f4937d236214484`, MIT, © 2026 bushrabeg. Ayrıca Humanizer-zh, stop-slop, insanca, turkish-writer. Lieflat CC-BY-NC: metin, liste veya örnek kopyalanmaz.

Bu deponun metni özgün MIT metnidir, © 2026 Ege Arhan. Yukarıdaki depolardan kural listesi veya örnek taşınmaz. İngilizce insanlaştırıcıların hepsi özne düşürmeyi kusur saymaz. Bu depo böyle bir listeyi varsayılan kusur listesi yapmaz.

Sabit indirme, inceleme içindir:

```text
git clone https://github.com/blader/humanizer.git
git -C humanizer checkout 0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0
git clone https://github.com/bushrabeg/turkce-humanizer.git
git -C turkce-humanizer checkout 65a1a4107029ed5b5a72bc226f4937d236214484
```

## Veri gerçeği

Planlanan modeller şu an yok. Mevcut pilot Grok kullanır: `data/pilot.json`, sekiz sentetik kayıt, Cursor grok-4.7-low. Bu kayıtlar insan örneği değildir ve bir modelin başarısını göstermez.

Tutulan kümenin hedefi 40 örnektir. Tür başına 6, model kaynaklı 30, insan 10. Aynı kaynak ailesi geliştirme kümesi ile final kümesinde birden durmaz. İnsan örnekleri kısa görev sohbetidir; insan kökeni düzgün düzyazı demek değildir.

Kişisel profil repoda yoktur. Ayrı yerel nottaki yaklaşık 10 özel görev iletisi temsilî değildir. Genel test profili kapalıdır.
