from fastapi import FastAPI, Request, HTTPException

# Import database connection functions
from app.database import connect_to_mongo, close_mongo_connection

# Import user data models
from app.models import UserModel, UserCreate, UserInDB

# Import CRUD operation functions
from app.crud import create_user, get_all_users

# Import password hashing function
from app.security import get_password_hash

# Initialize the FastAPI application
app = FastAPI()

# Event handler triggered when the application starts
@app.on_event("startup")
async def startup_db_client():
    # Connect to MongoDB database
    await connect_to_mongo(app)

# Event handler triggered when the application shuts down
@app.on_event("shutdown")
async def shutdown_db_client():
    # Close MongoDB database connection
    await close_mongo_connection(app)

# Root route to verify server is running
@app.get("/")
async def root():
    return {"message": "Empire API is Live, Commander."}

# Route to create a new user (basic CRUD version, no password security)
@app.post("/create_user")
async def api_create_user(user: UserModel, request: Request):
    db = request.app.state.db
    user_id = await create_user(user, db)
    return {"message": "User created successfully", "user_id": user_id}

# Route to retrieve all users from the database (basic CRUD version)
@app.get("/get_users")
async def api_get_users(request: Request):
    db = request.app.state.db
    users = await get_all_users(db)
    return users

# Secure route to register a new user with password encryption
@app.post("/signup")
async def signup(user: UserCreate, request: Request):
    db = request.app.state.db

    # Check if email is already registered
    existing_user = await db['users'].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Encrypt the user's password before saving
    hashed_password = get_password_hash(user.password)

    # Prepare the user data document for insertion
    user_data = {
        "name": user.name,
        "email": user.email,
        "hashed_password": hashed_password,
        "age": user.age
    }

    # Insert the secured user record into the database
    await db['users'].insert_one(user_data)

    return {"message": "User successfully registered"}