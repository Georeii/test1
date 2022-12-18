import peewee
from datetime import datetime

now = datetime.now()

conn1 = peewee.SqliteDatabase("база даных.sqlite")

# внимание на строку

class BaseModel(peewee.Model):
    class Meta:
        database = conn1


class Students(BaseModel):
    id = peewee.IntegerField(column_name="id")
    name = peewee.CharField(column_name="name")
    surname = peewee.CharField(column_name="surname")
    age = peewee.IntegerField(column_name="age")
    city = peewee.CharField(column_name="city")


class Courses(BaseModel):
    id = peewee.IntegerField(column_name="id")
    name = peewee.CharField(column_name="name")
    time_start = peewee.CharField(column_name='time_start')
    time_end = peewee.CharField(column_name='time_end')


class StudentCourses(BaseModel):
    student_id = peewee.IntegerField(column_name='student_id')
    course_id = peewee.IntegerField(column_name='course_id')


# после первого запуска за коментировать до строки 51 !!!!
Students.create_table()
Courses.create_table()
StudentCourses.create_table()

Students.insert_many([{'id':1,'name':'Max','surname':'Brooks','age':24,'city':'Spb'},
                      {'id':2,'name':'John','surname':'Stones','age':15,'city':'Spb'},
                      {'id':3,'name':'Andy','surname':'Wings','age':45,'city':'Manhester'},
                      {'id':4,'name':'Kate','surname':'Brooks','age':34,'city':'Spb'}]).execute()

Courses.insert_many([{'id':1,'name':'python','time_start':now.strftime("21.07.21"),'time_end':now.strftime('21.08.21')},
                     {'id':2,'name':'java','time_start':now.strftime('13.07.21'),'time_end':now.strftime('16.08.21')}]).execute()

StudentCourses.insert_many([{'student_id': '1', "course_id": "1"},
                            {'student_id': '2', "course_id": "1"},
                            {'student_id': '3', "course_id": "1"},
                            {'student_id': '4', "course_id": "2"}]).execute()
# до этого момента


for i in Students.select():
    if i.age >= 30:
        print("студенты которым за 30",i, i.name, i.surname, i.age, i.city)

s =[]
for i in StudentCourses.select():
    if i.course_id == 1:
        s.append(i.student_id)

for i in Students.select():
    for j in s:
        if i.id == j:
            print("студенты по пайтон", i, i.name, i.surname, i.age, i.city)

for i in Students.select():
    for j in s:
        if i.id == j:
            if i.city == 'Spb':
                print('студенты по пайтон из города "Spb"', i, i.name, i.surname, i.age, i.city)

