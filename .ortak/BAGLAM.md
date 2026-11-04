# Doğal Türkçe — güncel bağlam

Proje https://github.com/ege-arhan/dogal-turkce (public, MIT). Yerel kaynaklar SKILL.md, references/, evaluate.py, tests/, data/pilot.json. Kod yalnız Cursor ile yazıldı; Codex bağımsız inceleme/test.

5 Kasım 2026: 11 test geçti; özel dosyaların olmadığı temiz klasörde doğrulandı. Gerçek pilot `.local/pilot-v2`: 8 sentetik Grok kaynak × 4 yönerge =32/32 geçerli son metin. Ham akışlar ve yüzey kontrolleri yeniden doğrulandı. Bu kalite başarısı değil. İlk `.local/pilot` CLI argüman hatası arşivi; sonuç olarak kullanılmaz.

Kör kartlar `.local/kor-pilot-01-05.md` ve `06-08.md`. Anahtar private/keys.json: kullanıcı oyları bitene kadar açıklama. İnsan oyu0, rakip/final freeze yok. İlk5 için kullanıcıdan p01 A vb, eşit/hepsi kötü ve anlam hatası beklenir. Oylar evaluate.py vote ile açık kullanıcı yanıtından kaydedilir; uydurulmaz. score yalnız tüm oylar hazırsa. Genel benchmark kişisel profil kapalı.

Son40 eksik: GPT/Gemini30 kaynak kota nedeniyle toplanmadı;10 gerçek kısa kullanıcı mesajı yerelde (3sohbet,8aynıaile). GenelTürkçeyi temsil etmez. Tam son test pilot öncesinde ayrılmış sayılmaz; son test farklı kaynak aileleriyle ve yönerge sabitlendikten sonra. Kota/hesap değiştirilmez, ek kredi alınmaz.

Tüm ham/özel veri, upstream yönergeler/lisansları, anahtar, oy ve sesprofili `.local/` ve gitignore. GitHuba gitmez. Skill kurulu değil; kıyasları kirletme. Sayı/URL/kod korunumu tekbaşına anlam kanıtı değil.

Komutlar: python3 -m unittest discover -s tests -v; python3 evaluate.py cards --run .local/pilot-v2 --out .local/cards.json --limit 5; python3 evaluate.py vote --run .local/pilot-v2 --case p01 --choice A; python3 evaluate.py score --run .local/pilot-v2.
