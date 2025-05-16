#def first_func(a,b, c=13):
    #print("it's a",a)
    #print("c is", c)
    #return a+b+c

#print(first_func(a=15,c=99))

print("Гра-Хто хоче стати мільйонером")
pod50 = True
podzn = True

summa = 0
n_summa=0

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