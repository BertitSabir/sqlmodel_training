from contextlib import contextmanager
from typing import Generator
from sqlmodel import create_engine, SQLModel, Session, text
from sqlalchemy.engine import Engine
from pathlib import Path


def get_database_url(name: str) -> str:
    """
    Generate an SQLite database URL string for the given database name.

    Args:
        name (str): The name of the database.

    Returns:
        str: The SQLite database URL.
    """
    # check if a databse with this name exist in the current directory
    if Path(f"{name}.db").exists():
        print(f"Database {name}.db already exists. Deleting it.")
        Path(f"{name}.db").unlink()
    # return the SQLite database URL
    return f"sqlite:///{name}.db"


def get_engine(db_url: str) -> Engine:
    """Create and return a new SQLAlchemy engine using the provided database URL.

    Args:
        db_url (str): The database URL to connect to.

    Returns:
        Engine: A SQLAlchemy Engine instance connected to the specified database.
    """
    return create_engine(url=db_url, echo=True)


@contextmanager
def get_session(engine: Engine) -> Generator[Session, None, None]:
    """
    Context manager that yields a new Session object bound to the provided engine.

    Args:
        engine (Engine): The SQLAlchemy Engine instance to bind the session to.

    Yields:
        Session: A SQLModel Session instance.
    """
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


def create_db_and_tables(engine: Engine, models=None):
    """
    Create tables in the database using the provided engine and models.

    Args:
        engine (Engine): The SQLAlchemy Engine instance to use for table creation.
        models (list, optional): List of SQLModel classes to create tables for.
                               If None, uses all registered models.
    """
    if models:
        # Create only the specified models
        SQLModel.metadata.create_all(
            engine, tables=[model.__table__ for model in models]
        )
    else:
        # Create all models
        SQLModel.metadata.create_all(engine)

    with engine.connect() as connection:
        connection.execute(text("PRAGMA foreign_keys=ON"))


def clear_db_and_tables(engine: Engine):
    """
    Drop all tables in the database using the provided engine.

    Args:
        engine (Engine): The SQLAlchemy Engine instance to use for dropping tables.
    """
    SQLModel.metadata.drop_all(engine)
