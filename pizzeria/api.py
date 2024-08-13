from fastapi import APIRouter
from pizzeria.Services.CategoryService import CategoryService
from pizzeria.Services.PizzaService import PizzaService
from pizzeria.Services.PizzeriaService import PizzeriaService
from pizzeria.schemas.category import CategoryCreate
from pizzeria.schemas.pizza import PizzaCreate
from pizzeria.schemas.pizzeria import PizzeriaCreate

from pizzeria.database import get_session

# Створюємо об'єкти сервісів
category_service = CategoryService(get_session())
pizza_service = PizzaService(get_session())
pizzeria_service = PizzeriaService(get_session())

# Створюємо роутери
category_router = APIRouter(prefix="/categories", tags=["Categories"])
pizza_router = APIRouter(prefix="/pizzas", tags=["Pizzas"])
pizzeria_router = APIRouter(prefix="/pizzerias", tags=["Pizzerias"])

# Роути для категорій
@category_router.post("/")
def create_category(category: CategoryCreate):
    return category_service.create_category(category)

@category_router.get("/")
def get_all_categories():
    return category_service.get_all_categories()

@category_router.get("/{category_id}")
def get_by_id_category(category_id : int):
    return category_service.get_category(category_id)

@category_router.put("/{category_id}")
def update_category(category_id:int , category : CategoryCreate):
    return category_service.update_category(category_id,category)

@category_router.delete("/{category_id}")
def delete_category(category_id:int):
    return category_service.delete_category(category_id)

# Роути для піц
@pizza_router.post("/")
def create_pizza(pizza: PizzaCreate):
    return pizza_service.create_pizza(pizza)

@pizza_router.get("/")
def get_all_pizzas():
    return pizza_service.get_all_pizzas()

@pizza_router.get("/{pizza_id}")
def get_by_id_pizza(pizza_id:int):
    return pizza_service.get_pizza(pizza_id)

@pizza_router.put("/{pizza_id}")
def update_pizza(pizza_id:int, pizza :PizzaCreate):
    return pizza_service.update_pizza(pizza_id,pizza)

@pizza_router.delete("/{pizza_id}")
def delete_pizza(pizza_id:int):
    return pizza_service.delete_pizza(pizza_id)




# Роути для піцерій
@pizzeria_router.post("/")
def create_pizzeria(pizzeria: PizzeriaCreate):
    return pizzeria_service.create_pizzeria(pizzeria)

@pizzeria_router.get("/")
def get_all_pizzerias():
    return pizzeria_service.get_all_pizzerias()

@pizzeria_router.get("/{pizzeria_id}")
def get_pizzaria_by_id(pizzeria_id : int):
    return pizzeria_service.get_pizzeria(pizzeria_id)

@pizzeria_router.put("/{pizzeria_id}")
def update_pizzaria(pizzeria_id:int , pizzaria:PizzeriaCreate):
    return pizzeria_service.update_pizzeria(pizzeria_id,pizzaria)

@pizzeria_router.delete("/{pizzeria_id}")
def delete_pizzaria(pizzeria_id:int):
    return pizzeria_service.delete_pizzeria(pizzeria_id)