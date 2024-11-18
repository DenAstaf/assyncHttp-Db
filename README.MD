В данном процессе реализована работа с сетью и БД в асинхронном виде.

* Используется СУБД Postgre.
* Полученные данные хранятся в таблицах: "users" и "posts". Между таблицами настроено отношение "один ко многим", где один пользователь может быть связан с несколькими постами, но каждый пост может ссылаться только на одного пользователя.
<br>Пример запроса, который вернет пользователей и все их посты:
<br>`SELECT u.id AS user_id, u.name, p.id AS post_id, p.title, p.body` 
<br>`FROM users u`
<br>`INNER JOIN posts p ON u.id = p.user_id`
<br>`order by u.id desc`
<br>Пример запроса, который покажет количество постов каждого пользователя:
<br>`SELECT u.id AS user_id, u.name, COUNT(p.user_id) AS post_count`
<br>`FROM users u`
<br>`JOIN posts p ON u.id = p.user_id`
<br>`GROUP BY u.id`
<br>`order by u.id desc`
* Используется Alembic для работы с миграциями в асинхронном режиме (
для этого он был инициализирован в асинхронном виде: alembic init -t async alembic).
* Вместо requirements.txt используется Poetry.

Для начала работы необходимо:

1. Установить Poetry: pip install poetry
2. Выполнить команду, чтобы установить нужные зависимости: poetry install
3. Выполните команду, чтобы запустить докер: docker compose up -d