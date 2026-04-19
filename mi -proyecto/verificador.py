print("INICIO")
import string

while True:
    password = input("Ingresa tu contraseña (o escribe salir): ")
    
    if password.lower() == "salir":
        break
    
    print("Analizando...")
    
    tiene_mayus = False
    tiene_num = False
    tiene_simbolo = False
    
    for c in password:
        if c in string.ascii_uppercase:
            tiene_mayus = True
        if c in string.digits:
            tiene_num = True
        if c in string.punctuation:
            tiene_simbolo = True
        
    if len(password) < 8:
        print("Contraseña debil: muy corta")
    elif not tiene_mayus:
        print("Falta una letra mayuscula")
    elif not tiene_num:
        print("Falta un numero")
    elif not tiene_num:
       print("Falta un simbolo")
    else:
       print("Contraseña fuerte💪😏")
    