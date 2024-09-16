import os
import csv
from bs4 import BeautifulSoup

html = 'html_pages'
csvFile= 'countries_data.csv'


def extrairCidade(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        cidade = soup.find(id="places_country__row").find("td", class_="w2p_fw").text.strip()
        capital = soup.find(id="places_capital__row").find("td", class_="w2p_fw").text.strip()
        moeda = soup.find(id="places_currency_name__row").find("td", class_="w2p_fw").text.strip()
        codigoContinente = soup.find(id="places_continent__row").find("td", class_="w2p_fw").text.strip()
        

        continente_map = {
            "AS": "Asia",
            "EU": "Europe",
            "AF": "Africa",
            "NA": "North America",
            "SA": "South America",
            "OC": "Oceania",
            "AN": "Antarctica"
        }
        continente = continente_map.get(codigoContinente, "Unknown")
        
        return {
            'country': cidade,
            'capital': capital,
            'currency': moeda,
            'continent': continente
        }


def filesCSV():
    
    infoCidades = []

    
    for file_name in os.listdir(html):
        if file_name.endswith(".html"):
            file_path = os.path.join(html, file_name)
            country_data = extrairCidade(file_path)
            infoCidades.append(country_data)

    with open(csvFile, 'w', newline='', encoding='utf-8') as csv_file:
        campos = ['country', 'capital', 'currency', 'continent']
        writer = csv.DictWriter(csv_file, fieldnames=campos)
        
        writer.writeheader()
        writer.writerows(infoCidades)

    print(f"Dados armazenados no arquivo {csv}")

if __name__ == "__main__":
    filesCSV()