with open("yazilim.txt","r") as dosya:
    dosya.seek(10)
    str1 = dosya.read(5)
    dosya.seek(15)
    str2 = dosya.read(5)
    
    print(str1+str2)