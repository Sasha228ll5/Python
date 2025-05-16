#a = int(input("введіть число "))

#if a > 0:
    #a +=1
#elif a < 0:
    #a -=2
#else:
    #a = 10
#print("Ось результат дій", a)

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
posit_chi = 0
negat_chi = 0

if a > 0:
    posit_chi += 1
elif a < 0:
    negat_chi += 1
if b > 0:
    posit_chi += 1
elif b < 0:
    negat_chi += 1
if c > 0:
    posit_chi += 1
elif c < 0:
    negat_chi += 1
print("Кількість позитивних чисел:",posit_chi)
print("Кількість негативних чисел:",negat_chi)

