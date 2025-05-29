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
houses = soup.find_all("div", class_="title_block")
unvan1 = soup.find_all("div", class_="card_params")
many = soup.find_all("div", class_="price")

# Minimum ortaq say qədər dövr
count = min(len(houses), len(unvan1), len(many))

for i in range(count):
    ad_tag = houses[i].find("div", class_="title")
    konum_tag = unvan1[i].find("div", class_="location")
    qiymet_tag = many[i].find("span", class_="price-val")

    ad = ad_tag.get_text(strip=True) if ad_tag else ""
    konum = konum_tag.get_text(strip=True) if konum_tag else ""
    qiymet = qiymet_tag.get_text(strip=True) if qiymet_tag else ""

    if ad and konum and qiymet:
        ws.append([ad, konum, qiymet])

# Excel faylını yadda saxla
wb.save("bina_listings.xlsx")
print("Done: bina_listings.xlsx")
