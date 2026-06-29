from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.category import CategoryCreate, CategoryRead
from app.services.category_service import add_category, list_categories


router = APIRouter()


@router.post("/", response_model=CategoryRead, status_code=201)
def create_category(
    category_data: CategoryCreate,
    db: Session = Depends(get_db),
):
    return add_category(db, category_data)


@router.get("/", response_model=list[CategoryRead])
def get_categories(
    db: Session = Depends(get_db),
):
    return list_categories(db)