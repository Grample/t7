from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from connector import engine
#engine = create_engine('sqlite:///sqlalchemy_example.db')

Base = declarative_base()


class Group(Base):
    __tablename__ = 'study_groups'
    id = Column(Integer, primary_key=True)
    gr_name = Column(String(50), nullable=False)
    students = relationship("Student", back_populates="group")

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    group_id = Column(Integer, ForeignKey('study_groups.id', ondelete='CASCADE'))
    group = relationship("Group", back_populates='students')
    grades = relationship("Grade", back_populates='student')


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    discipline = relationship("Discipline", back_populates="teacher")


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    sub_name = Column(String(50), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship("Teacher", back_populates='disciplines')
    grades = relationship("Grade", back_populates='discipline')


class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    mark = Column(Integer)
    discipline_id = Column(Integer, ForeignKey('disciplines.id', ondelete='CASCADE'))
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    discipline = relationship("Discipline", back_populates='grade')
    student = relationship("Student", back_populates='grade')


Base.metadata.create_all(engine)