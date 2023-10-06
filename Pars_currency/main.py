import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as BS
import numpy as np
import requests


url = 'https://ru.investing.com/currencies/streaming-forex-rates-majors'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36'}

def print_dict_as_columns(dict_curr):
    keys = list(dict_curr.keys())
    for i in range(len(dict_curr[keys[0]])):  # Используем длину значений первого ключа
        for key in keys:
            print(f"{key}: {dict_curr[key][i]}")
            print(dict_curr)


def select_filter(items: dict):
    print('Выберите валюту:')
    [print(f"{item + 1}: {items['Currency'][item]}") for item in range(len(items["Currency"]))]
    select = int(input("Ваш выбор: "))
    return [items['Currency'][select-1], items['Link'][select-1]]

def select_from_url(currency: str, link: str) -> dict:
    from datetime import date
    print(link)
    # date (data) need convert to list
    # value -> list
    # percentage -> list
    return {"Currency": currency, "Link": link, "Date": str(date.today()), "Value": None, "Percentage": None}







def find_curr(url):
    count = 0
    links = []
    name_currency = []
    total_links = []
    dict_curr = {'Currency': [], 'Link': []}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
         soup = BS(response.text, 'html.parser')
         for link in soup.find_all('a', class_='inv-link bold datatable_cell--name__link__2xqgx'):
             for new_link in link.find_all('h4', class_='flex align-middle'):
                name = link.get('title')
                total_link = "https://ru.investing.com/" + link.get('href')
                count = count+1
                dict_curr['Currency'].append(name)  # Добавляем 'name' в ключ 'Currency'
                dict_curr['Link'].append(total_link)
                #print(link)
                #print(total_link)
                #print(name)
                name_currency.append(name)
                links.append(link)
                total_links.append(total_link)
    except Exception as e:
        print(f"Error: {e}")
    return dict_curr

def main():
    result = find_curr(url)
    print_dict_as_columns(result)
    select = select_filter(result)
    data = select_from_url(select[0],select[1])
    print(data)

if __name__ == '__main__':
    main()