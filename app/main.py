from fastapi import FastAPI, Request, HTTPException, status
import jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import inspect
from contextlib import asynccontextmanager

# Import database connection functions
from app.database import connect_to_mongo, close_mongo_connection

# Import user data models
from app.models import UserModel, UserCreate, UserInDB

# Import CRUD operation functions
from app.crud import create_user, get_all_users

# Initialize the FastAPI application with lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo(app)
    try:
        yield
    finally:
        await close_mongo_connection(app)

app = FastAPI(lifespan=lifespan)

SECRET_KEY = "your_secret_key_here"  # Change this to a secure random value in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    email: str
    password: str

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
    find = db['users'].find_one({"email": user.email})
    if inspect.isawaitable(find):
        existing_user = await find
    else:
        existing_user = find
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_data = {
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "age": user.age
    }

    insert = db['users'].insert_one(user_data)
    if inspect.isawaitable(insert):
        await insert
    else:
        pass
    return {"message": "User successfully registered"}

@app.post("/login")
async def login(login_req: LoginRequest, request: Request):
    email = login_req.email
    password = login_req.password
    db = request.app.state.db
    find = db['users'].find_one({"email": email})
    if inspect.isawaitable(find):
        user = await find
    else:
        user = find
    if not user or user.get("password") != password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    # Create JWT token
    payload = {
        "sub": user["email"],
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        "name": user["name"]
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}