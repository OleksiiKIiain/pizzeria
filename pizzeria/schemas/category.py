from typing import List
from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, strip_whitespace=True)

class CategoryCreate(CategoryBase):
    pizzeria_id: int = Field(..., gt=0)  # greater than 0

class CategorySchema(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=100, strip_whitespace=True)

    class Config:
        orm_mode = True
        validate_assignment = True
