# Файл с функциями для отправки запросов к API
# create_order(): создаёт заказ
# get_order_by_track(track): получает заказ по номеру трека

import requests
from configuration import BASE_URL, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH
from data import CREATE_ORDER_HEADERS, CREATE_ORDER_PAYLOAD

def create_order():
    
                                          # Отправляет POST-запрос на создание заказа.
                                          # Возвращает объект ответа (response).
    
    url = BASE_URL + CREATE_ORDER_PATH    # Полный URL для создания заказа
    response = requests.post(
        url,
        json=CREATE_ORDER_PAYLOAD,
        headers=CREATE_ORDER_HEADERS
    )
    print(f'Create order: статус {response.status_code}, тело: {response.text}')
    return response

def get_order_by_track(track):
    
                                            # Отправляет GET-запрос для получения заказа по номеру трека.
                                            # Возвращает объект ответа (response).
    
    url = BASE_URL + GET_ORDER_BY_TRACK_PATH  # Полный URL для получения заказа по треку
    params = {'t': track}                     # Параметр для запроса: номер трека заказа
    response = requests.get(url, params=params)
    print(f'Get order by track: статус {response.status_code}, тело: {response.text}')
    return response