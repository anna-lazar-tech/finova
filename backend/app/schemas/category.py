from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict


class CategoryType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class CategoryBase(BaseModel):
    name: str
    category_type: CategoryType
    icon: str | None = None
    color: str | None = None


class CategoryCreate(CategoryBase):
    user_id: int


class CategoryRead(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    created_at: datetime