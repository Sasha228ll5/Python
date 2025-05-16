#Language = "English"
#time = 'morning'

#if Language == "English":
    #print("English")
    #if time == "morning":
        #print("good morning")
    #else:
        #print("Good Afternoon")
#else:
    #print("incorrect language")

#correct_login = "Sanok"
#correct_password = "12345678"

#login = input("Введіть логін: ")
#if login == correct_login:
    #password = input("введіть пароль: ")
    #if password == correct_password:
        #print("Доступ  відкрито")
    #else:
        #print("Невірний пароль, повторіть ще раз")
#else:
    #print("логін не існує")

#a = int(input("введыть відстань в км:"))

#if a>=30:
    #if a<=40:
        #print("попав в ціль")
    #else:
        #print("переліт")
#else:
    #print("недоліт")

name = int(input("Як тебе звати, людина? "))
print("Привіт", name, ". Чим будемо займатися?")
choice = input("Додавати та множити або вчити прислів'я та приказки? ")
if choice == "Додавати та множити":
    choice2 = input("Обери дію: + або * ")
    if choice2 == "+":
        a = int(input("Введи число 1: "))
        b = int(input("Введи число 2: "))
        print("Сума чисел:", a + b)
    elif choice2 == "*":
        a = int(input("Введи число 1: "))
        b = int(input("Введи число 2: "))
        print("Добуток чисел:", a * b)
    else:
        print("Я можу тільки додавати та множити!")
elif choice == "Вчити прислів'я та приказки":
    choice2 = input("Вивчимо прислів'я? (так/ні) ")
    if choice2 == "так":
        print("Під лежачий камінь вода не тече!")
    elif choice2 == "ні":
        print("Добре, тоді вивчимо приказки:")
        print("Блищить як новий, тріщить як сорока!")
    else:
        print("Невідома відповідь!")
else:
    print("Я не вмію цього робити. Вибач,", name)