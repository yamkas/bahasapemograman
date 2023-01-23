#Function di Python didefinisikan menggunakan keyword "def", seperti ini:
def my_function(arg1, arg2):
    # kode yang ada di ekseskusi
    result = arg1 + arg2
    return result

# memanggil fungsi
result = my_function(13, 3)
print(result) # prints 16

#Rekursif adalah fungsi faktorial seperti ini : 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4)) # prints 24