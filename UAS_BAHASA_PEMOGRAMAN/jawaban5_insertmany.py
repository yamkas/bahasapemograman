import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_game"
)

cursor = db.cursor()
sql = "INSERT INTO game (nama_game, jenis_game) VALUES (%s, %s)"
values = [
    ("PSO2", "MMORPG"),
    ("Point Blank", "FPS"),
    ("Nioh", "Souls"),
    ("Dead Cell", "Indie"),
    ("Asphalt", "Racing")
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data yang ditambahkan lebih banyak".format(len(values)))