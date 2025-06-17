from fastapi import Depends

from pymongo.errors import DuplicateKeyError

from typing_extensions import Annotated

from api.models.client import Client

async def get_clients_list(name: str):
    async for result in Client.find():
        if result="" return
        set clients