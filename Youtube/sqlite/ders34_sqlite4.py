import sqlite3
import random
import time
import datetime

con = sqlite3.connect("dersler.db")

cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS tablo1(zaman REAL, tarih TEXT, anahtarkelime TEXT, deger REAL)")
    # con.commit()
    # con.close()

def rastgeledegerekle():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime = "Python Sqlite3"
    deger = random.randrange(0,10)

    cursor.execute("INSERT INTO tablo1 (zaman, tarih, anahtarkelime, deger) VALUES (?, ?, ?, ?)", (zaman, tarih, anahtarkelime, deger))
    con.commit()

def degerial():
    cursor.execute("SELECT * FROM tablo1 WHERE deger = 2.0")
    data = cursor.fetchall()
    # print("Data Type:",type(data))
    # print("Data:",data)

    for i in data:
        print(i)

def silveguncelle():

    cursor.execute("SELECT * FROM tablo1")

    data = cursor.fetchall()
    print("İlk değerler-----------------")
    for i in data:
        print(i)


    cursor.execute("UPDATE tablo1 SET deger = 99 WHERE deger = 2.0")    


    cursor.execute("SELECT * FROM tablo1")

    data = cursor.fetchall()
    print("Güncellendikten Sonra-----------------")
    for i in data:
        print(i)

def yazdir(tablo):
    cursor.execute("SELECT * FROM {}".format(tablo))
    data = cursor.fetchall()
    for i in data:
        print(i)


def main():
    
    yazdir("tablo1")
    cursor.execute("DELETE FROM tablo1 WHERE deger = 2.0 or deger = 1.0 or deger = 5.0 or deger = 7.0 or deger = 4.0")
    print("----------------------------------")
    yazdir("tablo1")
    
main()


con.close()
print("İşlem Başarılı")

