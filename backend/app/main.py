# main.py
# Entry point of your FastAPI backend
# Docker runs this file to start the backend server

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

# Create the FastAPI app
app = FastAPI(
    title="My CI/CD Backend",
    description="FastAPI backend for CI/CD Learning Framework",
    version="1.0.0"
)

# CORS Middleware
# Allows React frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect all routes from routes.py
app.include_router(router)

# Health check endpoint
@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Backend is running!",
        "framework": "FastAPI"
    }