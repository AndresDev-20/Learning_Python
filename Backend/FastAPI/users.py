##Clase de Creacion de la API
from fastapi import FastAPI
# Importamos esto ya que vamos a empezar a trabajar con una entidad
from pydantic import BaseModel

app = FastAPI()
# Creamos una clase que va a representar la entidad
class User(BaseModel):
    id: int
    name: str
    age: int

users_list = [
    User(id=1, name="Andres", age=20),
    User(id=2, name="Yeison", age=20),
    User(id=3, name="Alan", age=20),
    User(id=4, name="Aliss", age=20),
    User(id=5, name="Andres", age=20)
]


# Iniciamos el server con: uvicorn users:app --reload
@app.get("/usersjson")
async def users():
    return [{"Name": "Juan", "Age": 25}, {"Name": "Pedro", "Age": 30}, {"Name": "Juan", "Age": 25}, {"Name": "Pedro", "Age": 30}]

@app.get("/users")
async def users_class():
    return users_list 




## Clase de aprender sobre el Patch y el Query

# Path 
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query params
@app.get("/user/")
async def user_query(id: int):
    return search_user(id)


# Clase para las Operaciones POST, PUT y DELETE
@app.post("/user")
async def add_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return {"message": "El usuario ha sido registrado"}


@app.put("/user/")
async def update_user(user_update: User):

    found = False

    for index, save_user in enumerate(users_list):
        if save_user.id == user_update.id:
            users_list[index] = user_update
            found = True
            return {"Message": "Usuario Actualizado"}
        
    if not found:
        return {"Error": "Usuario no se pudo actualizar"}
    


@app.delete("/user/{id}")
async def delete_user(id: int):
    found = False

    for index, users in enumerate(users_list):
        if(users.id == id):
            del users_list[index]
            found = True
            return {"Message": "Usuario eliminado"}
        
    if not found:
        return {"Error": "El usuario no se ha eliminado"}


# Funcion definitiva para todo lo anterior
def search_user(id: int):
    try:
        users = filter(lambda user: user.id == id, users_list)
        return list(users)[0]
    except:
        return "Usuario no encontrado"