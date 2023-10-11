import json
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def check_url(url: str) -> bool:
  response = requests.get(url)

  if response.status_code >= 200 or response.status_code <= 299:
    print("Udało się połączyć")
  else:
    assert False


def check_temp(nazwa:str):
  url = 'https://www.meteoprog.pl/pl/weather/'+nazwa+'/'
  response = requests.get(url)
  soup = BeautifulSoup(response.content, features='html.parser')
  table = soup.find('ul',class_="today-hourly-weather hide-scroll")
  tablica = []
  print(table)
  for row in table:
     cos = 
     print(cos)

  # plt.plot(tablica)
  # plt.show()



url = 'https://api.gios.gov.pl/pjp-api/rest/station/findAll'
response = requests.get(url)
check_temp('Warszawa')
# check_url(url)

# response.content
#
# response.content.decode('utf-8')
#
# content = response.content.decode('utf-8')
# parsed_content = json.loads(content)
#
# print(type(response.content), type(content), type(parsed_content))
# for station in parsed_content:
#   print(f'ID: {station["id"]}, nazwa: {station["stationName"]}, miasto: {station["city"]["name"]}, lokalizacja: {station["addressStreet"]}')

