from models.db_async import async_session
from models import User, Post


async def insert_users(name: str, username: str, email: str) -> None:
    """Создает сессию и сохраняет изменения в таблицу users"""
    async with async_session() as session:
        async with session.begin():
            new_user = User(name=name, username=username, email=email)
            session.add(new_user)
        await session.commit()


async def insert_posts(user_id: int, title: str, body: str) -> None:
    """Создает сессию и сохраняет изменения в таблицу posts"""
    async with async_session() as session:
        async with session.begin():
            new_post = Post(user_id=user_id, title=title, body=body)
            session.add(new_post)
        await session.commit()
