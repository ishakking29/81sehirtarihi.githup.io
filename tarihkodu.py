from flask import Flask, render_template

app = Flask(__name__)

cities = {
    "adana": "Adana",
    "adıyaman": "Adıyaman",
    "afyonkarahisar": "Afyon",
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

@app.route('/')
def index():
    return render_template('index.html', cities=cities)

@app.route('/city/<city_name>')
def city_info(city_name):
    info = cities.get(city_name.lower())
    if info:
        return render_template('city_info.html', city_name=city_name.title(), info=info)
    else:
        return "Şehir bulunamadı", 404

if _name_ == "_main_":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)