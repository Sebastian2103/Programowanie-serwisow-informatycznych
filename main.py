import requests

url = 'http://wmii.uwm.edu.pl/'

response = requests.get(url)

print(response.status_code)
print(response.headers)
print(response.content.decode('utf-8'))
