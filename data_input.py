import sqlite3 as sq


def new_student():
    name = input('Введите имя: ')
    birth = input('Введите дату рождения в формите мм-дд-гггг: ')
    phone = input('Введите номер телефона в формате 8**********: ')
    address = input('Введите адрес: ')
    grade = input('Введите текущий класс ученика: ')
    with sq.connect('School.db') as con:
        cur = con.cursor()
        cur.execute(
            """INSERT INTO Students (Name, Date_of_Birth, Phone_number, Address, Current_grade) \
            VALUES (?, ?, ?, ?, ?)""", (name, birth, phone, address, grade))
    return


def new_teacher():
    name = input('Введите имя: ')
    birth = input('Введите дату рождения в формите мм-дд-гггг: ')
    phone = input('Введите номер телефона в формате 8**********: ')
    address = input('Введите адрес: ')
    k = 1
    while k == 1:
        question = input('Есть ли у учителя классное руководство y/n?: ')
        if question == 'y':
            grade = input('Каким классом руководит учитель: ')
            k = 0
        elif question == 'n':
            grade
            k = 0
        else:
            print('Вы ошиблись при вводе ответа на вопрос')
            k = 1
    subject = input('Введите специализацию: ')
    with sq.connect('School.db') as con:
        cur = con.cursor()
        cur.execute(
            """INSERT INTO Teachers (Name, Date_of_Birth, Phone_number, Address, Class_management, Specialisation) \
            VALUES (?, ?, ?, ?, ?, ?)""", (name, birth, phone, address, grade, subject))
    return


def find_student():
    name = input('Введите имя: ')
    with sq.connect('School.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT ID_student, Name, Date_of_Birth, Phone_number, Address, Current_grade \
            FROM Students WHERE Name = ?""", (name,))
        if cur is None:
            for result in cur:
                print(result)
        else:
            print('Ученика нет в базе')
    return


def find_teacher():
    name = input('Введите имя: ')
    with sq.connect('School.db') as con:
        cur = con.cursor()
        cur.execute(
            """SELECT ID_teacher, Name, Date_of_Birth, Phone_number, Address, Class_management, Specialisation \
            FROM Teachers WHERE Name = ?""", (name,))
        if cur is None:
            for result in cur:
                print(result)
        else:
            print('Учителя нет в базе')
    return


def get_timetable():
    name = input('Введите имя ученика: ')
    with sq.connect('School.db') as con:
        cur = con.cursor()
        col = cur.execute('SELECT * FROM Timetable')
        columns = list(map(lambda x: x[0], col.description))
        cur.execute(
            """SELECT Current_grade FROM Students WHERE Name = ?""", (name,))
        grade = cur.fetchone()
        grade = grade[0]
        result = cur.execute(
            """SELECT Lesson_number, Start_time, End_time, Teacher_ID, Subject, Class_number, ID_class\
            FROM Timetable WHERE Class_number = ?""", (grade,))
        for el in columns:
            print(el, end='\t')
        print()
        for item in result:
            for el in item:
                print(el, end='\t')
            print()
    return
