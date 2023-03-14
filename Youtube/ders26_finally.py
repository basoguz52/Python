try:
    dosya1 = open("deneme.txt",'w',encoding="utf-8")
    dosya2 = open("sa")
    
except:
    print("Dosya Bulunamadı")
finally:
    print(1)
    dosya1.write("Deneme Yazısı")
    dosya1.close()


print("Main Çalıştı")

# dosya1 = open("deneme.txt",'w')
# dosya2 = open("sa")
# print(2)