from bs4 import BeautifulSoup
import requests
import json

with open("dictionary.json", "r", encoding="utf-8") as file:
    dictionary = json.load(file)

base_url = "http://odmiana.net/odmiana-przez-przypadki-rzeczownika-"
base_url2 = "https://pl.bab.la/koniugacja/polski/"

for key in dictionary:
    url = base_url + key
    response = requests.get(url).text

    soup = BeautifulSoup(response, features="html.parser")
    table = soup.find("tbody")
    if table:
        td = table.find_all("td")
        print(td)
