from flask import Flask, render_template

# Flask uygulamasını başlatma
app = Flask(__name__)

# Türkiye'deki 81 ilin listesi (Küçük harfli URL anahtarı : Düzgün Türkçe Adı)
cities = {
    "adana": "Adana",
    "adıyaman": "Adıyaman",
    "afyonkarahisar": "Afyonkarahisar",
    "ağrı": "Ağrı",
    "amasya": "Amasya",
    "ankara": "Ankara",
    "antalya": "Antalya",
    "artvin": "Artvin",
    "aydın": "Aydın",
    "balıkesir": "Balıkesir",
    "bilecik": "Bilecik",
    "bingöl": "Bingöl",
    "bitlis": "Bitlis",
    "bolu": "Bolu",
    "burdur": "Burdur",
    "bursa": "Bursa",
    "çanakkale": "Çanakkale",
    "çankırı": "Çankırı",
    "çorum": "Çorum",
    "denizli": "Denizli",
    "diyarbakır": "Diyarbakır",
    "edirne": "Edirne",
    "elazığ": "Elazığ",
    "erzincan": "Erzincan",
    "erzurum": "Erzurum", 
    "eskişehir": "Eskişehir",
    "gaziantep": "Gaziantep", 
    "giresun": "Giresun",
    "gümüşhane": "Gümüşhane",
    "hakkari": "Hakkari",
    "hatay": "Hatay", 
    "ısparta": "Isparta",
    "mersin": "Mersin",
    "istanbul": "İstanbul",
    "izmir": "İzmir", 
    "kars": "Kars",
    "kastamonu": "Kastamonu",
    "kayseri": "Kayseri",
    "kırklareli": "Kırklareli",
    "kırşehir": "Kırşehir",
    "kocaeli": "Kocaeli",
    "konya": "Konya",
    "kütahya": "Kütahya",
    "malatya": "Malatya",
    "manisa": "Manisa",
    "kahramanmaraş": "Kahramanmaraş",
    "mardin": "Mardin", 
    "muğla": "Muğla",
    "muş": "Muş",
    "nevşehir": "Nevşehir",
    "niğde": "Niğde",
    "ordu": "Ordu",
    "rize": "Rize",
    "sakarya": "Sakarya",
    "samsun": "Samsun",
    "siirt": "Siirt",
    "sinop": "Sinop",
    "sivas": "Sivas", # Sivas'ı manuel olarak ekledim.
    "tekirdağ": "Tekirdağ",
    "tokat": "Tokat",
    "trabzon": "Trabzon",
    "tunceli": "Tunceli",
    "şanlıurfa": "Şanlıurfa",
    "uşak": "Uşak",
    "van": "Van",
    "yozgat": "Yozgat",
    "zonguldak": "Zonguldak", 
    "aksaray": "Aksaray", 
    "bayburt": "Bayburt",
    "karaman": "Karaman",
    "kırıkkale": "Kırıkkale",
    "batman": "Batman",
    "şırnak": "Şırnak",
    "bartın": "Bartın",
    "ardahan": "Ardahan", 
    "ığdır": "Iğdır",
    "yalova": "Yalova",
    "karabük": "Karabük",
    "kilis": "Kilis",
    "osmaniye": "Osmaniye", 
    "düzce": "Düzce"
}

# Ana sayfa rotası: Tüm illeri listeler
@app.route('/')
def index():
    # 'index.html' şablonuna iller sözlüğünü gönderir
    return render_template('index.html', cities=cities)

# İl bilgi rotası: Belirli bir ilin sayfasını gösterir
@app.route('/city/<city_name>')
def city_info(city_name):
    # URL'den gelen adı küçük harfe çevirip sözlükte arar
    url_key = city_name.lower()
    display_name = cities.get(url_key)
    
    if display_name:
        # Şehir bulunursa, 'city_info.html' şablonunu gönderir.
        # display_name: Şehrin düzgün adı (örn. "Ankara")
        # url_key: Şehrin URL'de kullanılan anahtarı (örn. "ankara")
        return render_template('city_info.html', city_name_title=display_name, city_name_url=url_key)
    else:
        # Şehir bulunamazsa 404 hatası döndürür
        return "Üzgünüz, aradığınız şehir bulunamadı.", 404

# Uygulamayı başlatma kısmı
if __name__ == "_main_":
    import os
    # Portu ortam değişkeninden al (örneğin sunucular için) veya 5000'i kullan
    port = int(os.environ.get("PORT", 5000))
    # Uygulamayı tüm arayüzlerde çalıştır
    app.run(host="0.0.0.0", port=port, debug=True) # debug=True hata ayıklama için faydalıdır
