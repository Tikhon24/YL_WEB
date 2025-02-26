import requests

server_address = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
cities = ['Барнаул', 'Мелеуз', 'Йошкар-Ола']

for city in cities:
    geocode = city
    # Готовим запрос.
    geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode}&format=json'
    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][1]["GeoObject"]
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"]
        # Печатаем извлечённые из ответа поля:
        print(f'{city} - {toponym_address}')
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
