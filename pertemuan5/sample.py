# contoh cara mengoding yang sederhana
def tambah():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    c = a+b
    print(c)
def kurang():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    c = a-b
    print(c)
def perkalian():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    c = a*b    
    print(c)

def pilihan():
    print("1. +")
    print("2. -")
    print("3. *")
    print("exit")

while True:
    pilihan()   
    pil=int(input("pilihan : ")) 
    if pil==1:
       tambah()
    elif pil==2:
       kurang() 
    elif pil==3:
       perkalian()    
    else :
        break    