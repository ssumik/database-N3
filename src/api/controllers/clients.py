from api.dto.client_dto import ClientDto
from api.services import clients

from beanie.exceptions import DocumentNotFound

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

router = APIRouter()

@router.get("/clients")
async def all_clients(name):
    return await clients.get_clients_list(name)

@router.post("/clients/create")
async def create_clients(
    client_dto: ClientDto
):
    return await clients.create_client(client_dto)
