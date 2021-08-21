from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

#print(soup.prettify())

temperatura = soup.find('p', class_='-gray _flex _align-center')

#print(temperatura.string)

print(temperatura)

print(soup.title.string)