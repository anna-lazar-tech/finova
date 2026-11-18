from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.category import Category
from app.models.user import User


router = APIRouter()


DEFAULT_CATEGORIES = [
    {"name": "Salary", "category_type": "income", "icon": "💼", "color": "#22C55E"},
    {"name": "Bonus", "category_type": "income", "icon": "🎁", "color": "#84CC16"},
    {"name": "Food", "category_type": "expense", "icon": "🍔", "color": "#F97316"},
    {"name": "Transport", "category_type": "expense", "icon": "🚗", "color": "#3B82F6"},
    {"name": "Housing", "category_type": "expense", "icon": "🏠", "color": "#6366F1"},
    {"name": "Healthcare", "category_type": "expense", "icon": "💊", "color": "#EF4444"},
    {"name": "Education", "category_type": "expense", "icon": "📚", "color": "#8B5CF6"},
    {"name": "Entertainment", "category_type": "expense", "icon": "🎮", "color": "#EC4899"},
    {"name": "Shopping", "category_type": "expense", "icon": "🛒", "color": "#F59E0B"},
    {"name": "Travel", "category_type": "expense", "icon": "✈️", "color": "#06B6D4"},
]


def create_default_categories(db: Session, user_id: int) -> int:
    created_count = 0

    for category_data in DEFAULT_CATEGORIES:
        existing_category = (
            db.query(Category)
            .filter(
                Category.user_id == user_id,
                Category.name == category_data["name"],
            )
            .first()
        )

        if existing_category:
            continue

        category = Category(
            **category_data,
            user_id=user_id,
            is_system=True,
        )

        db.add(category)
        created_count += 1

    db.commit()

    return created_count


@router.post("/create-demo-user")
def create_demo_user(db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == "demo@finova.app").first()

    if existing_user:
        created_categories = create_default_categories(db, existing_user.id)

        return {
            "message": "Demo user already exists",
            "user_id": existing_user.id,
            "email": existing_user.email,
            "created_categories": created_categories,
        }

    demo_user = User(
        email="demo@finova.app",
        password_hash="demo_password_not_for_production",
    )

    db.add(demo_user)
    db.commit()
    db.refresh(demo_user)

    created_categories = create_default_categories(db, demo_user.id)

    return {
        "message": "Demo user created",
        "user_id": demo_user.id,
        "email": demo_user.email,
        "created_categories": created_categories,
    }