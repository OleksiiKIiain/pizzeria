from sqlalchemy.orm import Session

from pizzeria.Entities.error import ErrorResult
from pizzeria.schemas.pizzeria import PizzeriaCreate, PizzeriaSchema
from pizzeria.Repositories.PizzeriaRepository import PizzeriaRepository

class PizzeriaService:
    def __init__(self, db: Session):
        self.pizzeria_repository = PizzeriaRepository(db)

    def create_pizzeria(self, pizzeria: PizzeriaCreate):
        return self.pizzeria_repository.create(pizzeria)

    def get_all_pizzerias(self) :
        pizzerias= self.pizzeria_repository.get_all()
        if pizzerias:
            return pizzerias
        else :
            return ErrorResult(message="List is empty")

    def get_pizzeria(self, pizzeria_id: int):
        pizzeria= self.pizzeria_repository.get(pizzeria_id)
        if pizzeria:
            return pizzeria
        else :
            return ErrorResult(message=f"Pizzeria with id= {pizzeria_id} not found")

    def update_pizzeria(self, pizzeria_id: int, pizzeria: PizzeriaCreate):
        pizzeria= self.pizzeria_repository.update(pizzeria_id, pizzeria)
        if pizzeria:
            return {"detail":f"Pizzeria is update successfully"}
        else :
            return ErrorResult(message = f"Update pizzeria failed , not found pizzeria by id")

    def delete_pizzeria(self, pizzeria_id: int) :
        pizzeria= self.pizzeria_repository.delete(pizzeria_id)
        if pizzeria:
            return {"detail" : f"Pizzeria with {id} has been deleted"}
        else :
            return ErrorResult(message="Pizzeria not found")
