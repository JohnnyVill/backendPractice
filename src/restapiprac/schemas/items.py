from pydantic import BaseModel, PositiveInt

class CreateItem(BaseModel):
    id: int
    category: str
    size: PositiveInt

class ItemResponse(BaseModel):
    id: int
    category: str
    size: PositiveInt