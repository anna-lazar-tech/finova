from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.operation import OperationCreate, OperationRead
from app.services.operation_service import add_operation, list_operations


router = APIRouter()


@router.post("/", response_model=OperationRead, status_code=201)
def create_operation(
    operation_data: OperationCreate,
    db: Session = Depends(get_db),
):
    return add_operation(db, operation_data)


@router.get("/", response_model=list[OperationRead])
def get_operations(
    db: Session = Depends(get_db),
):
    return list_operations(db)