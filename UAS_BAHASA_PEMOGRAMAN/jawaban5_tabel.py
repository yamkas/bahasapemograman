import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_game"
)

cursor = db.cursor()
sql = """CREATE TABLE game (
   nama_game VARCHAR(255), 
   batas_usia INT AUTO_INCREMENT PRIMARY KEY,    
   jenis_game VARCHAR(255)
)
"""
cursor.execute(sql)

print("Tabel game barhasil dibuat!")