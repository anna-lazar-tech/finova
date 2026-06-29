from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class OperationType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class OperationBase(BaseModel):
    amount: float = Field(gt=0)
    operation_type: OperationType
    category: str
    description: str | None = None
    operation_date: date


class OperationCreate(OperationBase):
    pass


class OperationRead(OperationBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime