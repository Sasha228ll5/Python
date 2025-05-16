print("Гра-Хто хоче стати мільйонером")
pod50 = True
podzn = True


summa = 0
n_summa=0
print("hello github")


def dost_podskazki():
    print("\t\t\t\t поточна сума:", summa)
    print("\t\t\t\t Доступні підсказки")
    if pod50== True and podzn==True:
        print("\t\t\t\t**************************")
        print("\t\t\t\t50 на 50")
        print("\t\t\t\t**************************")
        print("\t\t\t\tдопомога знавця 50 на 50")
        print("\t\t\t\t**************************")
    elif pod50 == True and podzn == False:
        print("\t\t\t\t**************************")
        print("\t\t\t\t50 на 50")
        print("\t\t\t\t**************************")
    elif pod50 == False and podzn == True:
        print("\t\t\t\t**************************")
        print("\t\t\t\tдопомога знавця 50 на 50")
        print("\t\t\t\t**************************")
    elif pod50 == False and podzn == True:
        print("\t\t\t\t**************************")
        print("\t\t\t\t Доступних пілсказок не має")
        print("\t\t\t\t**************************")


def podskazki(a,b):
    global pod50
    global podzn
    question = input("хочете використати підсказку?")
    if question == "да" or question == "ДА" or question == "Да":
        if pod50 == False and podzn == False:
            print("Доступних підказок немає")
        elif pod50 == True and podzn == True:
            pods = input("50 на 50 або допомога знавця? ")
        elif pod50 == True and podzn == False:
            pods = input("50 на 50?")
        elif pod50 == False and podzn == True:
            pods = input("допомога знавця?")
        if pods == "50 на 50":
            print("1.",a,"\t2.",b)
            pod50 = False
        elif pods == "допомога знавця":
            print("1.",b)
            podzn = False
        else:
            print("Неправильний вибір!")


def question(a,b,a1,a2,a3,a4):
    print("Питання No"+ str(a))
    print(b)
    print('1.',a1,"\t2.",a2)
    print('3.', a3, "\t4.", a4)

def loose(a):
    print("Шкода, але ви програли!")
    print("ваш виграш складає",n_summa,"грн")

Continue = True
Number = 0
begin = input("Хочете почати гру?")
if begin == "Да" or begin == "да" or begin == "ДА":
    dost_podskazki()
    ques = "Який контент складається лише з однієї країни?"
question(1,ques,"Європа","Азія","Африка","Австралія")
podskazki("Європа","Австралія")
answer = input("Введіть відповідь: ")
if answer == "Австралія":
    print("Чудово! Ви дали правильну відповідь!")
    summa = 500
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques = "Де ростуть соняшники?"
    question(2,ques,"на землі","на сонці","на небі","В воді")
    podskazki("На сонці", "На землі")
    answer = input("Дайте відповідь: ")
    if answer == "Наземлі":
        print("Чудово! Ви дали правильну відповідь!")
        summa = 1000
    else:
        Continue = False
    if Continue == False:
        loose(n_summa)
    else:
        dost_podskazki()
        ques = "Яких грошей не буває?"

question(3,ques, "Гривні","Льє", "Долари", "Ліри")
podskazki("Ліри", "Льє")
answer = input("Введіть відповідь: ")
if answer == "Льє":
    print("Чудово! Ви дали правильну відповідь!")
    summa = 2000
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques = "Як називається портрет, який написани з самого себе?"
    question(4, ques, "Самосвал", "Самописка", "Зеркальник", "Автопортрет")
    podskazki ("Самописка", "Автопортрет")
    answer = input("Введіть відповідь: ")
    if answer == "Автопортрет":
        print("Чудово! Ви дали правильну відповідь!")
        summa = 5000
    else:
        Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques = "Як називають безпілотний літальний апарат?"
    question(5,ques, "Дрон", "Махаон", "Десептикон", "Аніон")
    podskazki ("Аніон", "Дрон")
    answer = input("Введіть відповідь: ")
if answer == "Дрон":
    print("Чудово! Ви дали правильну відповідь!")
    summa = 10000
    n_summa = 10000
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques = "В якій грі невикористовують мяч?"
    question(6,ques, "Баскетбол","Теніс", "Бейсбол", "Керлінг")
    podskazki("Теніс", "Керлінг")
    answer = input("Дайте відповідь: ")
if answer == "Керлінг":
    print("Чудово! Ви далиправильну відповідь!")
    summa = 25000

else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques = "Який з цих мостів знаходится в Києві?"
    question (7,ques, "Кримський", "Дарницький", "Невський", "Славутицький")
    podskazki("Невський", "Дарницький")
    answer = input("Введіть відповідь: ")
    if answer == "Дарницький":
        print("Чудово! Ви далиправильну відповідь!")
        summa = 100000
    else:
        Continue = False
    if Continue == False:
        loose(n_summa)
    else:
        dost_podskazki()
        ques = "Хто з цих людей письменник"
        question(8,ques, "Жанклод Вандам", "Клод Моне", "Усейн Болт", "Едгар По")
        podskazki("Клод Моне", "Едгар По")
        answer = input("Дайте відповідь: ")
        if answer == "Едгар По":
            print("Чудово! Ви дали правильну відповідь!")
            summa = 250000
        else:
            Continue = False
    if Continue == False:
        loose(n_summa)