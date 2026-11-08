# Araştırma notu

Bu not, kalıp kataloğunun ve koruma kurallarının nereden geldiğini anlatır. Buradaki sayılar `scripts/kontrol.py` ile yeniden üretilebilir. Kalite iddiası değildir; insan oyu yerine geçmez.

## Türkçeye özgü sınırlar

İngilizce insanlaştırıcıların bazı kuralları Türkçede zarar verir. Beceri bu yüzden aşağıdakileri kusur saymaz ve korur:

- Özne düşürme Türkçede dilbilgisidir. Açık özne çoğu zaman karşıtlık ya da odak taşır ("Ben gelemem, o gelsin."). Toplu silmek anlamı değiştirir.
- `-miş` ile `-di` aynı geçmiş değildir. `-miş` aktarım, çıkarım ya da şaşırma bildirebilir; `-di`ye çevirmek kaynağın kesinliğini artırır.
- Nicelik sözcükleri ("çoğu", "bazı", "tüm", "hiç") birbirinin yerine geçmez.
- Edilgen ve `-mektedir` resmî yazıda olağandır. Katalog bu kalıbı `formal` türünde saymaz.
- Rica ve nezaket kipleri ("rica ederiz", "-ebilir misiniz") hitap ilişkisini taşır, dolgu değildir.

Okuma listesi:

- [Discourse management, reference tracking, speech and gesture in Turkish](https://www.mpi.nl/publications/item2095735/discourse-management-reference-tracking-speech-and-gesture-turkish)
- [arXiv:cmp-lg/9407017](https://arxiv.org/abs/cmp-lg/9407017)
- [arXiv:2207.05008](https://arxiv.org/abs/2207.05008)
- [Benjamins SLCS 175.09](https://www.benjamins.com/catalog/slcs.175.09aks)

TDK Yazım Kılavuzu imla kaynağıdır; doğallık ölçütü olarak kullanılmadı.

## Geliştirme derlemi

`data/derlem/arastirma.json`: 30 soru, her türden 6 (sohbet, açıklama, e-posta, teknik, resmî). Her soru Cursor'ın ask modunda, ek yönerge olmadan bir modele soruldu ve varsayılan yanıt kaydedildi. Modeller: `cursor-grok-4.5-medium` (10), `cursor-grok-4.6-medium` (10), `composer-2.5` (10). Toplam 5.574 sözcük. Final setindeki 30 soru aynı anda ama ayrı yazıldı ve metinleri katalog yazılırken okunmadı.

Kalıp taraması (8 Kasım 2026, katalog sürüm 1):

| Grup | Ağırlıklı puan | Pay |
|---|---:|---:|
| Biçim (B) | 729 | %93 |
| Sahneleme (S) | 23 | %3 |
| Sohbet çerçevesi (C) | 18 | %2 |
| Çeviri kokusu (T) | 10 | %1 |
| Şişirme (A) | 7 | %1 |

En sık kalıplar: kalın yazı bolluğu (B3, 267 kez, 30 metnin 27'sinde), kalın etiketli madde (B2, 102 kez, 19 metin), gereksiz başlık (B4, 51 kez, 8 metin), uzun tire (B1, 28 kez, 10 metin), ayraç çizgisi (B9, 7 metin), düzyazıda ok (B7, 9 metin), bağlaç yerine simge (B8, 5 metin).

Ortalama yoğunluk 100 sözcükte 13,11 puan. Türlere göre: sohbet 15,2; açıklama 15,33; e-posta 6,19; teknik 17,0; resmî 11,83.

Ana bulgu: güncel modellerin Türkçe varsayılan yanıtlarında yapaylığın büyük kısmı biçimden geliyor. Kalın etiketli madde listesi, başlık, tire ve ok neredeyse her yanıtta var. "Önemli bir rol oynar" türü sözcük kalıpları beklenenden seyrek. Eski Türkçe insanlaştırıcıların sözcük listesine dayanması bu yüzden yetersiz kalıyor.

Sınır: katalog bu derlem okunarak yazıldı, dolayısıyla bu sayılar katalogun kendi derlemine uyumunu gösterir, genellenebilirliğini değil. Kaynak modeller Grok ve Composer ile sınırlı; GPT, Gemini ve Claude çıktıları kota yüzünden toplanamadı.

## İnsan metni kontrolü

Final setindeki 10 insan metni (2012-2019 arası Debian Türkçe e-posta listeleri, 2018 Vikipedi sürümleri, 2019 Resmî Gazete ilanları) aynı araçla tarandı. Ortalama yoğunluk 100 sözcükte 1,09. Altı metinde hiç bulgu yok. Bulguların hepsi zayıf ya da orta ağırlıklı sözcük kalıpları: "tarafından", "sahip", "oldukça", "inanılmaz", "gerçekleştirilir" ve bir `ls` çıktısındaki `->`.

Bu iki şeyi gösteriyor. Birincisi, biçim kalıpları insan metninde neredeyse hiç yok, güçlü sinyal oldukları için ağırlıkları yüksek tutuldu. İkincisi, çeviri ve şişirme sözcükleri insanlar tarafından da kullanılıyor; tek başına görüldüklerinde yapaylık kanıtı değiller. Beceri bu yüzden bunları "yığılınca" düzeltir.

## Kişisel arşiv

Kullanıcının Codex ve Claude sohbet arşivi (yaklaşık 1,7 milyon asistan sözcüğü) n-gram düzeyinde tarandı. Sonuç güvenilir bir sinyal vermedi: en sık asistan kalıpları araç çıktısı, dosya yolları ve kod kalıntısıydı. Arşivden kural türetilmedi. Kişisel veri depoya girmedi.

## Önceki iş

İncelenen depolar ve değerlendirmede kullanılan sabit sürümler:

- [blader/humanizer](https://github.com/blader/humanizer) `0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0`, MIT, © 2025 Siqi Chen. İngilizce; Wikipedia'nın "Signs of AI writing" listesine dayanır.
- [bushrabeg/turkce-humanizer](https://github.com/bushrabeg/turkce-humanizer) `65a1a4107029ed5b5a72bc226f4937d236214484`, MIT, © 2026 bushrabeg. Türkçe, tek dosya.
- [tahiryildiz/insanca](https://github.com/tahiryildiz/insanca) `1d2e92ba9ac4613fe2cfce4125bb28b4fa896544`, MIT, © 2026 Tahir Yıldız. Türkçe, çok dosyalı kalıp kataloğu.

Ayrıca okunanlar: Humanizer-zh, stop-slop, turkish-writer. Lieflat CC BY-NC lisanslı olduğu için yalnız okundu. Bu depolardan metin, liste ya da örnek kopyalanmadı; katalog ve örnekler bu proje için yazıldı.

Değerlendirme için rakip yönergeler yerelde indirilir ve yayımlanmaz:

```bash
mkdir -p .local/upstream/humanizer .local/upstream/turkce-humanizer
```

```bash
curl --fail -L https://raw.githubusercontent.com/blader/humanizer/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/SKILL.md -o .local/upstream/humanizer/SKILL.md
```

```bash
curl --fail -L https://raw.githubusercontent.com/bushrabeg/turkce-humanizer/65a1a4107029ed5b5a72bc226f4937d236214484/SKILL.md -o .local/upstream/turkce-humanizer/SKILL.md
```

```bash
git clone https://github.com/tahiryildiz/insanca.git .local/upstream/insanca-git && git -C .local/upstream/insanca-git checkout 1d2e92ba9ac4613fe2cfce4125bb28b4fa896544
```

insanca için `evaluate.py`, `.local/upstream/insanca/` altında `SKILL.md` ile `references/akis-kurallari.md` ve `references/kaliplar/*.md` dosyalarını bekler (tam liste `evaluate.py` içindeki `_prompt_files`). Araçlar kapalı çalıştığı için çok dosyalı beceriler tek istemde birleştirilir; her dosyanın başına adı yazılır.
