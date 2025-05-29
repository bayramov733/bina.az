import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Sayta sorğu göndər
url = "https://bina.az/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Excel faylı üçün hazırlıq
wb = Workbook()
ws = wb.active
ws.title = "bina Listings"
ws.append(["Ad", "Konum", "Qiymet"])

# Üç listi eyni anda al
unvan = soup.find_all("div", class_="card_params")

for houses in unvan:
    ad_tag = houses.find("div", class_="location")
    konum_tag = houses.find("div", class_="name")
    qiymet_tag = houses.find("ul", class_="abs_block")

    ad = ad_tag.get_text(strip=True) if ad_tag else ""
    konum = konum_tag.get_text(strip=True) if konum_tag else ""
    qiymet = qiymet_tag.get_text(strip=True) if qiymet_tag else ""
    if ad and konum and qiymet:
        ws.append([ad, konum, qiymet])

# Excel faylını yadda saxla
wb.save("bina11_listings.xlsx")
print("Done: bina11_listings.xlsx")