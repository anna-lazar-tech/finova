from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings
from app.core.database import Base, engine
from app.models import Operation


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.get("/")
def root():
    return {"message": "Welcome to Finova API 🚀"}