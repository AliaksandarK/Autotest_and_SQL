# Файл для хранения заголовков и тела запроса на создание заказ

# Заголовки HTTP-запроса
CREATE_ORDER_HEADERS = {
    'Content-Type': 'application/json'
}

# Тело POST-запроса на создание заказа
CREATE_ORDER_PAYLOAD = {
    "firstName": "Aliaksandar",
    "lastName": "Kukharenko",
    "address": "Domash 25",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 4,
    "deliveryDate": "2025-07-25",
    "comment": "Ne zvonit",
    "color": ["BLACK"]
}