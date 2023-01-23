#Contoh Function exception handing :
try:
    # kode yang dapat menyebabkan pengecualian
    result = 1 / 0
except ZeroDivisionError:
    print("Tidak dapat dibagi dengan nol.")
finally:
    print("Kode ini akan selalu dieksekusi")