
while True:
    print("Доступні дії:")
    print("1-додати")
    print("2-відняти")
    print("3-помножити")
    print("4-поділити")
    print("5-факторіал")
    print("6-1/Х")
    print("7-ступінь")
    print("8-корінь квадратний")
    print("9-вихід")
    a = int(input("Оберіть дію:"))
    if a == 9:
        break
    b = int(input("Введіть число 1:"))

    if a == 1:
        c = int(input("Введіть число 2:"))
        print("Результат:",b+c)

    elif a == 2:
        c = int(input("Введіть число 2:"))
        print("Результат:",b-c)

    elif a == 3:
        c = int(input("Введіть число 2:"))
        print("Результат:",b*c)

    elif a == 4:
        c = int(input("Введіть число 2:"))
        print("Результат:",b/c)

    elif a == 5:
        resultatt = 1
        for i in range(1,1+b):
            resultatt*=i
        print("Результат:",resultatt)
    elif a == 6:
        print("Результат:",1/b)
    elif a == 7:
        c = int(input("Введіть число 2:"))
        print("Результат:",b**c)
    elif a == 8:
        print("Результат:",b**0.5)