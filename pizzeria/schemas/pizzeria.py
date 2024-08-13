from typing import List
from pydantic import BaseModel, Field

class PizzeriaBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, strip_whitespace=True)
    location: str = Field(..., min_length=5, max_length=200, strip_whitespace=True)

class PizzeriaCreate(PizzeriaBase):
    pass

class PizzeriaSchema(PizzeriaBase):
    id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
