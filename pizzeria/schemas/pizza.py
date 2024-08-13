from pydantic import BaseModel, Field

class PizzaBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, strip_whitespace=True)
    price: float = Field(..., gt=0)

class PizzaCreate(PizzaBase):
    category_id: int = Field(..., gt=0)

class PizzaSchema(PizzaBase):
    id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
