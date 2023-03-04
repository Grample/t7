from random import randint
import random

from faker import Faker

from connector import session
from model import Student, Teacher, Group, Discipline, Grade

DISCIPLINES = [
    "Вища математика",
    "Фізика",
    "Програмування",
    "Історія України",
    "Англійська"
]

GROUPS = ["group-1", "group-2", "group-3"]
NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50
fake = Faker("uk_UA")


def create_groups():
    for group_ in GROUPS:
        group = group(
            name=group_
        )
        session.add(group)
    session.commit()


def create_students():
    groups_rel = session.query(Group.id).all()
    for _ in range(1, NUMBER_STUDENTS + 1):
        student = Student(
            fullname=fake.name(),
            group_id=(random.choice(groups_rel))[0]
        )
        session.add(student)
    session.commit()


def create_teachers():
    for _ in range(1, NUMBER_TEACHERS + 1):
        teacher = Teacher(
            fullname=fake.name()
        )
        session.add(teacher)
    session.commit()


def create_disciplines():
    teachers_rel = session.query(Teacher.id).all()
    print(teachers_rel)

    for discip in DISCIPLINES:
        discipline = Discipline(
            name=discip,
            teacher_id=(random.choice(teachers_rel))[0]
        )
        session.add(discipline)
    session.commit()


def create_grades():
    disciplines_rel = session.query(Discipline.id).all()
    students_rel = session.query(Student.id).all()
    for i in range(1, NUMBER_STUDENTS + 1):
        grade = Grade(
            grade=random.choice(range(1, 12)),
            date_of=fake.date_between(start_date="-1y"),
            discipline_id=(random.choice(disciplines_rel))[0],
            student_id=(random.choice(students_rel))[0],
            id=i
        )
        session.add(grade)
    session.commit()


if __name__ == '__main__':
    create_groups()
    create_students()
    create_teachers()
    create_disciplines()
    create_grades()