from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt

fake_db = {"users": {}}

app = FastAPI()


class Payload(BaseModel):
    numbers: List[int]

class BinarySearchPayload(BaseModel):
    numbers: List[int]
    target: int

class User(BaseModel):
    username: str
    password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(username: str):
    # This is a simple implementation. In a real-world scenario, you'd want to use more secure practices.
    return jwt.encode({"sub": username}, "secret_key", algorithm="HS256")

async def get_current_user(token: str):
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/bubble-sort")
async def bubble_sort(payload: Payload, token: str):
    try:
        await get_current_user(token)  # Verify token
        numbers = payload.numbers
        n = len(numbers)
        for i in range(n):
            for j in range(0, n - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return {"numbers": numbers}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/filter-even")
async def filter_even_numbers(payload: Payload, token: str):
    try:
        await get_current_user(token)  # Verify token
        numbers = payload.numbers
        even_numbers = [num for num in numbers if num % 2 == 0]
        return {"even_numbers": even_numbers}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/sum-elements")
async def sum_elements(payload: Payload, token: str):
    try:
        await get_current_user(token)  # Verify token
        numbers = payload.numbers
        total_sum = sum(numbers)
        return {"sum": total_sum}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/max-value")
async def max_value(payload: Payload, token: str):
    try:
        await get_current_user(token)  # Verify token
        numbers = payload.numbers
        max_value = max(numbers)
        return {"max": max_value}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/binary-search")
async def binary_search(payload: BinarySearchPayload, token: str):
    try:
        await get_current_user(token)  # Verify token
        numbers = payload.numbers
        target = payload.target
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] == target:
                return {"found": True, "index": mid}
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return {"found": False, "index": -1}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/register")
async def register(user: User):
    if user.username in fake_db["users"]:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = get_password_hash(user.password)
    fake_db["users"][user.username] = hashed_password
    return {"message": "User registered successfully"}

@app.post("/login")
async def login(user: User):
    if user.username not in fake_db["users"] or not pwd_context.verify(user.password, fake_db["users"][user.username]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(user.username)
    return {"access_token": access_token}


   
 






