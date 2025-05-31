from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    """Base model class for all models in the application."""

    id: int | None = Field(default=None, primary_key=True)

    class Config:
        """Configuration for the base model."""

        arbitrary_types_allowed = True
