import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://riven.market/list/PC'

session = requests.session()

response = session.get(url)
# response = requests.get('https://riven.market/list/PC')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='riven')

for post in posts:
    print(post)