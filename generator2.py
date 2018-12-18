from bs4 import BeautifulSoup
import requests
import json

base_url = "http://odmiana.net/odmiana-przez-przypadki-rzeczownika-"
base_url2 = "https://pl.bab.la/koniugacja/polski/"

with open("dict.txt", "r", encoding="utf-8") as file:

    words = file.readlines()
    dictionary = {}

    for word in words:

        word = word.strip()
        url = base_url + word

        request = requests.get(url).text
        soup = BeautifulSoup(request, features="html.parser")

        table = soup.find_all("td")

        if len(table) != 0:
            dictionary[word] = {"synonyms": []}
            continue

        url = base_url2 + word
        request = requests.get(url).text
        soup = BeautifulSoup(request, features="html.parser")
        table = soup.find_all("ul", attrs={"class": "sense-group-results"})

        if len(table) != 0:
            origin = table[0].contents[0].string
            print(origin)
            dictionary[origin] = {"synonyms": []}


with open("test2.json", "w+") as file:
    json.dump(dictionary, file, indent=4)
