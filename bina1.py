import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Define URL (bina listings)
url = "https://bina.az/"

# Request page
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Prepare Excel
wb = Workbook()
ws = wb.active
ws.title = "bina Listings"
ws.append(["Ad","Konum","Qiymet"])

# Scrape listings
houses = soup.find_all("div", class_="title_block")
for house in houses:
     ad_tag = house.find("div", class_="title") 

     ad = ad_tag.get_text(strip=True) if ad_tag else ""    
     
unvan1 = soup.find_all("div", class_="card_params")
for unvan in unvan1:  
    konum_tag = unvan.find("div", class_="location") 

    konum = konum_tag.get_text(strip=True) if konum_tag else "" 

many = soup.find_all("div", class_="price")
for manys in many:
    qiymet_tag = manys.find("span", class_="price-val")

    qiymet = qiymet_tag.get_text(strip=True) if qiymet_tag else ""

if qiymet and ad and konum:
    ws.append([ad,konum, qiymet_tag.get_text()])

# Save Excel
wb.save("bina_listings.xlsx")
print("Done: bina_listings.xlsx")