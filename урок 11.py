# def a (a,b=11):
#     return a-b
# result = a (99)
# result1 = a (2,8)
# print(result1+result)
a = int(input("введіть число  1 "))
b = int(input("введіть число  2 "))
def perimetr(number1,number2):
    return (number1+number2)*2
#print(perimetr(number1=a,number2=b))
def plosha(number1,number2):
    return number1*number2
print(plosha(number1=a,number2=b))