from fastapi import FastAPI

app = FastAPI()

from order_routes import order_router
from admin_routes import admin_router

app.include_router(admin_router)
app.include_router(order_router)



# endpoint: http://127.0.0.1:8000/orders


# para rodar o código, rode no terminal: uvicorn main:app --reload  