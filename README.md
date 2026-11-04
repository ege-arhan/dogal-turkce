# dogal-turkce

Türkçe yapay anlatımı düzenlemek için deneysel bir beceri. Genel yazım düzelticisi değildir. Ölçülmüş kalite, kullanıcı oyu veya model başarısı iddiası yoktur. Depo: [ege-arhan/dogal-turkce](https://github.com/ege-arhan/dogal-turkce). Metin özgün MIT’tir, © 2026 Ege Arhan. İncelenen dış depoların metni kopyalanmaz.

Genel çekirdek `SKILL.md` içindedir. Düzenlemeden önce `references/examples.md` okunur. İsteğe bağlı kişisel ses yalnız yerel profilde durur; genel testte kapalıdır. Özel örneklem kısa görev mesajlarıyla sınırlıdır; genel Türkçeyi temsil etmez ve bu depoda yayımlanmaz.

Planlanan modeller şu an yok. Pilot `data/pilot.json`: 8 sentetik kayıt, Grok (Cursor grok-4.7-low). İnsan örneği değildir.

## Kurulum

Beceri klasörünün adı `dogal-turkce` olur. İçinde `SKILL.md` ve `references/` durur. Başka dosya gerekmez.

Cursor, proje veya kullanıcı:

```text
mkdir -p .cursor/skills/dogal-turkce
cp SKILL.md .cursor/skills/dogal-turkce/
cp -R references .cursor/skills/dogal-turkce/
```

```text
mkdir -p ~/.cursor/skills/dogal-turkce
cp SKILL.md ~/.cursor/skills/dogal-turkce/
cp -R references ~/.cursor/skills/dogal-turkce/
```

Codex:

```text
mkdir -p ~/.codex/skills/dogal-turkce
cp SKILL.md ~/.codex/skills/dogal-turkce/
cp -R references ~/.codex/skills/dogal-turkce/
```

Ölçüm koşusunda bu beceriyi yargı modeline önceden yükleme. Karşılaştırma, beceriyi görmeyen kolla karışmasın.

## Koşu

Ayrıntı `references/protocol.md`. Hedef final 40 kayıttır ve eşik önceden donar. Bugünkü komutlar 8’lik pilotu çalıştırır. Kart çıktısı `.json` dosyasıdır.

```text
python3 -m unittest discover -s tests -v
python3 evaluate.py run --cases data/pilot.json --out .local/pilot --arms ours,simple,humanizer,turkce --model grok-4.7-medium --workers 2
python3 evaluate.py cards --run .local/pilot --out .local/cards.json --limit 5
python3 evaluate.py vote --run .local/pilot --case p01 --choice A
python3 evaluate.py score --run .local/pilot
```

`score` bir başarı cümlesi üretmez. Pilot skoru bir eşik dondurabilir. Final koşusu `--stage test` ve o dondurulmuş dosyayı ister; tam veri kümesi olmadan kurulmaz.

Ayrıntı: `references/research.md`, `references/protocol.md`, `references/examples.md`. Sabit dış inceleme komutları `references/research.md` içindedir. Lisans: MIT, 2026 Ege Arhan.

## Karşılaştırma kaynaklarını hazırlama

Pilot dört kolu çalıştırmak için dış yönergeleri yerelde tutar. Aşağıdaki dosyalar yayımlanmaz; kullanım koşulları için kendi lisansları yanlarında bulunur. `curl` ve kimliği doğrulanmış Cursor CLI gerekir. Mevcut dosyaların üstüne indirmeden önce yeni bir klasör kullanın.

```sh
mkdir -p .local/upstream/humanizer .local/upstream/turkce-humanizer
curl --fail --location https://raw.githubusercontent.com/blader/humanizer/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/SKILL.md -o .local/upstream/humanizer/SKILL.md
curl --fail --location https://raw.githubusercontent.com/blader/humanizer/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/LICENSE -o .local/upstream/humanizer/LICENSE
curl --fail --location https://raw.githubusercontent.com/bushrabeg/turkce-humanizer/65a1a4107029ed5b5a72bc226f4937d236214484/SKILL.md -o .local/upstream/turkce-humanizer/SKILL.md
curl --fail --location https://raw.githubusercontent.com/bushrabeg/turkce-humanizer/65a1a4107029ed5b5a72bc226f4937d236214484/LICENSE -o .local/upstream/turkce-humanizer/LICENSE
```

İlk çalıştırma gerçek model kotası kullanır: pilotta 8 × 4 = 32 ayrı çağrı. En çok iki çağrı aynı anda yürür. Hata otomatik olarak yeniden denenmez; kayıtlar korunur. Aynı klasörde kaynak/yönerge/model değişikliği reddedilir. Model kullanılabilirliği hesapta ayrıca doğrulanmalıdır. Kişisel profili genel benchmark sırasında yüklemeyin.

Oy verirken en doğal bulduğunuz harfi seçin; tümü eşitse `tie`, tümü kötüyse `bad` kullanın. Anlam hatasını ilgili seçeneğe bağlayın, örneğin `--errors B:omission`. Bu hata işaretleri tercihten ayrı kaydedilir. Otomatik sayı/kod/bağlantı kontrolü yalnız bir uyarı üretir; anlamı bütünüyle doğrulamaz.
