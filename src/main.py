from fastapi import FastAPI
from src.config import settings
from src.routers import auth, users, titles

app = FastAPI(
    title="Nexlify",
    description="A Netflix-inspired content catalog API built with FastAPI best practices",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(titles.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Nexlify API! Visit /docs for Swagger UI."}

# TODO
# Routers going to be added here later
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(titles.router, prefix="/titles", tags=["titles"])

# َAPI Access token: eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MmU3MDQzNjllMjM4MDk2ZjAxNDgxMDNhNzg1N2JjZCIsIm5iZiI6MTc2NjE1NzA4OS41MjgsInN1YiI6IjY5NDU2YjIxNmQzNjU2MDBmYWZiMDdmOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.A-6h6iqYKkbQ6Xqdfu3FnJ56DwDkEZZtEXAYVm0FkVM