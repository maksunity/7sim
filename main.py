import requests
import os
import re
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin
import time


def get_link():
    link = 'https://en.wikipedia.org/wiki/List_of_cat_breeds'
    return link


def block_list(url):
    excluded_parts = ['Flag_of', 'Flag_of_the, ']
    pattern = re.compile(fr"({'|'.join(excluded_parts)})")

    invalid_keywords = ['wikipedia-wordmark-en.svg',
                        'wikipedia-tagline-en.svg',
                        'wikipedia.png',
                        'wikimedia-button.png',
                        'poweredby_mediawiki_88x31.png',
                        '40px-Ambox_important.svg.png',
                        '30px-Commons-logo.svg.png',
                        '20px-Wiki_letter_w_cropped.svg.png',
                        '23px-Flag_of_the_United_States.svg.png',
                        '16px-Symbol_category_class.svg.png',
                        '10px-OOjs_UI_icon_edit-ltr-progressive.svg.png',
                        '23px-Flag_of_Greece.svg.png',
                        '50px-Question_book-new.svg.png',
                        '40px-Wiktionary-logo-en-v2.svg.png',
                        '36px-Merge-split-transwiki_default.svg.png',
                        '12px-Commons-logo.svg.png',
                        '45px-Unbalanced_scales.svg.png',
                        '19px-Symbol_support_vote.svg.png',
                        '16px-Wiktionary-logo-en-v2.svg.png',
                        '40px-Edit-clear.svg.png',
                        '40px-Crystal_Clear_app_kedit.svg.png',
                        '40px-Text_document_with_red_question_mark.svg.png',
                        '40px-Wiki_letter_w.svg.png',
                        '42px-Ambox_current_red_Americas.svg.png']

    if pattern.search(url):
        return False

    for keyword in invalid_keywords:
        if keyword in url:
            return False

    return True


def is_desired_th(tag):
    return tag.name == 'th' and tag.get('scope') == 'row' and 'class' not in tag.attrs


def get_cat_link(link):
    links = []
    try:
        response = requests.get(link)
        if response.status_code == 200:
            soup = BS(response.text, 'html.parser')
            for link in soup.find_all(is_desired_th):
                a_tag = link.find('a')
                if a_tag:
                    link = a_tag.get('href')
                    total_link = "https://en.wikipedia.org" + link
                    if total_link and block_list(total_link):
                        links.append(total_link)
            return links
        else:
            print(f"Failed to scrape links from: {link}")
    except Exception as e:
        print(f"Error scraping links: {e}")
    return links


def download_image(url, folder_path):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        print(response)
        if response.status_code == 200:
            file_name = os.path.join(folder_path, url.split("/")[-1])
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download: {url}")
    except Exception as e:
        print(f"Error downloading image: {e}")


def main():
    link = get_link()
    links = get_cat_link(link)
    max_images = int(input("Enter the number of pictures to download: "))
    links_to_visit = links[:max_images]  # Ограничиваем список ссылок
    visited_links = set()
    downloaded_images = 0
    image_folder = "cat_images"

    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    while downloaded_images < max_images and links_to_visit:
        current_url = links_to_visit.pop(0)
        if current_url in visited_links:
            continue
        visited_links.add(current_url)
        print(f"Visiting: {current_url}")

        try:
            response = requests.get(current_url)
            if response.status_code == 200:
                soup = BS(response.text, 'html.parser')
                images = soup.find_all('img')
                for img in images:
                    img_url = urljoin(current_url, img.get('src'))
                    if block_list(img_url):
                        print(img_url)
                        download_image(img_url, image_folder)
                        downloaded_images += 1
                        if downloaded_images >= max_images:
                            break
            else:
                print(f"Failed to fetch images from: {current_url}")
        except Exception as e:
            print(f"Error fetching images: {e}")
        #time.sleep(100)


if __name__ == '__main__':
    main()
