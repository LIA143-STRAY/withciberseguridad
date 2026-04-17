import random
import string
longitud = int(input("cuantos caracteres quieres: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
password = " "
for i in range(longitud): password += random.choice(caracteres)
print("Tu contraseña es:", password)
