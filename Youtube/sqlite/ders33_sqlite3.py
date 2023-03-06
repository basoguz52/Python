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
    cursor.execute("SELECT * FROM tablo1 WHERE deger = 7.0")
    data = cursor.fetchall()
    print("Data Type:",type(data))
    # print("Data:",data)

    for i in data:
        print(i)



def main():
    degerial()    
    
main()



print("İşlem Başarılı")

