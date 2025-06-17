from pydantic import BaseModel

class Address(BaseModel):
    street: str
    state: str
    country: str