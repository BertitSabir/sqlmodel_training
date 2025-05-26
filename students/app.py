from datetime import date

from students.models import Student, Course, Enrollment, Club, StudentClubLink
from utils import get_database_url, get_engine, create_db_and_tables, get_session


def create_clubs(session):
    # Create a club:
    art_club = Club(name='Art')

    # Students:
    student1 = Student(
        first_name='Bob',
        last_name='Bib',
        email='bob.bib@mail.com',
        birth_date=date(1999, 1, 5)
    )
    student2 = Student(
        first_name='Tom',
        last_name='tim',
        email='tom.tim@mail.com',
        birth_date=date(1999, 11, 22)
    )

    # Add students to Art's club:
    art_club.students.append(student1)
    art_club.students.append(student2)
    session.add(art_club)
    session.commit()
    session.refresh(art_club)


def create_enrollments(session):
    # Students:
    student3 = Student(
        first_name='foo',
        last_name='bar',
        email='foo.bar@mail.com',
        birth_date=date(1999, 8, 7)
    )
    student4 = Student(
        first_name='toto',
        last_name='titi',
        email='toto.titi@mail.com',
        birth_date=date(1999, 12, 12)
    )

    # create Mathematics course
    math_course = Course(
        name='Mathematics',
        subject='Math',
        level='Beginner'
    )

    # Enroll students:
    student3_enrollment = Enrollment(
        course=math_course,
        student=student3,
        enrollment_date=date(2024, 9, 1)
    )
    student4_enrollment = Enrollment(
        course=math_course,
        student=student4,
        enrollment_date=date(2024, 9, 2)
    )

    session.add(student3_enrollment)
    session.add(student4_enrollment)
    session.commit()
    session.refresh(student3_enrollment)
    session.refresh(student4_enrollment)

    print("Enrollments created:", student3_enrollment, student4_enrollment)


def app():
    db_url = get_database_url(name='students')
    engine = get_engine(db_url=db_url)
    create_db_and_tables(engine, models=[Student, Course, Enrollment, Club, StudentClubLink])
    with get_session(engine) as session:
        create_clubs(session)
        create_enrollments(session)


if __name__ == '__main__':
    app()
