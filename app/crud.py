from app.models import UserModel
from bson import ObjectId
from fastapi import HTTPException
import collections.abc
import inspect

# Function to create a new user in the database
async def create_user(user: UserModel, db):
    if db is None:
        # Raise an error if database connection is not established
        raise HTTPException(status_code=500, detail="Database connection not ready.")
    
    # Convert the user model into a dictionary
    user_dict = user.dict()
    
    # Insert the user document into the 'users' collection
    insert = db["users"].insert_one(user_dict)
    if inspect.isawaitable(insert):
        result = await insert
    else:
        result = insert
    
    # Return the inserted user's ID as a string
    return str(result.inserted_id)

# Function to fetch all users from the database
async def get_all_users(db):
    if db is None:
        # Raise an error if database connection is not established
        raise HTTPException(status_code=500, detail="Database connection not ready.")
    
    users = []
    # Query the 'users' collection to find all user documents
    cursor = db["users"].find({})
    
    # Try async for (Motor), else fallback to sync for (mongomock)
    if hasattr(cursor, "__aiter__"):
        async for document in cursor:
            # Convert MongoDB ObjectId into a string for JSON serialization
            document["_id"] = str(document["_id"])
            users.append(document)
    else:
        for document in cursor:
            # Convert MongoDB ObjectId into a string for JSON serialization
            document["_id"] = str(document["_id"])
            users.append(document)
    
    # Return the list of all users
    return users