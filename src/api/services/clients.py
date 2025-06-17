from fastapi import Depends

from pymongo.errors import DuplicateKeyError

from api.models.client import Client
from api.models.address import Address
""" from api.models.product import Product """

async def create_client(client_dto):
    client_address = Address(
        street=client_dto.address.street,
        state=client_dto.address.state,
        country=client_dto.address.country
    )
    new_client = Client(
        name=client_dto.name,
        address=client_dto.address,
        products=[]
    )
    
    await new_client.insert()

async def get_clients_list(name: str):
    pass