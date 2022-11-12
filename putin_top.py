a = "Reyzor"
b = "8642"

name = input("Введите логин: ")
if name == a:
    print("Welcome,BLIN")

password = input("Введите пароль: ")
if password == b:
    print(f"Здравствуйте,{name}")
    input_text = input("Чем могу помочь?: ")
    while input_text != "стоп":
        if input_text == "Как дела?":
            print("القاتل الملكة: لدغة الغبار")
            input_text = input("Введите новое сообщение: ")
        elif input_text == "Как сегодня холодно?":
            print("Сегодня -15, посидите сегодня дома")
            input_text = input("Введите новое сообщение: ")
        elif input_text == "Приготовь чай пожалуйста":
            print(f"{name} приготовь сам! Руки ноги есть,и в чем проблема?")
            input_text = input("Введите новое сообщение: ")
        elif input_text == "Начинается игра, я открываю":
            print("тетрадь смерти, запишу там 5 никнеймов, все уmrut от REQVIEMа")
            input_text = input("Введите новое сообщение: ")
        else:
            print("не знаю такой команды :_(")
        input_text = input("Введите новое сообщение: ")

    else:
        print("Неверный пароль")
else:
    print("Такого логина нет")
