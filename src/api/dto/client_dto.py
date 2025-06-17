from pydantic import BaseModel
from uuid import UUID

from api.models.product import Product
from api.models.address import Address

from typing import Optional

class ClientDto(BaseModel):
    id: UUID
    name: str
    products: Optional[Product] = []
    address: Address