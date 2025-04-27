# Import AsyncIOMotorClient for asynchronous MongoDB connection
from motor.motor_asyncio import AsyncIOMotorClient

# Import os module to access environment variables
import os

# Load environment variables from .env file
from dotenv import load_dotenv

# Load all environment variables
load_dotenv()

# Retrieve the MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")

# Function to connect to MongoDB
async def connect_to_mongo(app):
    # Create a MongoDB client and store it in the app state
    app.state.client = AsyncIOMotorClient(MONGO_URI)
    # Connect to the specified database inside the cluster
    app.state.db = app.state.client.get_database("empire_db")
    print("✅ MongoDB connected successfully.")

# Function to close the MongoDB connection
async def close_mongo_connection(app):
    # Close the MongoDB client connection
    app.state.client.close()
    print("❌ MongoDB connection closed.")