from pydantic import BaseModel, ConfigDict 

class SBookAdd(BaseModel):
    title: str
    author: str
    year: int
    pages: int
    is_read: bool = False

class SBook(SBookAdd):
    model_config = ConfigDict(from_attributes=True)
    id: int
