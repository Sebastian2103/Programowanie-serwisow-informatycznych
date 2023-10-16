import json
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import datetime

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
  span = table.find_all('span', class_="today-hourly-weather__temp")
  text = table.find_all('span',class_="today-hourly-weather__name")
  temp = []
  temp2= []
  for row in span:
      temp.append(row.getText())
  temp = [int(t.replace('°', '').replace('+', '').replace('-', '')) for t in temp]
  for a in text:
      temp2.append(a.get_text())
  print(temp2)
  plt.plot(temp2,temp)
  plt.ylabel('Temperatura (°C)')
  plt.xlabel('Czas')
  plt.title("Temperatura dla "+nazwa)
  plt.xticks(rotation=45)
  plt.show()


def check_sensor(id_stacji,id_czujnika):

  url2 = f'https://api.gios.gov.pl/pjp-api/rest/data/getData/{id_czujnika}'
  response2 = requests.get(url2)
  content2 = response2.content.decode('utf-8')
  parsed_content2 = json.loads(content2)
  dates = []
  values = []
  for entry in parsed_content2['values']:
    if entry['value'] is not None:
      dates.append(datetime.datetime.strptime(entry['date'], '%Y-%m-%d %H:%M:%S'))
      values.append(entry['value'])
  plt.plot(dates, values, label=parsed_content2['key'])
  plt.xlabel('Data')
  plt.ylabel('Wartość')
  plt.title('Wykres danych PM10')
  plt.legend()
  plt.xticks(rotation=45)
  plt.show()




sensor_id = 5766
station_id = 877
url = 'https://api.gios.gov.pl/pjp-api/rest/station/findAll'
response = requests.get(url)
check_url(url)
# check_temp("Wroclaw")
url2 = f'https://api.gios.gov.pl/pjp-api/rest/station/sensors/{station_id}'
response = requests.get(url2)

if response.status_code != 200:
  exit()

stations = json.loads(response.content.decode('utf-8'))

print(stations)


check_sensor(station_id,sensor_id)




