# dogal-turkce

Yapay zekânın yazdığı Türkçe metni, anlamına dokunmadan insan eli değmiş gibi okunur hâle getiren bir beceri (skill). Claude Code, Cursor ve Codex'te çalışır.

İngilizce için yazılmış "humanizer" becerileri Türkçede iyi sonuç vermiyor. Kurallarının bir kısmı Türkçeye uymuyor: özneyi düşürmek Türkçede kusur değil, dilbilgisinin kendisi; edilgen çatı resmî yazıda olağan; `-miş` ile `-di` arasındaki fark anlam taşır. Türkçe modellerin kendine özgü kalıpları da o listelerde yok: "önemli bir rol oynar", "-mektedir" yığını, "sağlar" ve "yardımcı olur" bolluğu, çeviri kokan "sahip olmak". Bu proje sıfırdan, Türkçe için yazıldı.

## Ne yapar

```text
Önce:
Harika bir soru! Kitap okuma alışkanlığı kazanmak, kişisel gelişim yolculuğunuzda son derece
önemli bir rol oynar. İşte size yardımcı olabilecek bazı etkili ipuçları:

- **Küçük başlayın:** Günde sadece 10 sayfa okuyarak başlayabilirsiniz — bu, alışkanlığın
  sürdürülebilir olmasını sağlar.
- **Sabit bir zaman belirleyin:** Her gün aynı saatte okumak, beyninizin bu aktiviteyi bir
  rutin olarak algılamasına yardımcı olur.
...
Unutmayın, önemli olan miktar değil, süreklilik! 📚 Umarım bu öneriler işinize yarar.

Sonra:
Günde 10 sayfayla başlayabilirsiniz. Bu kadar az olunca sürdürmek kolaylaşır.

- Her gün aynı saatte okuyun; okumak zamanla rutine dönüşür.
...
Önemli olan çok okumak değil, her gün okumak.
```

Övgülü açılış, şişirme, kalın etiketli maddeler, uzun tire, slogan kapanış, emoji ve yardım dileği gider. Sayı, hitap ("siz"), önerilerin hepsi ve asıl fikir kalır. Beş türden tam örnek [references/ornekler.md](references/ornekler.md) içinde.

Beceri bir editör gibi çalışır, yeni bilgi eklemez. Olguları, sayıları, kapsamı ("çoğu" ile "tüm" aynı şey değil), olumsuzluğu, kipi, zaman ekini, hitabı, kodu, bağlantıları ve yer tutucuları korur. Metinde belirgin bir yapay kalıp yoksa olduğu gibi bırakır.

## Kurulum

Klasörü kopyalamak yeter. `scripts/` isteğe bağlıdır; düzenleme sonrası otomatik kontrol için gerekir.

Claude Code (kullanıcı geneli):

```bash
git clone https://github.com/ege-arhan/dogal-turkce.git /tmp/dogal-turkce && mkdir -p ~/.claude/skills/dogal-turkce && cp -R /tmp/dogal-turkce/SKILL.md /tmp/dogal-turkce/references /tmp/dogal-turkce/scripts ~/.claude/skills/dogal-turkce/
```

Cursor (proje içinde `.cursor/skills/`, kullanıcı geneli için `~/.cursor/skills/`):

```bash
mkdir -p .cursor/skills/dogal-turkce && cp -R /tmp/dogal-turkce/SKILL.md /tmp/dogal-turkce/references /tmp/dogal-turkce/scripts .cursor/skills/dogal-turkce/
```

Codex:

```bash
mkdir -p ~/.codex/skills/dogal-turkce && cp -R /tmp/dogal-turkce/SKILL.md /tmp/dogal-turkce/references /tmp/dogal-turkce/scripts ~/.codex/skills/dogal-turkce/
```

Beceri desteği olmayan bir araçta `SKILL.md`, `references/kaliplar.md` ve `references/ornekler.md` dosyalarını sistem istemine eklemek de işe yarar.

## Kullanım

Metni verip "doğallaştır", "insanlaştır", "yapay zekâ kokusunu gider" ya da "bu metin çok yapay duruyor" demek yeterli. İsteğe bağlı olarak okuru, tonu, hitabı (sen/siz) ve yoğunluğu (`tam` ya da `hafif`) belirtebilirsiniz. `hafif` yalnız güçlü kalıpları temizler.

Kendi üslubunuza yaklaştırmak isterseniz [references/profil.md](references/profil.md) şablonuyla bir profil hazırlayın ve depo dışında tutun.

## Kontrol aracı

`scripts/kontrol.py` yalnız Python standart kütüphanesiyle çalışır. Kalıp kataloğunu ([references/kaliplar.json](references/kaliplar.json)) tarar ve düzenlemede korunması gereken parçaların değişip değişmediğine bakar.

```bash
python3 scripts/kontrol.py tara metin.txt --tur chat
```

```bash
python3 scripts/kontrol.py karsilastir kaynak.txt cikti.txt --tur email
```

`tara` her bulguyu kalıp kimliğiyle listeler ve 100 sözcük başına ağırlıklı yoğunluk verir. `karsilastir` iki metnin yoğunluğunu karşılaştırır; sayı, bağlantı, kod bloğu, satır içi kod veya yer tutucu kaybolduysa ya da değiştiyse çıkış kodu 1 olur. Bu araç bir yapay zekâ dedektörü değildir. Kalıp sayısı düşük bir metin kötü yazılmış olabilir; anlamı yine insan okumalıdır.

Türler: `chat`, `explanation`, `email`, `technical`, `formal`. Bazı kalıpların ağırlığı türe göre değişir; örneğin `-mektedir` resmî yazıda sayılmaz.

## Değerlendirme

Değerlendirme düzeni [references/protocol.md](references/protocol.md) içinde. Kısaca:

1. Geliştirme pilotu: 10 gerçek model çıktısı, beş kol (bu beceri, tek cümlelik basit istem, blader/humanizer, bushrabeg/turkce-humanizer, insanca). Aynı yeniden yazma modeli, kör kartlar.
2. Pilottan sonra beceri ve rakip kol dondurulur; dosya özetleri kaydedilir.
3. Final: önceden ayrılmış ve mühürlenmiş 40 metin (30 model çıktısı, 2019 öncesinden 10 insan metni). Bu beceri ile donmuş rakip, kör A/B karşılaştırmasıyla yarışır.

Otomatik ölçümler (kalıp yoğunluğu, korunan parça farkı, benzerlik) ve ayrı bir yargıç model yalnız yardımcı sinyaldir. Başarı kararını insan oyu verir.

## Durum

8 Kasım 2026 itibarıyla 10 gerçek model çıktısıyla geliştirme pilotu tamamlandı. Yardımcı sinyaller olumlu:

- Bu becerinin çıktılarında sayı, bağlantı, kod ya da yer tutucu değişikliği yok (0/10). Rakip kollarda 1-4 uyarı var; çoğu zararsız biçim farkı, ikisi metni hiç vermeyen yanıt.
- Ayrı bir yargıç model doğallığa 5 üzerinden 4,2 verdi (en yakın rakipler 4,1 ve 4,0). Anlamı 10 çıktının 10'unda korunmuş buldu. En yakın iki rakipte anlam 10 çıktının 5'inde ve 8'inde kaymıştı.

İnsan oylaması bekleniyor. Final testi henüz koşulmadı; bu yüzden depoda bir üstünlük iddiası yok. Ayrıntılar [references/protocol.md](references/protocol.md) dosyasının "Sonuçlar" bölümünde.

Bilinen sınırlar: kaynak metinler Grok ve Composer modellerinden geliyor (GPT, Gemini ve Claude çıktıları kota nedeniyle toplanamadı). Yeniden yazma ve yargıç modeli aynı aileden. Cursor'ın kendi gizli sistem istemi tüm kolları aynı biçimde etkiliyor.

## Geliştirme

```bash
python3 -m unittest discover -s tests -v
```

Değerlendirme hattı `evaluate.py` içinde: `run`, `cards`, `vote`, `judge`, `score`, `freeze`. Ham çıktılar, oylar ve kişisel veriler `.local/` altında kalır ve depoya girmez. Rakip becerilerin indirilmesi ve sabit sürümleri [references/research.md](references/research.md) içinde.

## Lisans

MIT, © 2026 Ege Arhan. İncelenen dış depolardan kural listesi veya örnek kopyalanmadı.
