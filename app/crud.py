from app.models import UserModel
from bson import ObjectId
from fastapi import HTTPException

# Create a new user
async def create_user(user: UserModel, db):
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection not ready.")
    
    user_dict = user.dict()
    result = await db["users"].insert_one(user_dict)
    return str(result.inserted_id)

# Fetch all users
async def get_all_users(db):
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection not ready.")
    
    users = []
    cursor = db["users"].find({})
    async for document in cursor:
        document["_id"] = str(document["_id"])
        users.append(document)
    return users