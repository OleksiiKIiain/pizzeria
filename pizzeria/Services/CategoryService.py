from typing import List

from sqlalchemy.orm import Session

from pizzeria.Entities.error import ErrorResult
from pizzeria.schemas.category import CategoryCreate, CategorySchema,CategoryBase
from pizzeria.Repositories.CategoryRepository import CategoryRepository

class CategoryService:
    def __init__(self, db: Session):
        self.category_repository = CategoryRepository(db)

    def create_category(self, category: CategoryCreate) :
        return self.category_repository.create(category)

    def get_all_categories(self) :
        categories= self.category_repository.get_all()
        if categories :
            return categories
        else :
            return ErrorResult(message ="List is empty")

    def get_category(self, category_id: int) :
        category= self.category_repository.get_by_id(category_id)
        if category :
            return category
        else :
            return ErrorResult(message = f"Category with id = {category_id} not found  ")

    def update_category(self, category_id: int, category: CategoryCreate):
        category= self.category_repository.update(category_id, category)
        if category:
            return {"detail": f"Category is update successfully"}
        else:
            return ErrorResult(message=f"Update category failed")

    def delete_category(self, category_id: int):
        category= self.category_repository.delete(category_id)

        if category:
            return {"detail": f"Category with {category_id} has been deleted"}
        else:
            return ErrorResult(message="Category not found")
