# Import CryptContext from passlib to handle password hashing
from passlib.context import CryptContext

# Setting up the CryptContext to use bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash a plain password securely
def get_password_hash(password: str) -> str:
    # Hash the password using bcrypt and return it
    return pwd_context.hash(password)

# Function to verify if a plain password matches its hashed version
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Compare the provided plain password with the hashed password
    return pwd_context.verify(plain_password, hashed_password)