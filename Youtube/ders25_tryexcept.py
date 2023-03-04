sayi1 = input("1.Sayı:")
sayi2 = input("2.Sayı:")


try:
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    print(sayi1/sayi2)
except (ValueError,ZeroDivisionError):
    print("Bir Hata Oluştu")
# except ZeroDivisionError:
#     print("Bir Sayı 0'a Bölünemez")
