import sqlite3

con = sqlite3.connect("dersler.db")

cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT, soyad TEXT, numara INT, puan INT)")
    # con.commit()
    # con.close()

def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES ('Oguzhan', 'Bas', 19060388, 100)")
    con.commit()
    con.close()

tabloolustur()
degerekle()



