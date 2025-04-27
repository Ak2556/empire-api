from fastapi import FastAPI, Request
from app.database import connect_to_mongo, close_mongo_connection
from app.models import UserModel
from app.crud import create_user, get_all_users

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo(app)

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection(app)

@app.get("/")
async def root():
    return {"message": "Empire API is Live, Commander."}

@app.post("/create_user")
async def api_create_user(user: UserModel, request: Request):
    db = request.app.state.db
    user_id = await create_user(user, db)
    return {"message": "User created successfully", "user_id": user_id}

@app.get("/get_users")
async def api_get_users(request: Request):
    db = request.app.state.db
    users = await get_all_users(db)
    return users