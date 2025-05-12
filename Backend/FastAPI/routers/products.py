from fastapi import APIRouter

router = APIRouter(
    prefix="/products",  # Todas las rutas empiezan con /products
    tags=["products"],   # Etiqueta para la documentación
    responses={404: {"Message": "No encontrado"}}  # Personalizamos el mensaje de error
)

products_list = ["Producto 1", "Producto 2"]

@router.get("/")
async def products():
    return products_list
