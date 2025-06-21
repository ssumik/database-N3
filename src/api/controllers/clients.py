from api.dto.client_dto import ClientDto
from api.dto.product_dto import ProductDto
from api.services import clients

from beanie.exceptions import DocumentNotFound

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

router = APIRouter()

@router.get("/clients/{username}/search_product/{code}")
async def all_clients(username, code):
    return await clients.get_product_by_id(
        username=username,
        code=code    
    )

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

@router.post("/clients/{username}/products/add")
async def add_product(product: ProductDto, username: str):
    return await clients.add_product_to_user(
        product=product, 
        username=username
    )
    
@router.get("/clients/{username}/products")
async def get_all_user_products(username: str):
    return await clients.get_all_user_products(username)