from pymongo import MongoClient

#Base de datos local
#db_client = MongoClient().local.

#Base de datos remota 

db_client = MongoClient(
    "Url_Databse").test