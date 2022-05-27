# Ejercicio 1
x = 1
sumando = 0
while x <= 100:
    if x%2==0:
        sumando = sumando + x
    
    x = x + 1

print("La suma de los numeros de 1-100:",sumando)


# Ejercicio 2

print("Ingresar numero limite")
limite = int(input())
xx = 1
suma = 0
while xx <= limite:
    suma = suma + xx
    print("La suma de los numeros de 1-", limite, ":",suma)
    xx = xx + 1

# Ejercicio 3
num=0
size=0
i=0
contador=0
print("Ingrese cantidad de numeros a ingresar")
size=int(input())

while i < size:
    print("Ingrese numero")
    num=int(input())
    if num>0:
        contador=contador+1
    else:
     print("El numero es negativo, fin del programa")
     i=size
    i=i+1


print("El numeros positivos son:",contador)



# Ejercicio 4
num=10
i=0
while i<=num:
    i=i+1
    print("*"*(i))
    
# Ejercicio 5

while True:
    print("Menú de opciones") 
    print ("1. Calcular diametro")
    print ("2. Calcular perimetro")
    print ("3. Calcular area")
    print ("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        radio = int(input("Ingrese el radio: "))
        diametro = radio * 2
        print ("El diametro es: ", diametro)
    elif opcion == 2:
        radio = int(input("Ingrese el radio: "))
        perimetro = radio * 3.14 * 2
        print ("El perimetro es: ", perimetro)
    elif opcion == 3:
        radio = int(input("Ingrese el radio: "))
        area = radio * 3.14 * 2
        print ("El area es: ", area)
    elif opcion == 4:
        break
    else:
        print ("Opción incorrecta")
print ("Fin del programa")


