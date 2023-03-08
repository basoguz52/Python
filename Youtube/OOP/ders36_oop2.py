class Dusman:
    def __init__(self, isim="Düşman", kalan_can=100, saldiri_gucu=10, mermi_sayisi=10):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def print(self):
        print("Basılıyor...")
        print("İsim:", self.isim, "Kalan Can:", self.kalan_can,
              "Saldırı Gücü:", self.saldiri_gucu, "Mermi Sayısı", self.mermi_sayisi)


# dusman1 = Dusman()
# dusman2 = Dusman()
# print("     -----Düşman 1-----")
# dusman1.print()
# print("     -----Düşman 2-----")
# dusman2.print()

dusman1 = Dusman("Ali", 2000, 50, 50)
dusman2 = Dusman("Veli", 1500, 75, 75)
dusman3 = Dusman()


dusman1.print()
dusman2.print()
dusman3.print()
