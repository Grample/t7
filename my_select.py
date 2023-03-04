from sqlalchemy import func, desc

from model import Student, Teacher, Group, Discipline, Grade
from connector import session

def select_1():
    results = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all()
    for result in results:    
        print(result)  
    print()      


def select_2():
    result = session.query(Discipline.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).join(Student).join(Discipline).filter(Discipline.id == 3).group_by(Student.fullname, Discipline.name).order_by(desc("avg_grade")).first()
    print(result)
    print()
    
def select_3():
    results = session.query(Discipline.name, Group.name, func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).join(Student).join(Discipline).join(Group).filter(Discipline.id == 5).group_by(Discipline.name, Group.name).order_by(desc("avg_grade")).all()
    for result in results:    
        print(result)
    print()

def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).order_by(desc("avg_grade")).scalar()
    print(result)
    print()

def select_5():
    results = session.query(Teacher.fullname, Discipline.name)\
        .select_from(Discipline).join(Teacher).filter(Teacher.id == 2).order_by(desc(Discipline.name)).all()
    for result in results:    
        print(result)
    print()   

def select_6():
    results = session.query(Group.name, Student.fullname)\
        .select_from(Student).join(Group).filter(Group.id == 2).order_by(Student.fullname).all()
    for result in results:    
        print(result)
    print()

def select_7():
    results = session.query(Student.fullname, Discipline.name, Group.name, Grade.grade)\
        .select_from(Grade).join(Discipline).join(Student).join(Group).filter(Group.id == 2, Discipline.id == 1).order_by(Grade.grade).all()
    for result in results:    
        print(result)
    print()    

def select_8():
    results = session.query(Teacher.fullname, Discipline.name, func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).join(Discipline).join(Teacher).filter(Teacher.id == 5).group_by(Teacher.fullname, Discipline.name).order_by("avg_grade").all()
    for result in results:    
        print(result)
    print()    

def select_9():
    results = session.query(Student.fullname, Discipline.name)\
        .select_from(Grade).join(Discipline).join(Student).filter(Student.id == 29).group_by(Discipline.name, Student.fullname).order_by(Discipline.name).all()
    for result in results:    
        print(result)
    print()

def select_10():
    results = session.query(Teacher.fullname, Student.fullname, Discipline.name)\
        .select_from(Grade).join(Discipline).join(Student).join(Teacher).filter(Student.id == 12, Teacher.id == 5).group_by(Discipline.name, Student.fullname, Teacher.fullname).order_by(Discipline.name).all()
    for result in results:    
        print(result)
    print()           

if __name__ == '__main__':
    print("Найти 5 студентов с наибольшим средним баллом по всем предметам.")
    select_1()
    print("Найти студента с наивысшим средним баллом по определенному предмету.")
    select_2()
    print("Найти средний балл в группах по определенному предмету.")
    select_3()
    print("Найти средний балл на потоке (по всей таблице оценок).")
    select_4()
    print("Список курсов, которые читает определенный преподаватель.")
    select_5()
    print("Найти список студентов в определенной группе.")
    select_6()
    print("Найти оценки студентов в отдельной группе по определенному предмету.")
    select_7()
    print("Найти средний балл, который ставит определенный преподаватель по своим предметам.")
    select_8()
    print("Найти список курсов, которые посещает определенный студент.")
    select_9()
    print("Список курсов, которые определенному студенту читает определенный преподаватель.")
    select_10()