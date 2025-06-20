from beanie import Document, Indexed

from pydantic import Field

from uuid import uuid4, UUID

from api.models.product import Product
from api.models.address import Address

# Modelo de usuário de exemplo
class Client(Document):
    id: UUID = Field(default_factory=uuid4)
    name: Indexed(str, unique=True)
    products: list[Product]
    address: Address
    
    class Settings:
        name = "clients"