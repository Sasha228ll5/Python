import random

player1 = 0
player2 = 0
kubik = 0

while True:
    a = input("хочете кинути кубик?Користувач 1 ")
    if a == "Да" or a == "да":
        number1=random.randint(1, 6)
        print("Вам випало число",number1)
        player1 = player1+number1
        print("Користувач1 знаходиться на",player1,"клітинці")
    if player1 >=50:
        print("Вітаю ви виграли!Користувач 1")
        break
    a = input("хочете кинути кубик?Користувач 2 ")
    if a == "Да" or a == "да":
        number2 = random.randint(1, 6)
        print("Вам випало число", number2)
        player2 = player2 + number2
        print("Користувач2 знаходиться на", player2, "клітинці")
    if player2 >= 50:
        print("Вітаю ви виграли!Користувач 2")
        break