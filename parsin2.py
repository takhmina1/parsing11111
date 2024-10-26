import requests
from bs4 import BeautifulSoup

def get_html(url):
    # Отправляем GET-запрос и получаем HTML-страницу
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Не удалось получить страницу", response.status_code)
        return None

def parse_html(html):
    # Создаём объект BeautifulSoup для работы с HTML
    soup = BeautifulSoup(html, 'html.parser')
    # Находим все заголовки статей. На сайте Real Python заголовки имеют тег h2 и класс card-title
    articles = soup.find_all('h2', class_='card-title')
    
    # Выводим каждый заголовок статьи
    for article in articles:
        print(article.text.strip())  # выводим текст заголовка, убирая лишние пробелы

def main():
    url = 'https://realpython.com/'  
   
    html = get_html(url)
    if html:
        parse_html(html)

if __name__ == "__main__":
    main()
