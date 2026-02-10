from fastapi import FastAPI
from .routes import blogs

app = FastAPI(
    title="Blog Posting API",
    description="A simple blog posting API",
    version="1.0.0",
)

# Include routers
app.include_router(blogs.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Blog Posting API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "blog-posting-api"}