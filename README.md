
# Iha Kiralama Projesi

Fonksiyonalite;

- Üyelik ve Giriş Ekranı
- İHA Kayıt Sayfası ( İHA Marka, Model, Ağırlık , Kategori vb) - İHA Listeleme
- İHA Listelemede filtre ve arama özelliği
- İHA Silme
- İHA Güncelleme



## Proje Hakkında

Kullanıcılar siteye kayıt olup giriş yapabilir.  2 tane rol ayarlanmıştır. Bunlardan biri superuser yani admindir. Admin iha kaydı oluşturabilir. (IHA Marka, Model, Ağırlık , Kategori) Oluşturduğu bu kaydı silebilir ve değiştirebilir. Bir diğer rolümüz ise user. Admin olmayan user superadminin oluşturduğu iha kayıtlarından birini seçerek ve kiralama başlangıç tarihi, kiralama bitiş tarihi girerek iha kiralayabilir. Aynı zamanda ara yüzünde kendi kiraladığı ihaları görebilir. Superadminin paneline ise hangi userın handi ihayı kiraladığı ve bununla ilgili bilgileri düşer.

  
## Özellikler

- Proje Python Django ile gerçekleştirilmiştir.
- Veritabanı olarak postgresql kullanılmıştır.
- RestFramework, bootstrap5, crispy, psycopg2 gibi kütüphaneler kullanılmıştır.
- Ön yüzde çok az javascript kullanılmıştır. (delete, update işlemlerinde)
- İlişkisel tablolar ayrı ayrı tutulmuştur. 3 tane veritabanı mevcuttur. Birincisi kullanıcıların olduğu veritabanı, ihaların olduğu veritabanı ve kullanıcının kiralamış olduğu ihaların yer aldığı veritabanı. Sondaki veritabanında user ve iha id(foreign_key) ile bağlanmıştır.
- search, filtreleme ve listeleme işlemleri yapılmıştır.
- Şifre hash şeklinde tutulmuştur.

## Projeyi çalıştırmak


#### Docker

```http
  docker-compose up -d --build
```

#### Projeyi başlatmak

```http
  python manage.py runserver
```



  
## Ekran Görüntüleri

# Login sayfası. Kullanıcı siteye authenticate olur. Sadece username ve password ile giriş yapabilir. Validate işlemleri gerçekleştirilmiştir. Eğer bilgileri hatalıysa hata mesajı döner.
![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/loginPage.png)

# Sign in sayfası. Kullanıcı siteye kayıt olur. User name, email, ad, soyaad, şifre ve şifre tekrar bilgilerini girer. 
![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/RegisterPage.png)

# Iha Kayıt sayfası. Superuser buradan iha bilgilerini (brand,model,weight,category) girip kayıt oluşturur.
![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/IhaKay%C4%B1t.png)

# Iha Listeleme sayfası. Oluşturulan kayıtlar burada listelenir. Bu sayfaya userın da erişimi vardır. Ayrıca search ve filtreleme işlemi de burada gerçekleştirilmiştir. Brand ve categoriye göre listeleme yapmaktadır.

![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/ihaList.png)

# Iha Detay sayfası. Ayrıntılı bilgiye tıklandığında, tıklanan ürünün tüm bilgileri /iha-list/id urlnde döner.
![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/IhaListDetail.png)

# Iha Düzenle sayfası. Düzenleye tıklandığı zaman iha kaydı silinebilir veya update edilebilir.
![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/%C4%B0haDeleteUpdateDetail.png)

# User panel sayfası. Userın panelinde adminden farklı olarak İha Kirala ve kiraladığım ihalarım sayfası vardır.
![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/userpanel.png)

# İha kirala sayfası. User kiralayacağı ihayı, start ve end dateleri seçer.
![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/renIhaa.png)

# Kiraladığım ihalar sayfası. User kiraladığı ihaları görür.
![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/myIha.png)

# Rent Iha database
![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/databaseRecord.png)

# Docker

![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/dockerComposeUp.png)
![Uygulama Ekran Görüntüsü](https://github.com/isikduygu/RentIha/blob/32529acefb4ce13b894c873b8275dcab48428d7d/SS/dockerContainer.png)



  
## Eksiklikler

- Backend kısmına ağırlık verildiği için ve Frontend kısmı biraz zayıf kalmıştır.
- Birim testi yazılmamıştır.
- Permission kısımlarında eksiklikler vardır.
- Search işlemi sadece brand (marka) ve category kısmında çalışmaktadır.
- Silme ve kayıt alma işlemlerinden sonra bazı yerlerde yönlendirme yapılmı bazı yerlerde yapılmamıştır.


  
