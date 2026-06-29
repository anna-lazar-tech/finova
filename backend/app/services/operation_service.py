from sqlalchemy.orm import Session

from app.repositories.operation_repository import create_operation, get_operations
from app.schemas.operation import OperationCreate
from app.models.operation import Operation


def add_operation(db: Session, operation_data: OperationCreate) -> Operation:
    return create_operation(db, operation_data)


def list_operations(db: Session) -> list[Operation]:
    return get_operations(db)