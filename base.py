from sqlmodel import SQLModel, Field
from typing import Optional


class BaseModel(SQLModel):
    """Base model class for all models in the application."""

    id: Optional[int] = Field(default=None, primary_key=True)

    class Config:
        """Configuration for the base model."""

        arbitrary_types_allowed = True
