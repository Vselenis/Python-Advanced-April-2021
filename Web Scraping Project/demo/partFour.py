from bs4 import BeautifulSoup
import requests
import re

place = input("You have only a few word to describe your dream place...")
url = f"https://www.olx.bg/nedvizhimi-imoti/naemi/apartamenti/sofiya/q-{place}"
page = requests.get(url).text
document = BeautifulSoup(page, 'html.parser')

all_pages = document.find_all(class_="block br3 brc8 large tdnone lheight24")[-1]
final_page = int(all_pages.span.text)

announcements = {}
for page in range(1, final_page+1):
    url = f"https://www.olx.bg/nedvizhimi-imoti/naemi/apartamenti/sofiya/q-{place}/?page={page}"
    page = requests.get(url).text
    document = BeautifulSoup(page, "html.parser")

    items = document.find_all(class_="offer-wrapper")


    for item in items:
        price = item.find(class_='price').text.strip()
        article = item.find(class_='lheight22 margintop5')
        name = article.strong.text
        a_tag = article.find('a')
        link = a_tag["href"]


        announcements[name] = {"price": price, "link": link}

sorted_announcements = sorted(announcements.items(), key=lambda x: x[1]["price"])

for item in sorted_announcements:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])






