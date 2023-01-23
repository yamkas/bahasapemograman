import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_game"
)


def insert_data(db):
    nama_game = input("Masukan nama: ")
    jenis_game  = input("Masukan jenis: ")
    val = (nama_game, jenis_game)
    cursor = db.cursor()
    sql = "INSERT INTO game (nama_game, jenis_game) VALUES (%s. %s)"
    cursor.execute(sql, val)
    print("{} data berhasil disimpan".format(cursor.rowcount)) 


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM game"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  batas_usia = input("pilih batas usia> ")
  sql = "DELETE FROM game WHERE batas_usia=%s"
  val = (batas_usia,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Hapus Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")  

#clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    delete_data(db)
  elif menu == "0":
    delete_data(db)
 
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)