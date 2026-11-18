from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.category import Category
from app.models.operation import Operation
from app.schemas.operation import OperationCreate


def create_operation(db: Session, operation_data: OperationCreate) -> Operation:
    category = (
        db.query(Category)
        .filter(Category.id == operation_data.category_id)
        .filter(Category.user_id == operation_data.user_id)
        .first()
    )

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    operation = Operation(
        amount=operation_data.amount,
        operation_type=category.category_type,
        category_id=operation_data.category_id,
        user_id=operation_data.user_id,
        description=operation_data.description,
        operation_date=operation_data.operation_date,
    )

    db.add(operation)
    db.commit()
    db.refresh(operation)

    return operation


def get_operations(db: Session) -> list[Operation]:
    return db.query(Operation).order_by(Operation.operation_date.desc()).all()