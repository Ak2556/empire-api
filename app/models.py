# Import necessary modules from Pydantic for data validation
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Basic user model for initial CRUD operations
class UserModel(BaseModel):
    name: str = Field(...)  # Name of the user (required)
    email: EmailStr = Field(...)  # Validated email address (required)
    age: Optional[int] = None  # Age of the user (optional)

    class Config:
        # Example schema used for API documentation (Swagger)
        schema_extra = {
            "example": {
                "name": "Akash Thakur",
                "email": "akash@example.com",
                "age": 23
            }
        }

# Model used specifically for secure user signup payload
class UserCreate(BaseModel):
    name: str = Field(...)  # Name of the user (required)
    email: EmailStr = Field(...)  # Email of the user (required)
    password: str = Field(...)  # Plain password entered by user (required)
    age: Optional[int] = None  # Age of the user (optional)

    class Config:
        # Example schema for signup request
        schema_extra = {
            "example": {
                "name": "Akash Thakur",
                "email": "akash@example.com",
                "password": "StrongPassword123",
                "age": 23
            }
        }

# Internal model representing how user data is stored inside the database
class UserInDB(BaseModel):
    name: str  # Name of the user
    email: EmailStr  # Email of the user
    hashed_password: str  # Encrypted password (hashed form)
    age: Optional[int] = None  # Age of the user (optional)