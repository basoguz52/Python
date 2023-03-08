import os
os.system("cls")
class Ogrenci():
    def ders_calis(self):
        print("Öğrenci ders çalışıyor")

class Calisan():
    def calis(self):
        print("Personel çalışıyor")

class Yazilimci(Ogrenci,Calisan):
    pass


yazilimci = Yazilimci()

yazilimci.ders_calis()
yazilimci.calis()
