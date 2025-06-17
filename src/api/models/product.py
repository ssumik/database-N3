from pydantic import BaseModel

from pydantic import Field

from uuid import uuid4, UUID

class Product(BaseModel):
    code: UUID = Field(default_factory=uuid4)
    name: str
    price: int