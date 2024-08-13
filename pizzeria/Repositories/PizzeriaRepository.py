from typing import Optional, List

from sqlalchemy.orm import Session
from pizzeria.Entities.Pizzeria import Pizzeria
from pizzeria.schemas.pizzeria import PizzeriaCreate, PizzeriaSchema , PizzeriaBase

class PizzeriaRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, pizzeria: PizzeriaCreate) -> PizzeriaSchema:
        db_pizzeria = Pizzeria(name = pizzeria.name,
                               location = pizzeria.location)
        self.db.add(db_pizzeria)
        self.db.commit()
        self.db.refresh(db_pizzeria)
        return db_pizzeria

    def get_all(self) ->Optional[List[PizzeriaBase]]:
        pizzarias = self.db.query(Pizzeria).all()
        if pizzarias :
            return [PizzeriaBase(name = pizzeria.name , location = pizzeria.location ) for pizzeria in pizzarias]
        else :
            return None

    def get(self, pizzeria_id: int) -> Optional[Pizzeria]:
        pizzeria= self.db.query(Pizzeria).filter(Pizzeria.id == pizzeria_id).first()
        if pizzeria:
            return pizzeria
        else:
            return None

    def update(self, pizzeria_id: int, pizzeria: PizzeriaCreate) -> Optional[Pizzeria]:
        db_pizzeria = self.get(pizzeria_id)
        if db_pizzeria:
            for var, value in vars(pizzeria).items():
                setattr(db_pizzeria, var, value)
            self.db.commit()
            self.db.refresh(db_pizzeria)
            return db_pizzeria
        else :
            return None


    def delete(self, pizzeria_id: int) -> Optional[Pizzeria]:
        db_pizzeria = self.get(pizzeria_id)
        if db_pizzeria:
            self.db.delete(db_pizzeria)
            self.db.commit()
            return db_pizzeria
        else :
            return None
