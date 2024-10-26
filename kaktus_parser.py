import json
from bs4 import BeautifulSoup

# Пример HTML-кода, который вы могли бы получить с веб-страницы
html = """
<div class="BannerA--parent">
    <div class="BannerA--content">
        <div class="bnr bnr-a bnr-id-1">
            <div class="bnr-type-banner">
                <div class="bnr-type-banner-content" style="background-image: url('https://example.com/image1.jpg');"></div>
                <a class="bnr-type-banner-link" href="https://example.com/link1">Ссылка 1</a>
            </div>
        </div>
        <div class="bnr bnr-a bnr-id-2">
            <div class="bnr-type-banner">
                <div class="bnr-type-banner-content" style="background-image: url('https://example.com/image2.jpg');"></div>
                <a class="bnr-type-banner-link" href="https://example.com/link2">Ссылка 2</a>
            </div>
        </div>
        <div class="bnr bnr-a bnr-id-3">
            <div class="bnr-type-banner">
                <div class="bnr-type-banner-content" style="background-image: url('https://example.com/image3.jpg');"></div>
                <a class="bnr-type-banner-link" href="https://example.com/link3">Ссылка 3</a>
            </div>
        </div>
    </div>
</div>
"""

def parse_banners(html):
    """Парсим HTML и извлекаем ссылки и изображения баннеров."""
    soup = BeautifulSoup(html, 'html.parser')
    banners = soup.find_all('div', class_='bnr-type-banner')
    
    banner_list = []

    for banner in banners:
        image_style = banner.find('div', class_='bnr-type-banner-content')['style']
        image_url = image_style.split("url('")[1].split("')")[0] if "url('" in image_style else None
        link = banner.find('a', class_='bnr-type-banner-link')['href']

        if image_url and link:
            banner_list.append({
                "image_url": image_url,
                "link": link
            })

    return banner_list

def save_to_json(data, filename):
    """Сохраняем данные в формате JSON."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    banners = parse_banners(html)  # Парсим HTML
    save_to_json(banners, "banners.json")  # Сохраняем данные в JSON-файл
    print(f"Данные успешно сохранены в файл banners.json")

if __name__ == "__main__":
    main()
