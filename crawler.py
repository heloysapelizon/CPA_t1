import requests

from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000/places"

requisicao = requests.get(url)
if requisicao.status_code == 200:
    soup = BeautifulSoup(requisicao.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
         print(link.get('href'))
else:
    print(f"Erro: {requisicao.status_code}")
    