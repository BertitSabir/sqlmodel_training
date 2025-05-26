from datetime import date, datetime, timezone
from decimal import Decimal

from sqlmodel import SQLModel, Field, Relationship


class StudentClubLink(SQLModel, table=True):
    student_id: int | None = Field(default=None, foreign_key='student.id', primary_key=True)
    club_id: int | None = Field(default=None, foreign_key='club.id', primary_key=True)


class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=255)
    birth_date: date

    clubs: list['Club'] = Relationship(back_populates='students', link_model=StudentClubLink)
    enrollments: list['Enrollment'] = Relationship(back_populates='student')


class Club(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    students: list[Student] = Relationship(back_populates='clubs', link_model=StudentClubLink)


class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    subject: str = Field(max_length=50)
    level: str | None

    enrollments: list['Enrollment'] = Relationship(back_populates='course')


class Enrollment(SQLModel, table=True):
    student_id: int | None = Field(default=None, foreign_key='student.id', primary_key=True)
    course_id: int | None = Field(default=None, foreign_key='course.id', primary_key=True)
    grade: Decimal | None
    enrollment_date: date
    did_pass: bool = False

    student: Student = Relationship(back_populates='enrollments')
    course: Course = Relationship(back_populates='enrollments')
