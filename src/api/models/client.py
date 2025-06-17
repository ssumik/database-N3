from beanie import Document, Indexed

from pydantic import Field

from uuid import uuid4, UUID

# Modelo de usuário de exemplo
class Client(Document):
    id: UUID = Field(default_factory=uuid4)
    name: Indexed(str, unique=True)
    produts: str
    address: str