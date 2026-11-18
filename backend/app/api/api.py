from fastapi import APIRouter

from app.api.routes import categories, demo, operations


api_router = APIRouter()

api_router.include_router(
    demo.router,
    prefix="/demo",
    tags=["Demo"],
)

api_router.include_router(
    categories.router,
    prefix="/categories",
    tags=["Categories"],
)

api_router.include_router(
    operations.router,
    prefix="/operations",
    tags=["Operations"],
)