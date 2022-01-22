from bs4 import BeautifulSoup
import requests

url = "https://aws.amazon.com/new/?whats-new-content-all&whats-new-content-all.sort-by=item.additionalFields.postDateTime&whats-new-content-all.sort-order=desc&awsf.whats-new-database=*all&awsf.whats-new-developer-tools=*all&awsf.whats-new-end-user-computing=*all&awsf.whats-new-mobile=*all&awsf.whats-new-gametech=*all&awsf.whats-new-iot=*all&awsf.whats-new-machine-learning=*all&awsf.whats-new-management-governance=*all&awsf.whats-new-media-services=*all&awsf.whats-new-migration-transfer=*all&awsf.whats-new-networking-content-delivery=*all&awsf.whats-new-quantum-tech=*all&awsf.whats-new-robotics=*all&awsf.whats-new-satellite=*all&awsf.whats-new-security-id-compliance=*all&awsf.whats-new-serverless=*all&awsf.whats-new-storage=*all&awsf.whats-new-analytics=*all&awsf.whats-new-app-integration=*all&awsf.whats-new-arvr=*all&awsf.whats-new-blockchain=*all&awsf.whats-new-business-applications=*all&awsf.whats-new-cloud-financial-management=*all&awsf.whats-new-compute=*all&awsf.whats-new-containers=*all&awsf.whats-new-customer-enablement=*all&awsf.whats-new-customer%20engagement=*all"
request = requests.get(url).text
document = BeautifulSoup(request, "html.parser")

pages = document.find_all(class_="lb-border-p lb-box lb-has-link")

web_pages = []
for page in pages:
    a_tag = page.find('a')
    web_pages.append("https://aws.amazon.com/"+ a_tag['href'])

count = 1
for web in web_pages:
    req = requests.get(web).text
    doc = BeautifulSoup(req, "html.parser")

    article = doc.find(class_="nine columns content-with-nav").text.strip()

    with open(f'articleNumber{count}.txt', 'w') as f:
        f.write(str(article))

    count += 1

