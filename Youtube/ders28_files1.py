try:
    dosya = open("yazilim.txt","r")
except FileNotFoundError:
    print("Dosya Bulunamadı")

# read()
# readline()
# readlines()

# print(dosya.readline())
# print(dosya.readline())
print(dosya.readline())

liste = dosya.readlines()
print(liste[1])

dosya.close()