'''Создать парсер курс валют и по ним сделтаь графики через Matplotlib'''
import datetime

import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from bs4 import BeautifulSoup as BS
import numpy as np
import requests
from window import Window
import pprint
import time
import re
import locale

url = 'https://ru.investing.com/currencies/streaming-forex-rates-majors'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36'}

def print_dict_as_columns(dict_curr):
    keys = list(dict_curr.keys())
    for i in range(len(dict_curr[keys[0]])):
        for key in keys:
            print(f"{key}: {dict_curr[key][i]}")
            #print(dict_curr)

def select_filter(items: dict):
    print('Выберите валюту:')
    [print(f"{item + 1}: {items['Currency'][item]}") for item in range(len(items["Currency"]))]
    select = int(input("Ваш выбор: "))
    return [items['Currency'][select-1], items['Link'][select-1]]

def select_from_url(currency: str, link: str) -> dict:
    from datetime import date
    # print(link)
    # date (data) need convert to list
    # value -> list
    # percentage -> list
    return {"Currency": currency, "Link": link, "Date": str(date.today())}


def choice_time(data_for_choice, currency):
    print('Строить график от текушего времени, до выбранного\n'
          'или с определенной даты до определенной?\n')
    while True:
        try:
            choice = int(input('Введите "1" или "2" соответственно: '))
            if choice in (1,2):
                break
            else:
                print("Недопустимое число, введите число заново!")
        except ValueError as ve:
            print(f'Недопустимое значение, введите число! {ve}')

    if choice == 1:
        while True:
            pars_currency(data_for_choice, currency)
            time.sleep(1)
    else:
        return pars_history_tabel(data_for_choice + "-historical-data", currency)


def pars_currency(choice,currency):
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    values = []
    timeline = []
    try:
        response = requests.get(choice, headers=headers)
        if response.status_code == 200:
            soup = BS(response.text, 'html.parser')
            time = datetime.datetime.now()
            #test = soup.find_all('div', class_='text-5xl font-bold leading-9 md:text-[42px] md:leading-[60px] text-[#232526]')
            #test = test[0]
            #text = test.text
            #print(text)
            value = soup.find(attrs={"data-test": "instrument-price-last"})
            if value:
                value = locale.atof(soup.find(attrs={"data-test": "instrument-price-last"}).text.strip())
                print(f"Текущий курс {currency}", value)
            else:
                value = soup.find_all('div', class_="text-5xl") #locale.atof(soup.find(attrs={"class": "text-5xl font-bold leading-9 md:text-[42px] md:leading-[60px] text-[#232526]"}).text.strip())
                if value is not None:
                    text = value[0]
                    value_text = text.text
                    value_text = value_text.replace('.','')
                    value = locale.atof(value_text)
                    print(f"Текущий курс {currency}", value)
            timeline.append(time)
            values.append(value)
            plt.ion()
            fig, ax = plt.subplots()
            line1, = ax.plot(timeline, values)
            ax.legend()
            plt.xlabel('Индекс времени')
            plt.ylabel('Курс валюты')
            plt.title(f'График курса {currency}')
            line1.set_xdata(timeline)
            line1.set_ydata(values)
            plt.clf()
            plt.show()
            #plt.plot(timeline, values, marker='o', linestyle='-', color='b')

            # Отображаем обновленный график
            plt.pause(1)

    except Exception as e:
            print(f"Error: {e}")

'''fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Индекс')
ax.set_ylabel('Время (секунды)')
ax.set_zlabel('Курс')
'''
'''# Устанавливаем начальное значение оси Z
max_value = 110  # Это значение зависит от ваших ожиданий
ax.set_zlim(0, max_value)
'''

def pars_history_tabel(choice, currency):
    '''  form = soup.find('form', id='widgetFieldDateRange')
            form_data = {
                'pair_base': '1',
                'pair_quote': '18',
                'smlID': '300004',
                'st_date': '01/01/2023',
                'end_date': '12/31/2023',
                'interval_sec': 'Daily',
                'action': 'historical_data',
            }
            response.request.post(choice, data=form_data, headers=headers)
            if response.status_code == 200:'''
    dict_history = {'Date':[],'Price':[], 'Percentage':[]}
    try:
        response = requests.get(choice, headers=headers)
        if response.status_code == 200:
            soup = BS(response.text, 'html.parser')
            table = soup.find('table', class_=['datatable_table__DE_1_ datatable_table--border__XOKr2 datatable_table--mobile-basic__rzXxT datatable_table--freeze-column__XKTDf','w-full text-xs leading-4 overflow-x-auto freeze-column-w-1'])
            if table:
                rows = table.find_all('tr')
                for row in rows[1:]:
                    columns = row.find_all('td')
                    date = columns[0].text.strip()
                    cost = columns[1].text.strip()
                    percent = columns[6].text.strip()
                    dict_history['Date'].append(date)
                    dict_history['Price'].append(cost)
                    dict_history['Percentage'].append(percent)
            print_dict_as_columns(dict_history)
            plt.figure(figsize=(20, 12))
            plt.plot(dict_history['Date'], dict_history['Price'], marker='o', linestyle='-', color='b')
            plt.title(f'График курса {currency}')
            plt.xlabel('Дата')
            plt.ylabel('Цена')
            plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
            plt.tight_layout()
            plt.gca().invert_yaxis()
            plt.gca().invert_xaxis()
            plt.show()

    except Exception as e:
        print(f"Error: {e}")
    return dict_history



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
                dict_curr['Currency'].append(name)
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
    #print_dict_as_columns(result)
    select = select_filter(result)
    data = select_from_url(select[0],select[1])
    print(data)
    data_for_choice = data.get('Link')
    currency = data.get('Currency')
    print(data_for_choice)
    choice = (choice_time(data_for_choice, currency))
    #print(choice)


if __name__ == '__main__':
    main()