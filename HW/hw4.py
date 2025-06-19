

def square_result(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs) ** 2
            return result
        return wrapper

#Написал *args, **kwargs, чтобы он принимал любое количество аргументов

@square_result
def add (a, b, c, g):
   return a + b - c * g

print(add(2, 3, 1, 6))


def check_user(user):
    def decarator(func):
        def wrapper():
            if user == "admin":
                print(f"You have admin permission")
                func()
            else:
                print(False)
        return wrapper
    return decarator


@check_user("admin")
def delete_database():
    print("База данных удалена!")


@check_user("guest")
def delete_logs():
    print("Логи удалены!")

delete_database()
delete_logs()