import random 
numero=random.randint(0,99)
intento=int(input("elige un numero del 0 al 99:"))
numero_intento=0
while intento != numero_intento:
    if intento<numero:
        print("demasiado pequeño")
        numero_intento=numero_intento+1
        intento=int(input("elige un numero del 0 al 99:"))
    if intento>numero:
        print("demasiado grande")
        numero_intento=numero_intento+1
        intento=int(input("elige un numero del 0 al 99:"))
    if intento==numero:
        print("acertaste")
        numero_intento=numero_intento+1
        print("numero de intentos"+str(numero_intento))

