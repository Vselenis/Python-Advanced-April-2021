import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    url = f'https://dev.bg/page/{page}/?s=junior+python&post_type=job_listing#038;post_type=job_listing'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='job-list-item')
    for item in divs:
        title = item.find('h6').text.strip()
        company = item.find('span', class_='company-name hide-for-small').text.strip()
        place = item.find('span', class_='badge').text.strip()

        if place == 'София':
            job = {
                'title': title,
                'company': company
            }
            joblist.append(job)
    return

joblist = []

for i in range(0,6):
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')
