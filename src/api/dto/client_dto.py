from pydantic import BaseModel
from uuid import UUID

class ClientDto(BaseModel):
    id: UUID
    name: str
    produts: str
    address: str