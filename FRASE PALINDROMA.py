cadena = input("Ingrese una frase: ")
cadena_sin_espacios = cadena.replace(" ", "")
cadena_invertida = ""
#cadena_mayusculas = cadena.title()



print("")
print("Frase original: " ,cadena)
print("")
#print("Frase con mayusculas: " ,cadena_mayusculas)
print("Frase sin espacios: " ,cadena_sin_espacios)


for i in range(len(cadena_sin_espacios) -1, -1, -1):
    cadena_invertida += cadena_sin_espacios[i]
    
print("Frase invertida: ",cadena_invertida)

if cadena_sin_espacios == cadena_invertida:
    print("La palabra es palindroma")
else:
    print("La palabra no es palindroma")