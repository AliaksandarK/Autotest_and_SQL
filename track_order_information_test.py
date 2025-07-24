# Кухаренко Александр, 32-я когорта- Финальный проект. Инженер по тестированию плюс.

#Файл с автотестом проверки получения заказа по треку:

#1. Создать заказ
#2. Сохранить трек заказа
#3. Получить заказ по треку
#4. Проверить успешный статус ответа


from sender_stand_request import create_order, get_order_by_track

def test_get_order_by_track():
                               # Шаг 1: создание заказа
    create_order_response = create_order()
    assert create_order_response.status_code == 201, "Заказ не был создан! Проверьте данные запроса."
                               # Получаем "вытаскиваем" track из ответа сервера
    track = create_order_response.json().get('track')
    assert track, "В ответе нет значения 'track'!"
    
                                # Шаг 2: получение заказа по треку
    get_order_response = get_order_by_track(track)
    assert get_order_response.status_code == 200, f"Заказ по треку {track} не найден!"
    print('Тест успешно пройден!')

if __name__ == '__main__':
    test_get_order_by_track()    # Запуска теста при запуске файла напрямую