# a = int(input("введіть кілометри:"))
#
# def mili(kilometri):
#     return kilometri* 0.62137
# print(mili(kilometri=a))

# a = int(input("введіть число:"))
#
# def perevirka(number):
#     if number >=1:
#         print("правильне число")
#     elif number <=-1:
#         print("неправильне число")
#     else:
#         print("це нуль")
# perevirka(a)

# a = int(input("введіть місяць:"))
#
# def season(number):
#     if number== 1 or number== 2 or number== 12:
#         print("Zima")
#     elif number== 3 or number== 4 or number== 5:
#         print("vesna")
#     elif number== 6 or number== 7 or number== 8:
#         print("lito")
#     elif number== 9 or number== 10 or number== 11:
#         print("osin")
#     else:
#         print("неправильне число")
# season(a)

a = int(input("введіть число:"))

def perevirka(number):
    if number%2==0:
        print("ура перемога число парне")
    else:
        print("число не парне")
perevirka(a)