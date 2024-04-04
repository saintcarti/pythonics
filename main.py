import random 
import string

def generarcontraseña(longitud):
    caracteres= string.ascii_letters + string.digits + string.punctuation
    contrasena=''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

contrasena = generarcontraseña(20)
print(contrasena)