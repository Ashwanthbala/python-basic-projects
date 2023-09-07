import requests
from bs4 import BeautifulSoup

response = requests.get("https://wisdompetmed.com/")
soup = BeautifulSoup(response.text)
print(soup)
links = soup.find_all("div", class_="collapse navbar-collapse")
for i in links:
    print(i.text)

