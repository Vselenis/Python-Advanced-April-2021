from bs4 import BeautifulSoup
import requests

url = "https://www.emag.bg/elektrichesko-rende-einhell-tc-pl-750-750-w-shirochina-82-mm-dylbochina-na-narjazvane-10-mm-4345310/pd/D88ZX9BBM/?ref=other_customers_viewed_go_2_3&provider=rec&recid=rec_52_e595d5615538238b5803d3d5835914a8e519f06541f6895ce1c8c80321c0c1be_1642712891&scenario_ID=52"

result = requests.get(url)
document = BeautifulSoup(result.text, "html.parser")

prices = document.find(class_="product-new-price").text.strip()
price = prices[0:-6] + ',' + prices[-6:-4]

print(price)

