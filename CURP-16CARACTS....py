#Hernández Villegas Luis Antonio 
print("Primeras dieciséis caracteres de la CURP")
print()
print("Este programa saca tu curp ")
nombre1 = input("primer nombre: ").upper()

while len(nombre1) == 0:
    print("ERROR: este campo no puede quedar vacio")
    nombre1 = input("primer nombre: ").upper()


nombre2 = input("segundo nombre(opcional): ").upper()


apellido1 = input("primer apellido: ").upper()

while len(apellido1) == 0:
    print("ERROR: este campo no puede quedar vacio")
    apellido1 = input("primer apellido: ").upper()


apellido2 = input("segundo apellido: ").upper()


print("DATOS LEIDOS")
print("primer nombre = ", nombre1)
print("segundo nombre = ", nombre2)
print("primer apellido = ", apellido1)
print("segundo apellido = ", apellido2)


# Primera letra del apellido

letra1 = apellido1[0]


# PRIMERA VOCAL INTERNA DEL PRIMER APELLIDO

vocal_interna = "X"

for letra in apellido1[1:]:
    if letra in "AEIOU":
        vocal_interna = letra
        break


# PRIMERA LETRA DEL SEGUNDO APELLIDO

if apellido2 != "":
    letra3 = apellido2[0]
else:
    letra3 = "X"


# NOMBRE QUE SE UTILIZARA PARA LA CURP

nombre_curp = nombre1

if nombre1 in ["MARIA", "MA.", "MA", "JOSE", "J", "J."]:
    if nombre2 != "":
        nombre_curp = nombre2


# PRIMERA LETRA DEL NOMBRE

letra4 = nombre_curp[0]


# SI ALGUNA LETRA INICIAL ES Ñ SE CAMBIA POR X

if letra1 == "Ñ":
    letra1 = "X"

if letra3 == "Ñ":
    letra3 = "X"

if letra4 == "Ñ":
    letra4 = "X"


curp = letra1 + vocal_interna + letra3 + letra4

print("")
print("tus iniciales de la CURP son:", curp)

if curp== "LOCA":
    curp = curp[0] +"X" + curp[2]+curp[3]
print("curp corregido",curp.upper())
# FECHA DE NACIMIENTO

# Año

while True:
    try:
        año = int(input("año [1900,2026]: "))

        if año >= 1900 and año <= 2026:
            break

        print("ERROR: se espera un valor en [1900,2026]")

    except ValueError:
        print("ERROR: debes escribir un número entero")


# MES

while True:
    try:
        mes = int(input("mes [1,12]: "))

        if mes >= 1 and mes <= 12:
            break

        print("ERROR: se espera un valor en [1,12]")

    except ValueError:
        print("ERROR: debes escribir un número entero")


# DETERMINAR CUANTOS DIAS TIENE EL MES

match mes:

    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        numdias = 31

    case 2:

        if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
            numdias = 29
        else:
            numdias = 28

    case 4 | 6 | 9 | 11:
        numdias = 30

# DIA

while True:
    try:
        dia = int(input("dia [1," + str(numdias) + "]: "))

        if dia >= 1 and dia <= numdias:
            break

        print("ERROR: se espera un valor entre 1 y", numdias)

    except ValueError:
        print("ERROR: debes escribir un número entero")


# FORMAR FECHA

caracts_año = str(año)[2:]
caracts_mes = str(mes).zfill(2)
caracts_dia = str(dia).zfill(2)

fecha = caracts_año + caracts_mes + caracts_dia

print("fecha para CURP:", fecha)

# SEXO

while True:

    sexo = input("sexo (M/H): ").upper()

    if sexo == "M" or sexo == "H":
        break

    print("ERROR: escribe M para mujer o H para hombre")


# ESTADO DE NACIMIENTO

numEstados = 33

while True:

    try:

        print("")
        print("ESTADOS DE NACIMIENTO")

        print(f"{'1) Aguascalientes':25}", end="\t")
        print(f"{'2) Baja California':25}", end="\t")
        print(f"{'3) Baja California Sur':25}", end="\t")
        print(f"{'4) Campeche':25}")

        print(f"{'5) Coahuila':25}", end="\t")
        print(f"{'6) Colima':25}", end="\t")
        print(f"{'7) Chiapas':25}", end="\t")
        print(f"{'8) Chihuahua':25}")

        print(f"{'9) Ciudad de México':25}", end="\t")
        print(f"{'10) Durango':25}", end="\t")
        print(f"{'11) Guanajuato':25}", end="\t")
        print(f"{'12) Guerrero':25}")

        print(f"{'13) Hidalgo':25}", end="\t")
        print(f"{'14) Jalisco':25}", end="\t")
        print(f"{'15) Estado de México':25}", end="\t")
        print(f"{'16) Michoacán':25}")

        print(f"{'17) Morelos':25}", end="\t")
        print(f"{'18) Nayarit':25}", end="\t")
        print(f"{'19) Nuevo León':25}", end="\t")
        print(f"{'20) Oaxaca':25}")

        print(f"{'21) Puebla':25}", end="\t")
        print(f"{'22) Querétaro':25}", end="\t")
        print(f"{'23) Quintana Roo':25}", end="\t")
        print(f"{'24) San Luis Potosí':25}")

        print(f"{'25) Sinaloa':25}", end="\t")
        print(f"{'26) Sonora':25}", end="\t")
        print(f"{'27) Tabasco':25}", end="\t")
        print(f"{'28) Tlaxcala':25}")

        print(f"{'29) Tamaulipas':25}", end="\t")
        print(f"{'30) Veracruz':25}", end="\t")
        print(f"{'31) Yucatán':25}", end="\t")
        print(f"{'32) Zacatecas':25}")

        print(f"{'33) Nacido en el extranjero':25}")

        print("")

        estado = int(input(f"Selecciona el estado de nacimiento [1,{numEstados}]: "))

        if estado >= 1 and estado <= numEstados:
            break

        print("ERROR: el estado seleccionado no es válido")

    except ValueError:

        print("ERROR: debes escribir un número entero")

# OBTENER SIGLAS DEL ESTADO

match estado:

    case 1:
        nombreEstado = "Aguascalientes"
        siglas = "AS"

    case 2:
        nombreEstado = "Baja California"
        siglas = "BC"

    case 3:
        nombreEstado = "Baja California Sur"
        siglas = "BS"

    case 4:
        nombreEstado = "Campeche"
        siglas = "CC"

    case 5:
        nombreEstado = "Coahuila"
        siglas = "CL"

    case 6:
        nombreEstado = "Colima"
        siglas = "CM"

    case 7:
        nombreEstado = "Chiapas"
        siglas = "CS"

    case 8:
        nombreEstado = "Chihuahua"
        siglas = "CH"

    case 9:
        nombreEstado = "Ciudad de México"
        siglas = "DF"

    case 10:
        nombreEstado = "Durango"
        siglas = "DG"

    case 11:
        nombreEstado = "Guanajuato"
        siglas = "GT"

    case 12:
        nombreEstado = "Guerrero"
        siglas = "GR"

    case 13:
        nombreEstado = "Hidalgo"
        siglas = "HG"

    case 14:
        nombreEstado = "Jalisco"
        siglas = "JC"

    case 15:
        nombreEstado = "Estado de México"
        siglas = "MC"

    case 16:
        nombreEstado = "Michoacán"
        siglas = "MN"

    case 17:
        nombreEstado = "Morelos"
        siglas = "MS"

    case 18:
        nombreEstado = "Nayarit"
        siglas = "NT"

    case 19:
        nombreEstado = "Nuevo León"
        siglas = "NL"

    case 20:
        nombreEstado = "Oaxaca"
        siglas = "OC"

    case 21:
        nombreEstado = "Puebla"
        siglas = "PL"

    case 22:
        nombreEstado = "Querétaro"
        siglas = "QT"

    case 23:
        nombreEstado = "Quintana Roo"
        siglas = "QR"

    case 24:
        nombreEstado = "San Luis Potosí"
        siglas = "SP"

    case 25:
        nombreEstado = "Sinaloa"
        siglas = "SL"

    case 26:
        nombreEstado = "Sonora"
        siglas = "SR"

    case 27:
        nombreEstado = "Tabasco"
        siglas = "TC"

    case 28:
        nombreEstado = "Tlaxcala"
        siglas = "TL"

    case 29:
        nombreEstado = "Tamaulipas"
        siglas = "TS"

    case 30:
        nombreEstado = "Veracruz"
        siglas = "VZ"

    case 31:
        nombreEstado = "Yucatán"
        siglas = "YN"

    case 32:
        nombreEstado = "Zacatecas"
        siglas = "ZS"

    case 33:
        nombreEstado = "Nacido en el extranjero"
        siglas = "NE"


print("")
print("El estado seleccionado es", nombreEstado, ", siglas", siglas)

# PRIMERAS CONSONANTES INTERNAS


def consonante_interna(palabra):

    for letra in palabra[1:]:

        if letra not in "AEIOU":

            if letra == "Ñ":
                return "X"

            else:
                return letra

    return "X"


# CONSONANTE DEL PRIMER APELLIDO

consonante1 = consonante_interna(apellido1)


# CONSONANTE DEL SEGUNDO APELLIDO

if apellido2 == "":
    consonante2 = "X"
else:
    consonante2 = consonante_interna(apellido2)



consonante_nombre = consonante_interna(nombre_curp)

#FINAL


curp = curp + fecha + sexo + siglas

curp = curp + consonante1 + consonante2 + consonante_nombre


print("")
print("CURP:", curp.upper())
print("Numero de caracteres:", len(curp))