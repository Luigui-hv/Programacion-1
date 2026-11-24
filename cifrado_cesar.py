#CIFRADO CESAR
#HERNANDEZ VILLEGAS LUIS ANTONIO
print("=== CIFRADO CÉSAR ===")

mensaje = input("Escribe el mensaje: ")
desplazamiento = int(input("Ingresa el desplazamiento: "))

alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ"
mensaje_cifrado = ""
mensaje_descifrado = ""

# CIFRADO
for caracter in mensaje:
    if caracter in alfabeto:
        posicion = alfabeto.index(caracter)
        nueva_posicion = (posicion + desplazamiento) % len(alfabeto)
        mensaje_cifrado += alfabeto[nueva_posicion]
    else:
        mensaje_cifrado += caracter

print("\nMensaje cifrado:", mensaje_cifrado)

# DESCIFRADO
for caracter in mensaje_cifrado:
    if caracter in alfabeto:
        posicion = alfabeto.index(caracter)
        nueva_posicion = (posicion - desplazamiento) % len(alfabeto)
        mensaje_descifrado += alfabeto[nueva_posicion]
    else:
        mensaje_descifrado += caracter

print("Mensaje descifrado:", mensaje_descifrado)
