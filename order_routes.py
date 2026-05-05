from fastapi import APIRouter

order_router = APIRouter(prefix="/vendas", tags=["vendas"])

@order_router.get("/vendas")
async def vendas():
    return {"message": "Você acessou a rota de vendas!"}