class Dusman:
    kalan_can = 3
    
    def saldir(self):
        print("Hücum")
        self.kalan_can -= 1
    
    def hayatta_mi(self):
        if self.kalan_can <= 0:
            print("Öldü")
        else:
            print("Kalan can:", self.kalan_can)

dusman1 = Dusman()
dusman2 = Dusman()

dusman1.saldir()
dusman1.saldir()
dusman1.hayatta_mi()

dusman2.saldir()
dusman2.saldir()
dusman2.saldir()
dusman2.hayatta_mi()