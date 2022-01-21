from bs4 import BeautifulSoup

with open("indexTwo.html", "r") as f:
    document = BeautifulSoup(f, "html.parser")

tags = document.find_all('input', type="text")
for tag in tags:
    tag['placeholder'] = "I Love to change things :)"

with open('change.html', 'w') as f:
    f.write(str(document))
