import random
a = random.randint(1,20)
attemps = 3
balans = 0
while True:
    j = input("Хочете підсказку? ")
    if j == "yes" or j == "Yes":
        print("Чудово, ви використали підсказку! Вона зменьшує число")
        print("новий діапазон",a-random.randint(1,4),"до",a+random.randint(1,4))
    b = int(input("введіть число щоб угадати: "))

    if a==b:
        print("Вітаю ви вгадали")
        if attemps == 3:
            print("Вітаю у вас 500 очків")
            balans += 500
        elif attemps == 2:
            print("Вітаю у вас 300 очків")
            balans += 300
        else:
            print("Вітаю у вас 100 очків")
            balans +=100
        l = input("хочете відвідати магазин?")
        if l == "yes" or "Yes":
            p = input("Добре! Бажаєти в нас купити одне життя за 300 баксів?")
            if p == "yes" or "Yes":
                if balans<300:
                    print("у вас нема грошей")
                    break
                attemps +=1
    else:
        print("Ви не вгадали:( спробуйте ще раз")
        attemps-=1


    if attemps == 0:
        print("вибачте ви програли комп'ютеру")
        print("Число було загадано",a)
        break