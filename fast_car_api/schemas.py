from typing import Optional
from pydantic import BaseModel


class CarSchema(BaseModel):
    brand: str
    model: str
    color: Optional[str]
    factory_year: Optional[int]
    model_year: Optional[int]
    description: Optional[str]
