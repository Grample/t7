import argparse
import sqlalchemy
from sqlalchemy.sql import select, update, insert, delete
from model import Group, Student, Teacher, Discipline, Grade
from connector import conn

parser = argparse.ArgumentParser(description='CRUD create read update delete')

parser.add_argument("-a", "--action", choices=['create', 'read', 'update', 'delete'], required=True)
parser.add_argument("-m", "--model", choices=['Group', 'Student', 'Teacher', 'Discipline', 'Grade'], required=True)
parser.add_argument("-id", "--id", type=int, default=None)
parser.add_argument("-n", "--name", type=str, default=None)
parser.add_argument("-fn", "--fullname", type=str, default=None)
parser.add_argument("-gid", "--group_id", type=int, default=None)
parser.add_argument("-tid", "--teacher_id", type=int, default=None)
parser.add_argument("-did", "--discipline_id", type=int, default=None)
parser.add_argument("-sid", "--student_id", type=int, default=None)
parser.add_argument("-g", "--grade", type=int, default=None)

args = parser.parse_args()

def do_action(args):
    if args.action == "read":
        query = eval(f"select({args.model})")

    elif args.action == "create":
        model = args.model
        if model == "Group":
            values = f"gr_name='{args.name}'"
        elif model == "Student":
            values = f"student='{args.fullname}', group_id={args.group_id}"
        elif model == "Teacher":
            values = f"teacher='{args.fullname}'"
        elif model == "Discipline":
            values = f"discipline='{args.name}', teacher_id={args.teacher_id}"
        elif model == "Grade":
            values = f"grade={args.grade}, student_id={args.student_id}, discipline_id={args.discipline_id}"
        query = eval(f"insert({args.model}).values({values})")

    elif args.action == "update":
        model = args.model
        if model == "Group":
            values = f"gr_name='{args.name}'"
        elif model == "Student":
            values = f"student='{args.fullname}'"
        elif model == "Teacher":
            values = f"teacher='{args.fullname}'"
        elif model == "Discipline":
            values = f"discipline='{args.fullname}'"
        elif model == "Grade":
            values = f"grade={args.grade}"
        query = eval(f"update({args.model}).values({values}).where(eval(f'{args.model}.id=={args.id}'))")

    elif args.action == "delete":
        query = eval(f"delete({args.model}).where(eval(f'{args.model}.id=={args.id}'))")

    return conn.execute(query)

if __name__ == '__main__':
    for i in do_action(args):
        print(i)