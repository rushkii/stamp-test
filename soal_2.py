# Soal 2: Menampilkan ramalan cuaca kota Jakarta untuk 5 hari kedepan

# 1. Silakan gunakan API yang disediakan http://openweathermap.org
# 2. Tolong tampilkan output berupa ramalan cuaca kota Jakarta untuk 5 hari ke depan
# 3. Yang ditampilkan hanya 1 suhu per hari
# 4. Soal ini tidak membutuhkan akun berbayar.


# Install requests terlebih dahulu jika belum ada menggunakan `pip3 install requests`
import requests
from datetime import datetime


GEO_API_URL = "http://api.openweathermap.org/geo/1.0/direct"
FC_API_URL = "http://api.openweathermap.org/data/2.5/forecast"
API_KEY = "" # YOUR OPENWEATHERMAP API KEY


def human_date(dt: datetime) -> str:
    """
    Mengubah datetime object menjadi datetime string secara terformat.
    """
    return dt.strftime("%a, %d %b %Y")


def get_coord_by_city_name(city_name: str) -> tuple[int, int]:
    """
    Ambil koordinat berdasarkan nama kota.
    """
    response = requests.get(url=GEO_API_URL, params={"q": city_name, "limit": 1, "appid": API_KEY})
    data = response.json()[0]
    return data["lat"], data["lon"]


def get_5day_forecast(lat: int, lon: int) -> str:
    """
    Mengambil data prakiraan cuaca selama 5 hari kedepan.
    """
    result = ""
    response = requests.get(url=FC_API_URL, params={"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric", "cnt": 40})
    data = response.json()

    for item in data["list"]:
        dt = datetime.fromtimestamp(item["dt"])

        # Karena response API forecast mengembalikan hasil prakiraan cuaca-
        # selama 5 hari setiap jamnya, jadi ambil hanya salah satu jamnya saja.
        if item["dt_txt"].endswith("00:00:00"):
            result += f"{human_date(dt)}: {item['main']['temp']}°C\n"

    return result.rstrip("\n")


def answer():
    # Menggunakan lat & long Jakarta yang sudah disediakan.
    # lat, lon = -6.2146, 106.8451

    # Atau menggunakan API geo.
    lat, lon = get_coord_by_city_name("Jakarta")
    result = get_5day_forecast(lat, lon)
    print(result)


if __name__ == "__main__":
    answer()
