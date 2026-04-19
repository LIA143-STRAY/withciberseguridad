import random
import string
while True:
     try:
         longitud = int(input("Cuantos caracteres quieres: "))
         if longitud < 6:
              print("Muy corta, intenta de nuevo")
         else:
              break
     except:
         print("Por favor ingresa un numero valido")
usar_simbolos = input("Quieres simbolos? (s/n): ")
caracteres = string.ascii_letters + string.digits
if usar_simbolos.lower() == "s":
      caracteres += string.punctuation
password = ""
for i in range(longitud):
      password += random.choice(caracteres)
print("Tu contraseña es:", password)
