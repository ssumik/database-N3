from pydantic import BaseModel

from uuid import UUID

from typing import Optional

class ProductDto(BaseModel):
    code : Optional[UUID] = UUID
    name: str
    price: int