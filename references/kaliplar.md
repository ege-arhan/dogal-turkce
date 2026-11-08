# Kalıp dizini

Her kalıbın bir kimliği var (C1, A2 gibi). `scripts/kontrol.py` aynı kimliklerle çalışır; makinenin aradığı desenler `kaliplar.json` dosyasındadır. Yalnız kimlik numarası olmayan U grubu elle denetlenir.

Ağırlık üç türlüdür. **Güçlü** kalıp tek görülmesiyle düzeltilir. **Orta** kalıp çoğu durumda düzeltilir; "Dokunma" satırındaki durumlardan biriyse bırakılır. **Zayıf** kalıp insan yazısında da sık görülür; ancak aynı paragrafta başka kalıplarla birlikteyse düzeltilir.

Bazı kalıplar türe göre değişir. Örneğin "-mektedir" resmî yazıda kusur sayılmaz. Bu ayrım her maddede belirtilmiştir.

Bu sayfa hangi kalıbın neden yapay durduğunu ve nasıl düzeltileceğini anlatır. Hiçbir madde, olgu silmek ya da yeni bilgi eklemek için gerekçe olamaz.

## C. Sohbet çerçevesi

Model, cevabı bir sohbetin içine yerleştirir: önce soruyu över, sonra cevabı takdim eder, en sonda da yardım teklif eder. Düzenlenen metin bir e-posta, duyuru ya da açıklama olarak kullanılacaksa bu çerçevenin hiçbir parçası yerinde durmaz.

**C1. Onaylı ya da övgülü açılış** (güçlü). "Elbette!", "Tabii ki,", "Harika bir soru!", "Çok haklısınız." Bu ifadeleri sil ve metni doğrudan cevapla başlat.
Dokunma: Kullanıcının söylediği bir şeyi gerçekten onaylayan cevaplarda ("Evet, bu ayar kalıcıdır.") onay bilgi taşır.

**C2. Sunum ve meta cümlesi** (güçlü). "İşte size birkaç öneri:", "Aşağıda hocanıza gönderebileceğiniz örnek bir e-posta var.", "Bu yazıda ... ele alacağız.", "Gelin birlikte inceleyelim.", "Kendi bilgilerinizle değiştirmeniz yeterli." Bu cümleler içeriği değil, içeriğin teslimini anlatır. Sil; teslim edilen metin (e-posta, duyuru) kendi başına kalsın.
Dokunma: Bir kılavuzun gerçekten okura yaptığı yönlendirme ("Kurulumdan önce 2. bölümü okuyun.").

**C3. Yardım dileği ve kalıp kapanış** (güçlü, e-postada orta). "Umarım yardımcı olur.", "Başka sorunuz olursa çekinmeden sorun.", "Bol şans!" Sil.
Dokunma: E-postada gerçek bir iletişim yolu bildiren kapanış ("Sorunuz olursa 0212 ... numarasından bize ulaşabilirsiniz.") bilgi taşır; yalnız "çekinmeden" gibi dolguyu çıkar.

**C4. Devam teklifi** (güçlü). "İsterseniz size bir okuma listesi de hazırlayabilirim.", "Bütçeni söylersen ona göre daraltabilirim." Sil. Düzenlenmiş metin sohbetin devamı değildir.

**C5. Model beyanı** (güçlü). "Bir yapay zekâ olarak...", "Bilgilerim şu tarihe kadardır." Sil. Beyanın içinde gerçek bir uyarı varsa (ör. "Bu tıbbi teşhis değildir.") uyarıyı koru.

## S. Sahneleme

Sahneleme, bilgi eklemeden önem havası yaratır. Cümle bir şey söylemiyorsa, söyleyecekmiş gibi de yapmasın.

**S1. Özet kapanışı ve özet etiketi** (orta). "Sonuç olarak", "Özetle", "Kısacası", "Kısaca:" ve ardından metnin zaten söylediğinin tekrarı. Tekrar ediyorsa cümleyi tümüyle sil. Kapanış yeni bir bilgi taşıyorsa bilgiyi tut, yalnız etiketi kaldır.
Dokunma: Uzun bir raporun gerçekten özet olan bölümü.

**S2. Boş vurgu** (güçlü). "Unutmayın ki,", "Şunu belirtmek gerekir ki", "Dikkat edilmesi gereken önemli bir nokta:", "Altını çizmek isterim." Vurgu sözünü sil, ardından gelen bilgiyi düz cümleyle ver.
Dokunma: Gerçek bir uyarının kendisi ("Unutmayın: sigortayı kapatmadan prize dokunmayın.") korunur. Bu durumda yalnız "Unutmayın:" çıkarılabilir; uyarı cümlesi aynen kalır.

**S3. Retorik soru ve soru biçimli başlık** (orta). "Peki bu ne anlama geliyor?", "## Ne işe yarar?" Soruyu sil, cevabı doğrudan yaz. Kısa metinde soru başlığını cümleye dönüştür.
Dokunma: SSS biçimindeki bir sayfada sorular metnin yapısıdır.

**S4. Gereksiz karşıtlık** (orta). "X sadece bir araç değil, aynı zamanda bir yaşam biçimidir.", "Bu bir son değil, bir başlangıç." Kimse X'in yalnız araç olduğunu söylememişse karşıtlık boştur; olumlu cümleyle söyle.
Dokunma: Gerçek bir yanlış anlamayı düzelten karşıtlık ("Hata sunucuda değil, istemcide.").

**S5. Paragraf başı geçiş zinciri** (zayıf). Her paragrafın "Ayrıca,", "Bunun yanı sıra,", "Öte yandan," ile başlaması. Tek bir geçiş sorun değildir. Zincir varsa çoğunu sil; paragraflar zaten sırayla okunur.

**S6. Sıralama iskelesi** (zayıf). Kısa bir metinde "İlk olarak... İkinci olarak... Son olarak...". Üç cümlelik bir anlatımda iskele gereksizdir.
Dokunma: Sıranın önemli olduğu adımlar.

**S7. Bağlam yapıştırıcısı** (orta, resmî yazıda zayıf). "Bu bağlamda", "Bu doğrultuda", "Bu noktada". Cümleleri birbirine yapıştırmak için kullanılır, bir ilişki bildirmez. Sil ya da gerçek ilişkiyi yaz ("bu yüzden", "bunun için").

**S8. Slogan kapanış** (orta). "Küçük adımlar büyük farklar yaratır.", "En hızlı kazanım: ...", "En önemlisi:" Metnin sonuna eklenen vecize. Bilgi taşımıyorsa sil. "En hızlı kazanım" gibi bir öncelik bilgisi taşıyorsa etiketsiz, düz bir cümleye çevir ("En hızlı sonucu sabit uyku saati ve yatmadan önce ekranı bırakmak verir.").

## A. Şişirme

**A1. Önem şişirmesi** (orta, resmî yazıda zayıf). "büyük önem taşır", "kritik öneme sahiptir", "önemli bir rol oynar", "kilit rol", "vazgeçilmez". Neden önemli olduğu yazıyorsa o nedeni bırak, şişirmeyi sil. Yazmıyorsa yargıyı ölçülü söyle ("etkiler", "gereklidir").
Dokunma: Kaynak bir önem derecesini gerçekten bildiriyorsa (ör. "Bu güncelleme kritik bir güvenlik açığını kapatır.") derece korunur.

**A2. Abartılı sıfat** (güçlü). "devrim niteliğinde", "çığır açan", "oyun değiştirici", "eşsiz", "muazzam", "büyüleyici", "mükemmel bir seçim". Sıfatı sil ya da somut bilgiyle değiştir. Kaynak somut bilgi vermiyorsa sıfatı silmek yeter; yeni bilgi uydurma.

**A3. Pazarlama dili** (güçlü). "potansiyelinizi ortaya çıkarın", "... dünyasına adım atın", "kariyer yolculuğunuz", "bir üst seviyeye taşıyın", "fark yaratın", "değer katın", "Yaşam alanlarınızın konforu önceliğimizdir." Sil. Duyurulardaki kurum övgüsü de bu gruba girer.

**A4. Kapsam sıfatı** (zayıf). "kapsamlı", "derinlemesine", "detaylı bir şekilde". Metin gerçekten kapsamlı değilse sil.

**A5. Pekiştirici yığını** (zayıf). "son derece", "oldukça", "gerçekten çok". Tek başına sorun değildir. Aynı paragrafta birden fazlaysa çoğunu sil.

**A6. Sahne ve sır benzetmesi** (orta). "Fotosentez iki perdelik bir oyundur.", "Asıl sahne kloroplast.", "başrolde Rubisco", "başarının sırrı". Açıklamayı tiyatroya ya da sırra çeviren benzetme. Doğrudan söyle: "Fotosentez iki perdelik bir oyundur." yerine "Fotosentez iki aşamada olur."
Dokunma: Öğretici bir metinde tek bir benzetme anlamayı kolaylaştırıyorsa kalabilir.

## T. Çeviri kokusu

Bu kalıplar İngilizce cümle yapısının Türkçeye taşınmasından doğar. Cümle dilbilgisi açısından doğrudur ama Türkçe konuşan biri böyle kurmaz.

**T1. "Anlamına gelir"** (orta). "Bu, her gün iki kez yüksek su olduğu anlamına gelir." İngilizcedeki "this means" yapısıdır. "Bu yüzden her gün iki kez yüksek su olur." ya da "Yani ..." de.
Dokunma: Sözcük anlamı tanımları ("Kelime 'su' anlamına gelir.").

**T2. "Sahip olmak"** (orta). "Bu telefon yüksek bir performansa sahiptir.", "Üç odaya sahip bir ev." Türkçede "-ı var" ve sıfat yapısı doğaldır: "Telefonun performansı yüksek.", "Üç odalı bir ev."
Dokunma: Mülkiyet ve hukuk dili ("Şirketin yüzde 30 hissesine sahiptir.").

**T3. Boş fiil** (orta, resmî yazıda zayıf). "gerçekleştirmek", "olanak tanımak", "imkân sunmak", "katkıda bulunmak". Asıl fiili kullan: "toplantı gerçekleştirildi" yerine "toplantı yapıldı", "aramanıza olanak tanır" yerine "arayabilirsiniz".

**T4. "Yardımcı olur" ve "sağlar" bolluğu** (zayıf). "Bu, uykuya dalmanıza yardımcı olur." "Bu yöntem hız sağlar." Tek başına sorun değildir. Sıksa öznesi ve fiiliyle söyle: "Böyle daha kolay uykuya dalarsınız."

**T5. "Bir ... olarak" girişi** (orta). "Bir geliştirici olarak, bu ayarı bilmelisiniz." İngilizcedeki "As a developer" yapısıdır. "Geliştiriciyseniz bu ayarı bilmeniz gerekir."

**T6. Gereksiz iyelik zamiri** (orta). "Sizin bilgisayarınızda", "senin için en iyisi". Türkçede iyelik eki kişiyi zaten gösterir: "bilgisayarınızda".
Dokunma: Karşıtlık ya da vurgu ("Benim değil, sizin hesabınızda görünüyor.").

**T7. Türüne uymayan "-mektedir"** (sohbette güçlü; açıklama ve e-postada orta; teknik metinde zayıf; resmî yazıda muaf). "Bu yöntem hızlı çalışmaktadır." Sohbette "çalışır" ya da "çalışıyor" de.
Dokunma: Resmî yazı, tutanak, yönetmelik dili.

**T8. "Tarafından" edilgeni** (zayıf; resmî ve teknik metinde muaf). "Bu kitap Ahmet tarafından yazıldı." Gündelik metinde etken çatı daha doğaldır: "Bu kitabı Ahmet yazdı." Fail bilinmiyorsa ya da önemli değilse edilgen kalır; fail ekleme.

**T9. "Herhangi bir" bolluğu** (zayıf). "Herhangi bir sorunuz olursa" yerine "Sorunuz olursa".

**T10. Büro dolgusu** (zayıf; resmî yazıda muaf). "söz konusu", "hususunda", "itibarıyla", "ilgili olarak". Gündelik metinde "bu", "konusunda", "-den beri", "hakkında" yeter.

**T11. Adlaştırma zinciri** (orta). "Belgelerin teslim edilmesinin sağlanması gerekmektedir." Ardışık "-ması/-mesi" yığını. Fiil cümlesine çevir: "Belgelerin teslim edilmesi gerekir." ya da "Belgeleri teslim edin." (ikincisi yalnız kaynak bir talimatsa).

**T12. "Bunu yaparak"** (zayıf). "Bunu yaparak zaman kazanırsınız.", "Bu sayede", "Bu şekilde". Sık tekrar ediyorsa "Böylece" ya da yan cümleyle bağla.

## B. Biçim

Günümüz modellerinin en belirgin izi biçimdir. Kalın yazı, etiketli madde, başlık ve simge, kısa bir cevabı bile rapor gibi gösterir. Türkçe düzyazıda bunların çoğu yoktur.

**B1. Uzun tire** (orta). "Uyku hijyeniyle başla — çoğu uykusuzluk buradan düzelir." Türkçe yazıda cümle içi uzun tire nadirdir. Yerine virgül, iki nokta, noktalı virgül ya da yeni bir cümle kullan.
Dokunma: Sayı ve tarih aralıkları ("1–2 saat", "2020-2024"), diyalog çizgisi.

**B2. Kalın etiketli madde** (orta). "- **Kafein:** Öğleden sonra kesin." Etiketi kaldır; maddeyi düz bir cümle yap ya da etiketi cümlenin öznesi olarak kullan ("Kafeini öğleden sonra kesin.").
Dokunma: Gerçek bir tanım listesi (sözlükçe, parametre listesi).

**B3. Kalın yazı bolluğu** (zayıf). Bir paragrafta birden fazla kalın ifade. Kalın yazıyı tamamen kaldır; gerçekten okurun kaçırmaması gereken tek bir uyarı varsa yalnız o kalsın.

**B4. Gereksiz başlık** (orta; e-posta ve resmî yazıda güçlü). Kısa bir cevapta "## Özet", "### Nasıl çalışır?" Başlıkları kaldır, paragraflar sırayla aksın. E-postada başlık olmaz. Konu satırı ve resmî yazının başlık bloğu ("DUYURU", kurum adı) başlık sayılmaz; kalır.
Dokunma: Uzun bir teknik belgede gezinmeyi sağlayan başlıklar.

**B5. Emoji** (güçlü; sohbette orta). Sil. Kaynak gerçekten emoji kullanan bir sohbet mesajıysa ve kullanıcı sohbet tonunu korumak istiyorsa bırakılabilir.

**B6. Ünlem bolluğu** (zayıf; sohbette muaf). Açıklama, e-posta ya da resmî metinde ünlemi noktaya çevir.

**B7. Düzyazıda ok** (orta). "20 dakikadır uyuyamıyorsan → kalk." Oku sözcükle değiştir: "20 dakikadır uyuyamıyorsan kalk."
Dokunma: Kod, formül, arayüz yolu ("Ayarlar → Gizlilik").

**B8. Bağlaç yerine simge** (zayıf; teknik metinde muaf). "Yatak = uyku.", "sabah gün ışığı + kısa yürüyüş", "telefon/TV". Simgeyi sözcükle yaz: "Yatağı yalnız uyku için kullan.", "sabah gün ışığı ve kısa bir yürüyüş".

**B9. Ayraç çizgisi** (orta). Bölümleri ayıran "---" satırları. Sil; gerekiyorsa boş satır yeter.

## U. Üslup (elle denetlenir)

**U1. Telgraf üslubu.** "Can düşer. Eşleşme yoksa satır yok. Sipariş yok, NULL." Özne ve fiil atılmış, yan yana dizilmiş kısa parçalar. Kısa cümle Türkçede doğaldır; doğal olmayan, bağlantıları atılmış not dilidir. Parçaları bağlayarak tam cümle kur: "Can'ın siparişi olmadığı için sonuçta yer almaz."

**U2. Hitap kayması.** Kaynak "sen" ile başlayıp "siz"e geçiyorsa ya da tersi oluyorsa, metnin baskın hitabına uydur. Hitabı hiçbir zaman kendiliğinden değiştirme; yalnız tutarsızlığı gider.

**U3. Üçleme ritmi.** Her cümlede üç sıfat ya da üç örnek: "hızlı, güvenilir ve ölçeklenebilir". Tek bir üçleme sorun değildir. Ritim tekdüzeleşmişse bazılarını ikiye indir; çıkardığın öğe bilgi taşıyorsa başka cümlede tut.

**U4. Tekdüze paragraf.** Her paragrafın aynı biçimde kurulması (iddia, açıklama, slogan). Kalıbı kır: bazı paragrafları birleştir, sloganları sil.

**U5. Gereksiz liste ve tablo.** İki üç cümlelik bir bilgiyi madde işaretlerine bölmek. Sıralı adım, kural ya da karşılaştırma değilse düzyazıya çevir. Bilgi içeren tablo kalır.

## Aşırı düzeltme

Kalıpları temizlerken metni bozmak da yapay bir sonuçtur. Şunlardan kaçın:

- Bilgi silmek: uyarı, koşul, adım, istisna, sayı, örnek.
- Kaynakta olmayan bir şey eklemek: kişisel deneyim, duygu, yorum, deyim, argo, yazım hatası.
- Kesinliği ya da kapsamı kaydırmak: "çoğu"yu "hepsi" yapmak, "olabilir"i "olur" yapmak.
- Hitabı ve türü değiştirmek: resmî duyuruyu samimileştirmek, "siz"i "sen" yapmak.
- Yer tutucuları doldurmak ya da silmek.
- Bir kalıbı silip yerine başka bir kalıp koymak ("Elbette" yerine "Aslında").
- İşlevsel listeyi zorla düzyazıya çevirmek. Kurulum adımları liste olarak daha iyi okunur.
