'''
Написать программу, которая найдет в вики все фото котиков.
Пояснение. Для выполнения вам необходимо разобратьс библиотеками requests, BeautifulSoup,
узнать что такое дом сайта и и научиться загружать и обрабатывать сайты
'''

import requests
import re
import json
from bs4 import BeautifulSoup

#payloads = {'cat': ['cat', 'cats', 'kitty']}

def get_link():
    link = input('Put here your link web-site: ')
    return link

def get_cat(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all('a', href=True)
        animal_image_links = []
        for link in links:
            href = link.get('href')
            if href and re.search(r'(cat|cats|kitty)', href, re.I):
                # Check if the link contains "cat," "cats," or "kitty" (case-insensitive)
                full_link = link + href if not href.startswith('http') else href
                animal_image_links.append(full_link)

        with open('Cat.txt', 'w') as file:
            for link in animal_image_links:
                response = requests.get(link)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')

                image_tags = soup.find_all('img', src=re.compile(r'(cat|cats|kitty)'))
                for img_tag in image_tags:
                    img_url = img_tag.get('src')
                    if img_url:
                        file.write(img_url + '\n')

    except requests.exceptions.RequestException as e:
        print("Error:", e)

def main():
    link = 'https://en.wikipedia.org/wiki/Cat'
    #link = get_link()
    get_cat(link)


    '''with open('Cat.txt', 'w') as file:
        file.write(result.text)'''

'''if __name__ == '__main__':
    main()'''




