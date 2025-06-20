from fastapi import Depends, status
from fastapi.exceptions import HTTPException

from beanie.odm.operators.find.evaluation import RegEx

from pymongo.errors import DuplicateKeyError

from api.models.client import Client
from api.models.address import Address
from api.models.product import Product
from api.dto.product_dto import ProductDto

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
    regex = f".*{name}.*"
    clients = await Client.find(
        RegEx(Client.name, pattern=name, options="i")
    ).to_list()
    if not clients:
        return {"message": "Nenhum usuário encontrado..."}
    return clients

async def get_product_by_id(username: str, code: str):
    client = await Client.find_one(
        Client.name == username)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não foi possível encontrar usuário.",
        )
    for product in client.products:
        if str(product.code) == code:
            return product
    return {"message": "Produto não encontrado."}

async def add_product_to_user(product: ProductDto, username: str):
    client = await Client.find_one(Client.name == username)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não foi possível encontrar usuário.",
        )
    new_product = Product(
        name=product.name,
        price=product.price
    )
    client.products.append(new_product)
    await client.save()
    return {"message": "Produto adicionado!"}

async def get_all_user_products(username):
    client = await Client.find_one(Client.name == username)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não foi possível encontrar usuário.",
        )
    return client.products