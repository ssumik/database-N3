from api.dto.client_dto import ClientDto
from api.services import clients

from beanie.exceptions import DocumentNotFound

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

router = APIRouter()

@router.get("/clients/search_product/{product}")
async def all_clients(product):
    return await clients.get_client_product(product)

@router.get("/clients/search_street/{street}")
async def all_clients(street):
    return await clients.get_clients_street(street)

@router.get("/clients/search/{name}")
async def all_clients(name):
    return await clients.get_clients_list(name)

@router.post("/clients/create")
async def create_client(
    client_dto: ClientDto
):
    return await clients.create_client(client_dto)

