from datetime import date, datetime
from enum import Enum

from sqlalchemy import Date, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class OperationType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Operation(Base):
    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    amount: Mapped[float] = mapped_column(Float, nullable=False)
    operation_type: Mapped[OperationType] = mapped_column(String, nullable=False)

    description: Mapped[str | None] = mapped_column(String, nullable=True)
    operation_date: Mapped[date] = mapped_column(Date, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    user = relationship("User", back_populates="operations")
    category = relationship("Category", back_populates="operations")