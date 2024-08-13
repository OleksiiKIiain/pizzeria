from typing import List, Optional
from sqlalchemy.orm import Session
from pizzeria.Entities.Pizza import Pizza
from pizzeria.schemas.pizza import PizzaCreate, PizzaSchema, PizzaBase


class PizzaRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, pizza: PizzaCreate) -> Pizza:
        db_pizza = Pizza(name=pizza.name, price=pizza.price, category_id=pizza.category_id)
        self.db.add(db_pizza)
        self.db.commit()
        self.db.refresh(db_pizza)
        return db_pizza

    def get_all(self) -> Optional[List[PizzaBase]]:
        pizzas = self.db.query(Pizza).all()
        if pizzas:
            return [PizzaBase(name = pizza.name,price = pizza.price) for pizza in pizzas]
        else :
            return None

    def get_by_id(self, pizza_id: int) -> Optional[Pizza]:
        pizza = self.db.query(Pizza).filter(Pizza.id == pizza_id).first()
        if pizza:
            return pizza
        return None

    def update(self, pizza_id: int, pizza: PizzaCreate) -> Optional[Pizza]:
        db_pizza = self.get_by_id(pizza_id)
        if db_pizza:
            db_pizza.name = pizza.name
            db_pizza.price = pizza.price
            db_pizza.category_id = pizza.category_id
            self.db.commit()
            self.db.refresh(db_pizza)
            return db_pizza
        return None

    def delete(self, pizza_id: int) -> Optional[PizzaSchema]:
        db_pizza = self.get_by_id(pizza_id)
        if db_pizza:
            self.db.delete(db_pizza)
            self.db.commit()
            return PizzaSchema(name = db_pizza.name , id = db_pizza.id, price = db_pizza.price)
        return None
