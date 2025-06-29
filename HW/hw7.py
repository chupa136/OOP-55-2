import sqlite3

connect = sqlite3.connect("students.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students(
    name VARCHAR NOT NULL,
    surname VARCHAR NOT NULL,
    year INTEGER NOT NULL
)""")

def add_student(name, surname, year):
    cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (name, surname, year))
    connect.commit()
    print(f"student insert!!!")

#add_student("Kolya", "Sazhin", 2005)

def get_all_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print(f" All students:{students}")

get_all_students()

def update_student(name, surname, year, rowid):
    cursor.execute("""UPDATE students SET name=?, surname=?, year=? WHERE rowid=?""",
                   (name, surname, year, rowid))
    print(f"student {rowid} update!!!")
    connect.commit()

#update_student("Damir", "Toktosunov", 2008, 1)

def delete_student(rowid):
    cursor.execute("DELETE FROM students WHERE rowid=?", (rowid,))
    print(f"student {rowid} delete!!!")
    connect.commit()

delete_student(3)


