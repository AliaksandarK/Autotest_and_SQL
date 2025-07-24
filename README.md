## Тест создаёт новый заказ через POST, а затем получает его по трек-номеру через GET. Всё запускается с помощью Pytest.

## Установка и запуск

1. Установите Python (если не установлен).
2. Перейдите в папку с проектом (в терминале VSCode):
```bash
cd путь_к_папке_проекта
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Запустите автотест через Pytest:
```bash
pytest -v
```
5. При успешном выполнении увидите `1 passed`:
```text
test_track_order_information.py::test_get_order_by_track PASSED
```
6. Если тест не прошёл, будет подробный вывод причины и ответов API.

## Файлы
- configuration.py — настройки соединения
- data.py — данные запроса
- sender_stand_request.py — функции отправки запросов
- test_track_order_information.py — сам тест