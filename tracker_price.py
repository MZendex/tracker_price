import requests
from bs4 import BeautifulSoup

def track_price(url):
    # Отправляем GET-запрос на сайт
    response = requests.get(url)

    # Проверяем, что запрос успешен
    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML-страницы
        soup = BeautifulSoup(response.content, 'html.parser')

        # Найдите элемент, содержащий цену на странице (используйте инструменты разработчика вашего браузера для определения соответствующего селектора)
        price_element = soup.find('span', class_='price')

        # Получаем текст цены
        price = price_element.text.strip()

        # Выводим цену
        print(f"Current price: {price}")
    else:
        print("Failed to retrieve data from the website.")

# Пример использования
url = "https://www.example.com/product"  # Замените на URL конкретного продукта
track_price(url)
