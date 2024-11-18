__all__ = (
    "get_users",
    "get_posts",
)

import aiohttp
import logging


log = logging.getLogger(__name__)


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:
            return await response.json()


async def fetch_posts() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as response:
            return await response.json()


async def get_users() -> dict:
    log.info("Start getting information users")
    users = await fetch_users()
    log.info("Got information users")
    return users


async def get_posts() -> dict:
    log.info("Start getting information posts")
    posts = await fetch_posts()
    log.info("Got information posts")
    return posts
