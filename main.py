import asyncio
import logging

from logger import configure_logging
from jsonplaceholder_requests import get_users, get_posts
from work_to_db import insert_users, insert_posts

log = logging.getLogger(__name__)


async def get_data_http() -> tuple:
    """
    Создает задание на получение данных по http
    и возвращает результат
    """

    log.info("Start main")

    # Создает группу заданий и выполняет ее
    async with asyncio.TaskGroup() as tg:
        task_users_get_data = tg.create_task(get_users())
        task_posts_get_data = tg.create_task(get_posts())

    # получает значение, которое возвращает функция
    users = task_users_get_data.result()
    posts = task_posts_get_data.result()

    return users, posts


async def push_data_to_db() -> None:
    data_user = await get_data_http()  # Получает результат из асинхронной функции get_data_http()

    task_users_push_db = [insert_users(user['name'], user['username'], user['email']) for user in data_user[0]]
    task_posts_push_db = [insert_posts(user['userId'], user['title'], user['body']) for user in data_user[1]]

    # Из за ограничения целостности приходится заполнять таблицы друг за другом
    # т.к. если их объеденить в единое: await asyncio.gather(*task_users_push_db, *task_posts_push_db)
    # то падает в ошибку, т.к. таблица posts ссылается на таблицу users
    # "user_id" таблицы posts это ForeignKey "id" таблицы users
    # т.е происходит попытка вставить строку с user_id, а в таблице users такого id еще нет.
    log.info("Start Uploading information to a table - users")
    await asyncio.gather(*task_users_push_db)
    log.info("End Uploading information to a table - users")

    log.info("Start Uploading information to a table - posts")
    await asyncio.gather(*task_posts_push_db)
    log.info("End Uploading information to a table - posts")

    log.info("Finish main")


def main() -> None:
    configure_logging()
    asyncio.run(push_data_to_db())


if __name__ == "__main__":
    main()
