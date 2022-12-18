import sqlite3
from datetime import datetime

now = datetime.now()

conn = sqlite3.connect("база даных.sqlite")
curs = conn.cursor()

# после первого запуска за коментировать до строки 35 !!!!
# добавление таблиц
curs.execute("CREATE TABLE Students(id int, name varchar(32),surname varchar(32), age int,city varchar(32))")

curs.execute("CREATE TABLE Courses(id int,name varchar(32), time_start int,time_end int)")

curs.execute("CREATE TABLE Student_courses(student_id int, course_id int)")

# добывление курса
curs.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)",
                 [(1, 'python', now.strftime('21.07.21'), now.strftime('21.08.21')),
                  (2, 'java', now.strftime('13.07.21'), now.strftime('16.08.21'))])

# добавление студентов
curs.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)",
                 [(1, 'Max', 'Brooks', 24, 'Spb'),
                  (2, 'John', 'Stones', 15, 'Spb'),
                  (3, 'Andy', 'Wings', 45, 'Manhester'),
                  (4, 'Kate', 'Brooks', 34, 'Spb')])

# добавление Student_courses
curs.executemany("INSERT INTO Student_courses VALUES (?, ?)", [(1, 1),
                                                               (2, 1),
                                                               (3, 1),
                                                               (4, 2)])

# до этого момента
# -----------------------------------------------


def Students_age(age):
    curs.execute("SELECT * FROM Students WHERE age >= (?)", [age])
    print(curs.fetchall())


# -----------------------------------------------
def Programming_course(num_course):
    curs.execute("SELECT student_id  FROM Student_courses WHERE course_id == (?)", [num_course])
    h = curs.fetchall()
    for i in h:
        curs.execute("SELECT name FROM Courses WHERE id == (?)", [num_course])
        s = curs.fetchall()
        curs.execute("SELECT * FROM Students WHERE id == (?)", [i[0]])

        print("студенты", curs.fetchall(), "по", s[0][0])


# ---------------------------------------------
def Programming_course_and_city(num_course, city):
    curs.execute("SELECT student_id  FROM Student_courses WHERE course_id == (?)", [num_course])
    for i in curs.fetchall():
        curs.execute("SELECT * FROM Students WHERE city == (?) and id == (?)", [city, i[0]])
        student = curs.fetchall()
        if student != []:
            curs.execute("SELECT name FROM Courses WHERE id == (?)", [num_course])
            print("студенты из города", city, student, "по языку", curs.fetchall()[0][0])


# -----------------------------------------------
conn.commit()
conn.close()
