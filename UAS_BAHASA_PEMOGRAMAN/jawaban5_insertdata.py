import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_game"
)

cursor = db.cursor()
sql = "INSERT INTO game (nama_game, jenis_game) VALUES (%s, %s)"
val = ("Assassins Creed", "Stealth")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))