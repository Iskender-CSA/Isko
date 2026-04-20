email = input("Введите email: ")

if "@" in email and "." in email:
    print("Email выглядит правильно")
else:
    print("Email неправильный")