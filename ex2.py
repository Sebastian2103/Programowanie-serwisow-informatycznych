import requests
from bs4 import BeautifulSoup


url = 'http://wmii.uwm.edu.pl/kadra'
response = requests.get(url)

soup = BeautifulSoup(response.content, features='html.parser')
table = soup.find('table', class_='views-table cols-8').find('tbody')

for row in table:
    name = row.find('td', class_='views-field views-field-title active').text.strip()
    degree = row.find('td', class_='views-field views-field-degree').text.strip()
    phone = row.find('td', class_='views-field views-field-field-phone').text.strip()
    mail = row.find('href', class_="views-field views-field-field-email")
    print(degree, name, phone, mail)
