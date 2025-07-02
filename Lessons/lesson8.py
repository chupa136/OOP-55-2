import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            fio VARCAHR (100) NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades(
            gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER,
            subject VARCAHR (100) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (userid) REFERENCES users(userid)
        )
    ''')

    connect.commit()

create_table()


def add_user(fio, age):
    cursor.execute('INSERT INTO users(fio, age) VALUES (?, ?)', (fio, age))
    connect.commit()
    print(f"Пользователь {fio} добавлен")


# add_user('Илья Муромец', 23)
# add_user('John Doe1', 24)
#add_user('John Doe6', 17)
#add_user('John Weak', 25)
#add_user('John Weak1', 23)
#add_user('John Weak2', 22)


def add_grade(userid, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (userid, subject, grade)
    )
    print(f"Оценка добавлена для пользователя с ID {userid}")
    connect.commit()

#add_grade(4, "Физика", 5)
#add_grade(5, "Физика", 3)
#add_grade(6, "Физика", 4)


def get_users_with_grades():
    cursor.execute('''
        SELECT users.fio, grades.subject, grades.grade
        FROM users FULL OUTER JOIN grades ON users.userid = grades.userid
    ''')

    rows = cursor.fetchall()
    for i in rows:
        print(f"FIO: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}")


# get_users_with_grades()


# AVG() – Среднее значение
# MAX() – Максимальное значение
# MIN() – Минимальное значение  COUNT() SUM()

# def get_avg_age():
#     cursor.execute('SELECT SUM(age) FROM users')
#     avg_age = cursor.fetchone()
#
#     print(avg_age)
#
# get_avg_age()



def create_view_old_users():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS old_users AS
        SELECT fio, age
        FROM users
        WHERE age > 25
    ''')
    connect.commit()
    print('Представление old_users создано')

#create_view_old_users()

def get_old_users():
    cursor.execute("""
        SELECT * FROM old_users
    """)

    users = cursor.fetchall()

    print(users)

#get_old_users()


def create_view_physics_grades():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS physics_grades AS
        SELECT subject. grade
        FROM grades
        WHERE subject = "Физика"
    ''')
    connect.commit()
    print('Представление physics_grades создано')

create_view_physics_grades()

def get_physics_grades():
    cursor.execute('''
    SELECT * FROM grades
    ''')
    grades = cursor.fetchall()
    print(grades)

get_physics_grades()
