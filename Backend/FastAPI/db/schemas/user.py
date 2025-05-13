def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]}


def users_schemas(users) -> list:
    users = [user_schema(user) for user in users]
    return users
