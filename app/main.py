from fastapi import FastAPI
from app.config import settings
from app.extractions.router import router as extractions_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)


app.include_router(extractions_router)

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok", "message": "API is running"}