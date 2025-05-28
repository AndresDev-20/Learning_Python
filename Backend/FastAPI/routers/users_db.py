from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schemas
from db.client import db_client
from bson import ObjectId

router = APIRouter()




@router.get("/usersdb")
async def users_class():
    return users_schemas(db_client.users.find())

# ---------------------- PATH PARAM --------------------------
@router.get("/userdb/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))

# --------------------- QUERY PARAM --------------------------
@router.get("/userdb/")
async def user_query(id: str):
    return search_user("_id", ObjectId(id))

# -------------------- POST ----------------------------------
@router.post("/userdb", status_code=201)
async def add_user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail={"error": "El usuario ya existe"})
    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)

# --------------------- PUT ----------------------------------
@router.put("/userdb/", response_model=User)
async def update_user(user_update: User):
   try:
    user_dict = dict(user_update)
    del user_dict["id"]
    db_client.users.find_one_and_replace({"_id": ObjectId(user_update.id)}, user_dict)
   except:
        return {"Error": "Usuario no se pudo actualizar"}
   
   return search_user("_id", ObjectId(user_update.id))

# ------------------- DELETE ---------------------------------
@router.delete("/userdb/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return {"Error": "El usuario no se ha eliminado"}

# ------------------- FUNCION AUXILIAR -----------------------
def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field:key})
        return User(**user_schema(user))
    except:
        return "Usuario no encontrado"



