from sqlalchemy.orm import Session

from pizzeria.Entities.error import ErrorResult
from pizzeria.schemas.pizza import PizzaCreate,PizzaSchema
from pizzeria.Repositories.PizzaRepository import PizzaRepository

class PizzaService:
    def __init__(self, db: Session):
        self.pizza_repository = PizzaRepository(db)

    def create_pizza(self, pizza: PizzaCreate) :
        return self.pizza_repository.create(pizza)

    def get_all_pizzas(self) :
        pizzas =  self.pizza_repository.get_all()
        if pizzas:
            return pizzas
        else:
            return ErrorResult(message = "List of pizzas is empty")

    def get_pizza(self, pizza_id: int) :
        pizza = self.pizza_repository.get_by_id(pizza_id)
        if pizza:
            return pizza
        else:
            return ErrorResult(message =f"Pizza with id = {pizza_id} not found")

    def update_pizza(self, pizza_id: int, pizza: PizzaCreate):
        update_pizza = self.pizza_repository.update(pizza_id, pizza)

        if update_pizza:
            return {"detail": f"Pizza is update successfully"}
        else:
            return ErrorResult(message=f"Update pizza failed")

    def delete_pizza(self, pizza_id: int) :
        pizza= self.pizza_repository.delete(pizza_id)
        if pizza:
            return {"detail": f"Pizza with {pizza_id} has been deleted"}
        else:
            return ErrorResult(message="Pizza not found")
