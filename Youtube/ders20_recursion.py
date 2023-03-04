"""
RECURSİON

1.BİTİŞ DURUMU TANIMLAMAK GEREKLİ FONKSİYONUN SONSUZA KADAR KENDİNİ ÇAĞIRMAMASI İÇİN
2.FONKSİYONUN BELLİ ŞARTLARDA KENDİNİ ÇAĞIRMASI GEREKLİ

def topla(liste):
    toplam = 0
    for i in liste:
        toplam += i
    return toplam

print(topla([1,2,3,4,5]))


"""


def topla(liste):
    if(len(liste) == 0):
        return 0
    else:
        return liste[0] + (topla(liste[1:]))
    

a = [1,2,3,4]
print(topla([1,2,3,4]))