
# Kişisel Web Sitesi

Bu proje, Django, HTML ve CSS kullanılarak oluşturulmuş kişisel bir web sitesidir. Web sitesi, kullanıcıların çalışmalarını sergilemeleri ve blog yazıları yazmaları için bir platform sağlar.

## Özellikler

- **Kullanıcı Doğrulama**: Kayıt olma, giriş yapma ve profil yönetimi.
- **Portföy**: Projeleri açıklamalar ve resimlerle sergileme.
- **Blog**: Blog yazıları yazma, düzenleme ve silme.
- **Duyarlı Tasarım**: Farklı ekran boyutları için optimize edilmiştir.

## Kurulum

1. **Depoyu klonlayın**:
   ```bash
   git clone https://github.com/DoganayBalaban/Personal-website.git
   cd Personal-website
   ```

2. **Sanal ortam oluşturun ve aktif hale getirin**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows için `venv\Scripts\activate`
   ```

3. **Bağımlılıkları yükleyin**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrasyonları çalıştırın**:
   ```bash
   python manage.py migrate
   ```

5. **Bir süper kullanıcı oluşturun**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Geliştirme sunucusunu başlatın**:
   ```bash
   python manage.py runserver
   ```

7. **Web sitesine erişin**: Tarayıcınızda `http://127.0.0.1:8000/` adresini açın.

## Dizin Yapısı

- `base`: Temel şablonlar ve statik dosyalar.
- `env`: Sanal ortam klasörü.
- `media`: Yüklenen medya dosyaları.
- `static`: Statik dosyalar (CSS, JavaScript).
- `templates`: HTML şablonları.
- `db.sqlite3`: SQLite veritabanı dosyası.
- `manage.py`: Django proje yönetim betiği.
- `requirements.txt`: Python bağımlılıkları.

## Katkıda Bulunma

1. Depoyu forklayın.
2. Yeni bir dal oluşturun: `git checkout -b yeni-ozellik`.
3. Değişikliklerinizi yapın ve commit edin: `git commit -m 'Yeni özellik ekle'`.
4. Dalı pushlayın: `git push origin yeni-ozellik`.
5. Bir pull request açın.


## İletişim

Herhangi bir sorunuz için Doganay Balaban ile [balabandoganay@gmail.com](mailto:balabandoganay@gmail.com) adresinden iletişime geçebilirsiniz.
```