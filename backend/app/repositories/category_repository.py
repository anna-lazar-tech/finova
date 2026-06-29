from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate


def create_category(db: Session, category_data: CategoryCreate) -> Category:
    category = Category(**category_data.model_dump())

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_categories(db: Session) -> list[Category]:
    return db.query(Category).order_by(Category.name.asc()).all()