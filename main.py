#This is my first FastAPI application integrated with Docker and Jenkins
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "Docker and Jankins program!"}   