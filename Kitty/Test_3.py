import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

cat_keywords = ['cat', 'kitten', 'feline', 'kitty', 'domestic cat', 'wildcat', 'big_cat', 'lion', 'tiger', 'leopard']

def is_cat_related_image(img):
    alt_text = img.get('alt', '').lower()
    title_text = img.get('title', '').lower()
    for keyword in cat_keywords:
        if keyword in alt_text or keyword in title_text:
            return True
    return False

# Function to download an image
def download_image(url, folder_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_name = os.path.join(folder_path, url.split("/")[-1])
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download: {url}")
    except Exception as e:
        print(f"Error downloading image: {e}")


# Function to scrape links from a Wikipedia article
def scrape_links_from_wikipedia(url):
    links = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and href.startswith('/wiki/') and ':' not in href:
                    links.append(urljoin("https://en.wikipedia.org", href))
        else:
            print(f"Failed to scrape links from: {url}")
    except Exception as e:
        print(f"Error scraping links: {e}")
    return links

def is_cat_related_url(href):
    for keyword in cat_keywords:
        if keyword.replace(" ", "_") in href:
            return True
    return False

# Main function to start the process
def main():
    start_url = "https://en.wikipedia.org/wiki/Cat"
    max_images = int(input("Enter the number of pictures to download: "))
    links_to_visit = [start_url]
    visited_links = set()
    downloaded_images = 0
    image_folder = "cat_images"

    # Create a folder to store the downloaded images
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    while downloaded_images < max_images and links_to_visit:
        current_url = links_to_visit.pop(0)
        if current_url in visited_links:
            continue
        visited_links.add(current_url)

        print(f"Visiting: {current_url}")

        # Scrape links from the current page
        links = scrape_links_from_wikipedia(current_url)
        links_to_visit.extend(links)

        # Find and download images from the current page
        try:
            response = requests.get(current_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                images = soup.find_all('img')
                for img in images:
                    if is_cat_related_image(img):
                        img_url = urljoin(current_url, img.get('src'))
                        download_image(img_url, image_folder)
                        downloaded_images += 1
                        if downloaded_images >= max_images:
                            break
            else:
                print(f"Failed to fetch images from: {current_url}")
        except Exception as e:
            print(f"Error fetching images: {e}")


if __name__ == "__main__":
    main()
