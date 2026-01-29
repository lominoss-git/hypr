import os, re
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib.parse, urllib.request


def parse_container(container):
    a = container.find("a")
    url = urllib.parse.urljoin(BASE_URL, a.get("href"))

    h2 = container.find("h2")
    name = h2.text

    return {
        "url": url,
        "name": name,
    }


def slugify_name(name):
    if not name:
        return "product"

    slug = name.strip().lower()
    slug = re.sub(r"\s+", " ", slug)
    slug = slug.replace(" ", "-")
    slug = re.sub(r"-+", "-", slug)

    return slug


def get_extension(url):
    parsed = urllib.parse.urlparse(url)
    root, ext = os.path.splitext(parsed.path)

    return ext


def download_image(url, output_path):
    if not url or not url.startswith("https://"):
        return False

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(output_path, "wb") as out_file:
                out_file.write(response.read())

        return True

    except Exception as e:
        print(f"Warning: Failed to download {url} ({e})")
        return False


BASE_URL = "https://www.uriage.fr"
MAIN_URL = urllib.parse.urljoin(BASE_URL, "/gammes")

html = requests.get(MAIN_URL)
soup = BeautifulSoup(html.text, "html.parser")

category_containers = soup.find_all("div", class_="product-container")

categories = []
for container in category_containers[2:]:
    categories.append(parse_container(container))

for category in categories:
    category_html = requests.get(category["url"])
    category_soup = BeautifulSoup(category_html.text, "html.parser")

    product_containers = category_soup.find_all("div", class_="product-container")
    
    products = []
    for container in product_containers:
        products.append(parse_container(container))

    for product in products:
        product_html = requests.get(product["url"])
        product_soup = BeautifulSoup(product_html.text, "html.parser")
        
        image_dir = f'Products/{category["name"]}/{product["name"]}'
        Path(image_dir).mkdir(parents=True, exist_ok=True)

        slider_container = product_soup.find("div", class_="slider--product")
        image_containers = slider_container.find_all("div", class_="slider__slide-image")
        
        for idx, container in enumerate(image_containers, start=1):
            img = container.find("img")
            url = img.get("src")

            ext = get_extension(url)
            filename = f'{slugify_name(product["name"])}_{idx}{ext}'
            output_path = os.path.join(image_dir, filename)

            if download_image(url, output_path):
                print(f"Downloaded: {filename}")
