import random


class Dusman:
    def __init__(self, isim="Düşman", kalan_can=500, saldiri_gucu=10, mermi_sayisi=5):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim, "Saldırıyor")
        harcanan_mermi = random.randrange(0, 10)
        print("Harcanan Mermi:", harcanan_mermi)
        self.mermi_sayisi -= harcanan_mermi
        print("Kalan Mermi:", self.mermi_sayisi)

        return (harcanan_mermi, self.saldiri_gucu)

    def saldiriya_ugra(self, harcanan_mermi, saldiri_gucu):
        print("Vuruldum")
        self.kalan_can -= harcanan_mermi * saldiri_gucu

    def mermi_bitti_mi(self):
        if self.mermi_sayisi <= 0:
            print(self.isim, " Konuşuyor: Mermim Bitti")
            return True
        return False

    def hayatta_mi(self):
        if self.kalan_can <= 0:
            print("Ölü...")
        else:
            print("Yaşıyor")

    def print(self):
        print("Basılıyor...")
        print("İsim:", self.isim, "Kalan Can:", self.kalan_can,
              "Saldırı Gücü:", self.saldiri_gucu, "Mermi Sayısı:", self.mermi_sayisi)


def main():
    dusmanlar = []

    for i in range(10):
        rastgele_can = random.randrange(100, 200)
        rastgele_saldiri_gucu = random.randrange(10, 20)
        rastgele_mermi = random.randrange(20, 30)
        yenidusman = Dusman("Düşman " + str(i+1), rastgele_can, rastgele_saldiri_gucu, rastgele_mermi)
        dusmanlar.append(yenidusman)

    for dusman in dusmanlar:
        dusman.print()

main()
