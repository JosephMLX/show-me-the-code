import requests
from bs4 import BeautifulSoup


url = 'https://github.com/JosephMLX/show-me-the-code'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'lxml')
print(soup.body)
