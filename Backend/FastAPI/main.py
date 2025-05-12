from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles  # Para recursos estáticos

# Importamos los routers (users y products)
from routers import users, products, basic_auth_users

app = FastAPI()

# Montamos la carpeta 'static' en la URL '/static'
# Esto permite acceder a archivos estáticos desde el navegador
# Ejemplo: http://127.0.0.1:8000/static/images/Imagen-2.jpeg
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluimos nuestros routers personalizados
app.include_router(users.router)
app.include_router(products.router)
app.include_router(basic_auth_users.router)

@app.get("/")
async def root():
    return "Hello FastAPI!"

@app.get("/nuevaruta")
async def nueva_ruta():
    return {"message": "Esta es una nueva ruta en FastAPI!"}
