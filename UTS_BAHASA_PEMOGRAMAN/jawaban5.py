pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
    Yamkas Coffe
    List Menu Minuman Kopi 
 
    ==============================
    A. Kopi VanillaLate : Rp 11.000
    B. Kopi Americano : Rp 12.000
    ==============================
    """)
    pesan=str(input("Masukan kopi yang ingin di pesan ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama= "Kopi VanillaLatte"
        harga=(11000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "b":
        listnama= "Kopi Americano"
        harga = (12000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silakan masukan menu yang tersedia Y/N =")
 
    print("--------------------------")
    print("Yamkas Coffe")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")
