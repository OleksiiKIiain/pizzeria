from typing import List, Type, Optional

from sqlalchemy.orm import Session
from pizzeria.Entities.Category import Category
from pizzeria.schemas.category import CategoryCreate, CategorySchema, CategoryBase

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, category: CategoryCreate) -> Category:
        db_category = Category(name=category.name, pizzeria_id=category.pizzeria_id)
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def get_all(self) -> Optional[List[CategoryBase]]:
        categories = self.db.query(Category).all()
        if categories:
            return [CategoryBase(name = category.name) for category in categories]
        else :
            return None

    def get_by_id(self, category_id: int) -> Optional[Category]:
        category = self.db.query(Category).filter(Category.id == category_id).first()
        if category:
            return category
        else :
            return None

    def update(self, category_id: int, category: CategoryCreate) -> Optional[Category]:
        db_category = self.get_by_id(category_id)
        if db_category:
            for var, value in vars(category).items():
                setattr(db_category, var, value)
            self.db.commit()
            self.db.refresh(db_category)
            return db_category
        else :
            return None

    def delete(self, category_id: int) -> Optional[Category]:
        db_category = self.get_by_id(category_id)
        if db_category:
            self.db.delete(db_category)
            self.db.commit()
            return db_category
        else :
            return None
