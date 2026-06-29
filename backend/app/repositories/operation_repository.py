from sqlalchemy.orm import Session

from app.models.operation import Operation
from app.schemas.operation import OperationCreate


def create_operation(db: Session, operation_data: OperationCreate) -> Operation:
    operation = Operation(**operation_data.model_dump())

    db.add(operation)
    db.commit()
    db.refresh(operation)

    return operation


def get_operations(db: Session) -> list[Operation]:
    return db.query(Operation).order_by(Operation.operation_date.desc()).all()