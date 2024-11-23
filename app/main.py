from fastapi import FastAPI
from .routers import items

app = FastAPI(
    title="My FastAPI App",
    description="A simple FastAPI application",
    version="1.0.0"
)

app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI application!"} 
    return {"message": "Welcome to my FastAPI application!"} 