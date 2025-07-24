markdown
#  Задача 1:
#  Представь чтсо тебе нужно проверить, отображается ли созданный заказ в базе данных.
#  Для этого: выведи список логинов курьеров с количеством их заказов в статусе "В доставке" (поле inDelivery=true)
#  Подключение по SSH

```bash
ssh bf006cc7-29d7-4cac-af27-f093e0da04fb@serverhub.praktikum-services.ru -p 4554
Результат:

bash
morty@e3ae0af8c430:~$
Публичный SSH-ключ
bash
cat ~/.ssh/id_rsa.pub
Результат:

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC6EzHN... (ключ обрезан для краткости)
Саша@DESKTOP-G3B38JM
Подключение к базе данных
bash
psql -U morty -d scooter_rent
Первая попытка:

Password for user morty:
FATAL: password authentication failed for user "morty"
Вторая попытка:

psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.
Попытка выполнить SQL-запрос
Первый запрос (ошибка):
sql
SELECT couriers.login, COUNT(orders.id) AS delivery_count
FROM orders
JOIN couriers ON orders.courier_id = couriers.id
WHERE orders."inDelivery" = true
GROUP BY couriers.login;
Ошибка:

ERROR: relation "orders" does not exist
Список таблиц:
sql
\dt
Результат:

 Schema |     Name      | Type  | Owner
--------+---------------+-------+-------
 public | Couriers      | table | root
 public | Orders        | table | root
 public | SequelizeMeta | table | root
(3 rows)
Уточнённый запрос c кавычками и правильными именами столбцов:
sql
SELECT "Couriers".login, COUNT("Orders".id) AS delivery_count
FROM "Orders"
JOIN "Couriers" ON "Orders"."courierId" = "Couriers".id
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers".login;
Первый результат:

(0 rows)
Повторный запрос (после появления заказов):

 login | delivery_count
-------+----------------
 ninja |              2
(1 row)
Завершение сессии
Read from remote host serverhub.praktikum-services.ru: Connection reset by peer
Connection to serverhub.praktikum-services.ru closed.
client_loop: send disconnect: Connection reset by peer
🗃️ Стенд и API
Стенд веб-приложения: https://4baa1996-eb9f-4155-85b1-9a9827a82664.serverhub.praktikum-services.ru/

Документация API: https://4baa1996-eb9f-4155-85b1-9a9827a82664.serverhub.praktikum-services.ru/docs/

Вывод
Я успешно:

Подключился к серверу по SSH и к базе PostgreSQL.

Проверил структуру таблиц.

Выполнил SQL-запрос на количество заказов в доставке.

Обработал ошибки и исправил SQL-синтаксис.

Получил ожидаемый результат.