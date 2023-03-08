import os
os.system("cls")
class Calisan():
    def __init__(self, isim, maas, departman):
        print("Çalışan Sınıfının Yapıcı Fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Çalışan sınıfının bilgileri gösteriliyor.")
        print("İsim:", self.isim, "Maaş:", self.maas,
              "Departman:", self.departman)

    def maasa_zam_yap(self, zam_miktari):
        print("Maaşa Zam Yapıldı")
        self.maas += zam_miktari

    def departman_degistir(self, yeni_departman):
        print("Departman Değiştiriliyor...")
        self.departman = yeni_departman


class Yonetici(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):
        print("Yönetici Sınıfının Yapıcı Fonskiyonu")
        super().__init__(isim, maas, departman)
        self.kisi_sayisi = kisi_sayisi
        

    def bilgileri_goster(self):
        print("Yönetici sınıfının bilgileri gösteriliyor")
        print("İsim:", self.isim, "Maaş:", self.maas,
              "Departman:", self.departman,"Kişi Sayısı:",self.kisi_sayisi)
    
    def kisi_sayisi_arttir(self,arttir):
        print("Kişi sayısı arttırılıyor.")
        self.kisi_sayisi += arttir

# calisan = Calisan("Mehmet Baltacı", 2500, "İnsan Kaynakları")
# calisan.bilgileri_goster()

yonetici = Yonetici("Mehmet Baltacı", 2500, "İnsan Kaynakları", 20)

yonetici.bilgileri_goster()
yonetici.kisi_sayisi_arttir(20)
yonetici.bilgileri_goster()