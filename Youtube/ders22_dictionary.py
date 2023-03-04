sozluk = {"Python":"Güzel Bir Dil","Php":"Script Dili","C":"Compile Edilen Bir Dil"}

#print("Tip:",type(sozluk))

# print(sozluk["Python"])

# for i in sozluk.items():
#     print(i)

# for i in sozluk.items():
#     print(i[0],i[1])

# for i,j in sozluk.items():
#     print(i,j)

dersler = {"Ahmet":["Veri Tabanı","İşletim Sistemleri"],"Oğuz":["Script","OOP"],"Mehmet":"Lineer Cebir"}

isim = input("İsim Giriniz:")
print("{} aldığı dersler".format(isim))

for i in dersler[isim]:
    print(i)

for i,h in dersler.items():
    if i == "Ahmet":
        print(h)
