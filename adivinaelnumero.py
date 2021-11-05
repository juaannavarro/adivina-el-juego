import random 
    
numero=random.randint(0,99)
print("Introduzca el numero a adivinar", numero)
while True:
    numero=input("Introduzca un numero entre 0 y 99 incluidos")

    try:
        numero=int(numero)
    except:
        pass
    else:
        if 0<= numero <= 99:
            break