# a = "Привіт"
# print(a[3:-1])

# a = ord('А')
# print(a)

# a= chr(24)
# print(a)

# phone = "+1-234-567-89-10"
# b = phone.replace("-","")
# print(b)i
# phone2=""
# for i in phone:
#     if i=="-":
#         phone2+=" "
#     else:
#         phone2+=i
# print(phone2)

# a = "aAAABBBBbbbbcccC12121"
# if a.isdigit():
#     print("воно лише з цифр")
# elif a.isalpha():
#     print("Наш рядок складається тільки з букв")
#     if a.isupper():
#         print("складається з великих букв")
#     elif a.islower():
#         print("складається з маленьких букв")
# else:
#     print("Складається із букв і цифр")

# a = "abacdafabaccooabacabacqabac"
# c = 0
# while True:
#     b = a.find("abac")
#     if b ==-1:
#         break
#     else:
#         a = a[b+4:]
#         c+=1
# print(c)
# print(a.count("abac"))

# a = "Фалака це улюблене катування середньовіччя. Покарати могли будь-когоударами по п'ятах."
# c = 0
# b = a.split()
# for i in b:
#     if i.count("а") ==3:
#         c+=1
# print(c)

# a = "avfvhfukfofnbbnfffbmf"
# # for i in a:
# #     if a == "f":
# b = a.replace("f","ff")
# print(b)

# a = "птахи пхаетон пхінянь про"
# b = 0
# for i in a.split():
#     if i.startswith("п"):
#         b += 1
# print(b)