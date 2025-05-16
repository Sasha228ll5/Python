# class Cs2:
#     name = "cs2"
#     size = "50gb"
#     time = 300
#     type = "shoter"
# class GTA5:
#     name = "GTA5"
#     size = "100GB"
#     time = 200
#     type = "shoter"
#     def feedback(self):
#         print("гра дуже пагана 1бал фу ")
# a = GTA5()
# (a.feedback())
# class Game:
#     def __init__(self,name,size,time,type):
#         self.name = name
#         self.size = size
#         self.time = time
#         self.type = type
#     def info(self):
#         print(f"this is {self.name},size is {self.size},type is {self.type}, time is {self.time}")
# game = Game(name = "gta5", size="100gb",type="shoter",time="300")
# game.info()
# game.time = int(input("введіть час:"))
# game.info()

# class Soda:
#     def __init__(self,dobavka = "mandarin"):
#         self.dobavka = dobavka
#
#     def moyadobavka(self):
#         if self.dobavka:
#             print("газировка з",{self.dobavka})
#         else:
#             print("Звичайна газировка")
# soda = Soda()
# soda.moyadobavka()

# class Trianglechecker:
#     def __init__(self,a,b,c):
#         self.b = b
#         self.c = c
#         if a.isdigit() and b.isdigit() and c.isdigit():
#             self.a=int(a)
#             self.b = int(b)
#             self.c = int(c)
#     def perevirkatriygolnika(self):
#         if type(self.a)==str or type(self.b)==str or type(self.c)== str:
#             print("Потрібно вводити лише числа!")
#         elif self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
#             print("ура можна побудувати трикутник!")
#         elif self.a <=0 or self.b <=0 or self.c <=0:
#             print("неможна писати негативні числа!")
#         else:
#             print("неможна побудувати трикутник!")
#
# a = (input("введіть сторона"))
# b = (input("введіть сторона"))
# c = (input("введіть сторона"))
# k = Trianglechecker(a = a,b = b,c = c)
# k.perevirkatriygolnika()

