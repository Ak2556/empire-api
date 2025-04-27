from pydantic import BaseModel, Field
from typing import Optional

class UserModel(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    age: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Akash Thakur",
                "email": "akash@example.com",
                "age": 23
            }
        }