# a = input("Birinci sayı:")
# b = input("İkinci sayı:")
# c = input("Üçüncü sayı:")
# print(type(a))
# print("sayıların toplamı:",int(a)+int(b)+int(c))
# print(type(a))

print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı:")
soyad = input("Oyuncunun Soyadı:")
takim = input("Oyuncunun Takımı:")

bilgiler = [ad,soyad,takim]

print("Database'e Kaydediliyor...")

#print("Oyuncunun Adı:",ad,"Oyuncunun Soyadı:",soyad,"Oyuncunun Oynadığı Takım:",takim)

print("Oyuncunun Adı:{}\n Oyuncunun Soyadı:{}\n Oyuncunun Oynadığı Takım:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Kaydedildi")