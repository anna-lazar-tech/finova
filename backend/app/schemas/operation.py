from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


class OperationBase(BaseModel):
    amount: float = Field(gt=0)
    category_id: int
    user_id: int
    description: str | None = None
    operation_date: date


class OperationCreate(OperationBase):
    pass


class OperationRead(OperationBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    operation_type: str
    created_at: datetime
    updated_at: datetime