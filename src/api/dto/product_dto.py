from pydantic import BaseModel

class ProductDto(BaseModel):
    name: str
    price: int