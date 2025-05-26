# SQLModel Training Project

A demonstration project for learning and practicing SQLModel, a library that combines SQLAlchemy Core and Pydantic for type-safe database interactions in Python.

## Project Overview

This project consists of two separate applications that demonstrate SQLModel usage with different domain models:

1. **Heroes App**: A superhero management system where heroes can join teams and participate in missions.
2. **Students App**: A student management system where students can join clubs and enroll in courses.

Each application has its own database and models, demonstrating how to properly separate concerns when working with SQLModel.

## Requirements

- Python 3.13 or higher
- SQLModel 0.0.24 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sqlmodel-training
   ```

2. Install dependencies and create virtual environment:
   ```bash
   uv sync
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Project Structure

```
sqlmodel-training/
├── README.md
├── pyproject.toml
├── main.py                 # Main entry point to run both apps
├── utils.py                # Shared utilities for database operations
├── base.py                 # Base model definitions
├── heroes/                 # Heroes application
│   ├── __init__.py
│   ├── app.py              # Heroes app functionality
│   └── models.py           # Hero, Team, Mission models
└── students/               # Students application
    ├── __init__.py
    ├── app.py              # Students app functionality
    └── models.py           # Student, Club, Course models
```

## Application Details

### Heroes App

The Heroes app demonstrates:
- Many-to-many relationships between Heroes and Teams
- Many-to-many relationships with additional data (Heroes and Missions with roles)
- CRUD operations on related entities

#### Models:
- **Hero**: Represents a superhero with name, secret identity, and age
- **Team**: Represents a team of heroes with name and headquarters
- **Mission**: Represents a mission with name and description
- **HeroTeamLink**: Link model for the many-to-many relationship between heroes and teams
- **HeroMissionLink**: Link model for the many-to-many relationship between heroes and missions, including role information

### Students App

The Students app demonstrates:
- Many-to-many relationships between Students and Clubs
- Many-to-many relationships with additional data (Students and Courses with enrollment information)
- Working with date fields and more complex data types

#### Models:
- **Student**: Represents a student with personal information
- **Club**: Represents a club that students can join
- **Course**: Represents an academic course with subject and level
- **Enrollment**: Link model for the many-to-many relationship between students and courses, including grade and enrollment date
- **StudentClubLink**: Link model for the many-to-many relationship between students and clubs

## Usage

### Running the Applications

You can run both applications sequentially:

```bash
python main.py
```

Or run them individually:

```bash
python -m heroes.app
python -m students.app
```

### Key Features Demonstrated

1. **SQLModel ORM Usage**: Define models, create tables, and perform CRUD operations
2. **Relationship Handling**: Many-to-many relationships with and without additional data
3. **Database Separation**: Properly isolate models to their respective databases
4. **Context Managers**: Safe database session handling

## Solution to Common Issues

### Preventing Cross-Database Table Creation

The project demonstrates how to prevent tables from both apps being created in both databases by:

1. Using the `models` parameter in the `create_db_and_tables` function to specify which models should be created in each database:

```python
create_db_and_tables(engine, models=[Hero, Team, Mission, HeroMissionLink, HeroTeamLink])
```

This ensures that only the relevant tables are created in each database.

## License

[MIT License](LICENSE)
