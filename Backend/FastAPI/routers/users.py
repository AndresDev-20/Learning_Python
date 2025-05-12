from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

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

@router.get("/usersjson")
async def users():
    return [{"Name": "Juan", "Age": 25}, {"Name": "Pedro", "Age": 30}]

@router.get("/users")
async def users_class():
    return users_list

# ---------------------- PATH PARAM --------------------------
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# --------------------- QUERY PARAM --------------------------
@router.get("/user/")
async def user_query(id: int):
    return search_user(id)

# -------------------- POST ----------------------------------
@router.post("/user", status_code=201)
async def add_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail={"error": "El usuario ya existe"})
    else:
        users_list.append(user)
        return {"message": "El usuario ha sido registrado"}

# --------------------- PUT ----------------------------------
@router.put("/user/")
async def update_user(user_update: User):
    found = False
    for index, save_user in enumerate(users_list):
        if save_user.id == user_update.id:
            users_list[index] = user_update
            found = True
            return {"Message": "Usuario Actualizado"}
    if not found:
        return {"Error": "Usuario no se pudo actualizar"}

# ------------------- DELETE ---------------------------------
@router.delete("/user/{id}")
async def delete_user(id: int):
    found = False
    for index, users in enumerate(users_list):
        if users.id == id:
            del users_list[index]
            found = True
            return {"Message": "Usuario eliminado"}
    if not found:
        return {"Error": "El usuario no se ha eliminado"}

# ------------------- FUNCION AUXILIAR -----------------------
def search_user(id: int):
    try:
        users = filter(lambda user: user.id == id, users_list)
        return list(users)[0]
    except:
        return "Usuario no encontrado"
