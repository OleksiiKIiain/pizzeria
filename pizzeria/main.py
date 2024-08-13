import uvicorn
from fastapi import FastAPI
from pizzeria.api import category_router, pizza_router, pizzeria_router

app = FastAPI()


app.include_router(category_router)
app.include_router(pizza_router)
app.include_router(pizzeria_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5003, log_level="info")