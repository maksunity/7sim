import requests
from bs4 import BeautifulSoup
from queue import Queue
import re

def get_links_with_keyword(url, keyword):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links on the page
        links = soup.find_all('a', href=True)

        # Filter links that mention the keyword
        relevant_links = [link['href'] for link in links if keyword in link['href'].lower()]

        return relevant_links

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def get_and_save_cat_image_links(url, keyword):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        image_tags = soup.find_all('img', src=re.compile(r'(cat|kitty)'))

        with open('cat_photos.txt', 'a') as file:
            for img_tag in image_tags:
                img_url = img_tag.get('src')
                if img_url:
                    file.write(img_url + '\n')

    except requests.exceptions.RequestException as e:
        print("Error:", e)

def crawl_and_search(seed_url, keyword):
    visited = set()
    queue = Queue()

    queue.put(seed_url)

    while not queue.empty():
        current_url = queue.get()

        if current_url in visited:
            continue

        visited.add(current_url)
        relevant_links = get_links_with_keyword(current_url, keyword)

        for link in relevant_links:
            print("Found relevant link:", link)
            queue.put(link)

        get_and_save_cat_image_links(current_url, keyword)

def main():
    seed_url = input('Enter the seed URL: ')
    keyword = input('Enter the keyword to search for (e.g., cat, cats, kitty): ').lower()

    open('cat_photos.txt', 'w').close()

    crawl_and_search(seed_url, keyword)
    print("Cat-related image links saved to 'cat_photos.txt'.")

if __name__ == '__main__':
    main()
