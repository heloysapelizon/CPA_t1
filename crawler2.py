import os
import requests
from bs4 import BeautifulSoup

base_url = 'http://127.0.0.1:8000/places/default/view/'



cidades = [
    ('Afghanistan', 1),
    ('Åland Islands', 2),
    ('Albania', 3),
    ('Algeria', 4),
    ('American Samoa', 5),
    ('Andorra', 6),
    ('Angola', 7),
    ('Anguilla', 8),
    ('Antarctica', 9),
    ('Antigua and Barbuda', 10),
]


output = 'html_pages'
os.makedirs(output, exist_ok=True) 


def download_html(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"HTML salvo: {file_name}")


def crawl_places():
    for country, id in cidades:
        url = f'{base_url}{country}-{id}'       
        file_name = os.path.join(output, f'{country}.html')
        download_html(url, file_name)

