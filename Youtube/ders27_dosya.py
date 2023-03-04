dosya1 = open("yazilim.txt","w")#dosya yoksa yeni oluşturur ve yazar, varsa eski dosyayı siler yeni dosyaya yazar
dosya2 = open("deneme.txt","r")#dosyayı okuma moduna açıyor
dosya3 = open("bilisim.txt","a")#olan dosya içindeki bilgileri değiştirmemize olanak sağlıyor,dosya yoksa yeni dosyaya yazar

dosya3.write("123")