from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

async def connect_to_mongo(app):
    app.state.client = AsyncIOMotorClient(MONGO_URI)
    app.state.db = app.state.client.get_database("empire_db")
    print("✅ MongoDB connected successfully.")

async def close_mongo_connection(app):
    app.state.client.close()
    print("❌ MongoDB connection closed.")