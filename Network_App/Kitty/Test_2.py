import requests
from bs4 import BeautifulSoup
import re
from queue import Queue

def get_and_save_image_links(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        image_tags = soup.find_all('img', src=re.compile(r'(cat|kitty)'))

        with open(output_file, 'a') as file:
            for img_tag in image_tags:
                img_url = img_tag.get('src')
                if img_url:
                    if not img_url.startswith('http'):
                        img_url = url + img_url
                    file.write(img_url + '\n')

    except requests.exceptions.RequestException as e:
        print("Error:", e)

def crawl_and_search(seed_url, keyword, max_depth, output_file):
    visited = set()
    queue = Queue()
    depth_map = {}  # Keep track of the depth of each URL

    queue.put((seed_url, 0))

    while not queue.empty():
        current_url, current_depth = queue.get()

        if current_url in visited or current_depth > max_depth:
            continue

        visited.add(current_url)

        relevant_links = get_links_with_keyword(current_url, keyword)

        for link in relevant_links:
            print("Found relevant link:", link)
            queue.put((link, current_depth + 1))

        get_and_save_image_links(current_url, output_file)

def get_links_with_keyword(url, keyword):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all('a', href=True)

        relevant_links = [link['href'] for link in links if keyword in link['href'].lower()]

        return relevant_links

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def main():
    seed_url = input('Enter the seed URL: ')
    keyword = input('Enter the keyword to search for (e.g., cat, cats, kitty): ').lower()
    max_depth = int(input('Enter the maximum depth for traversal: '))
    output_file = 'cats.txt'

    # Clear the contents of the output file before starting
    open(output_file, 'w').close()

    crawl_and_search(seed_url, keyword, max_depth, output_file)
    print(f"Image links related to '{keyword}' saved to '{output_file}'.")

if __name__ == '__main__':
    main()
