# a = ["буряк","картопля","морква","капуста","цибуля","сіль",]
# # for i in range(len(a)):
# #     print(a[i])
# # for i in a:
# #     print(i)
# # a[4] = "м'ясо"
# # a.insert(1,"перець")
# # a.remove("цибуля")
# # a.pop()
# # a[8] = "meat"
# print(a[-3])

# a = [1,2,3,4,5,6,7,8]
# a.remove(6)
# for i in range(6):
#     a.insert(0,0)
# a.insert(4,100)
# for i in range(19):
#     a.append(55)
# for i in range(19):
#     a.remove(55)
# print(a)

# a = int(input("введіть ціле число:"))
# n = []
# number = 1
# for i in range(a):
#     n.append(number)
#     number+=2
#     print(n)

# a=[9,7,False,'',None,1,0,4]
# for i in a:
#     if i in [False,None,'',0]:
#         a.remove(i)
#     print(a)

# n=[1,10,2,6,9,27,36,22,89,45,90,9,92,100]
# b = []
# summa = 0
# for i in n:
#     if i >=27 and i <=93 and i%2==0:
#         b.append(i)
#         summa+=i
# print(b)
# print(summa)
#порахувати сумму зі списку н

# n=[1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
# b = []
# summadodatni = 0
# skilkidodatni = 0
# for i in n:
#     if i <= 0:
#         summadodatni+=i
# for k in n:
#     if k>=0:
#         skilkidodatni+=1
# b.append(skilkidodatni)
# b.append(summadodatni)
# print(b)
# n = [1,-2,-3,4,-5]
# b = []
# minussperedi = 0
# for i in n:
#     minussperedi=i*-1
#     b.append(minussperedi)
# print(b)

# n = [1,1,2,3,1,2,4,6,6,7,7,2,2,2,1]
# b = []
# for i in n:
#     if i not in b:
#         b.append(i)
# print(b)

# n = ['steam',"school","flick","mouse"]
# b = []
# h = True
# for i in n:
#     if i == "flick":
#         h = not h
#     b.append(h)
# print(b)

# n = [1,10,2,60,80,3,14,63,92,100,122,]
# b = sorted(n)
# print(b[len(b)-2],b[len(b)-1])
#
# #Два найбільші числа