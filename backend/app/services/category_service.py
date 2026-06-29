from sqlalchemy.orm import Session

from app.models.category import Category
from app.repositories.category_repository import create_category, get_categories
from app.schemas.category import CategoryCreate


def add_category(db: Session, category_data: CategoryCreate) -> Category:
    return create_category(db, category_data)


def list_categories(db: Session) -> list[Category]:
    return get_categories(db)