frutas = ["laranja", "maca", "uva"]
print(frutas)
print(frutas[0])
print(frutas[2])
frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

lista = ["P", "y", "t", "h", "o", "n"]


print(lista[:2])
print(lista[2:])
print(lista[::])
print(lista[0:3:2])
print(lista[::-1])

carros = ("celta", "palio", "astra")
for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")


numeros = [10, 25, 12, 32, 14, 52, 3, 2, 65, 85,
           74, 15, 24, 23, 63, 96, 8, 5, 21, 4, 7, 41]

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)  # type: ignore
        print(numero)


numeros = [10, 25, 12, 32, 14, 52, 3, 2, 65, 85,
           74, 15, 24, 23, 63, 96, 8, 5, 21, 4, 7, 41]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)



numeros=[10,25,12,32,14,52,3,2,65,85,74,15,24,23,63,96,8,5,21,4,7,41]

quadrado=[]

for numero in numeros:
    quadrado.append(numero**2)
    print(quadrado)

numeros=[10,25,12,32,14,52,3,2,65,85,74,15,24,23,63,96,8,5,21,4,7,41]
quadrado=[numero **2 for numero in numeros]
print(quadrado)

lista2= []

lista2.append(1)
lista2.append("Python")
lista2.append([45,25,23])

print(lista2)

lista3 = lista2.copy()

print(id(lista3), id(lista2))

lista3[0] = 2
print(lista3)

cores =[ "Azul", "amarelo", "purple", "roxo", "amarelo","Azul", "amarelo"]

print(cores.count("Azul")) # [].COUNT
print(cores.count("amarelo"))
print(cores.count("roxo"))

car=["celta", "palio", "astra"]

print(car)

car.extend(["Camry","BMW 328 "]) #[].EXTEND

print(car)

print(car.index("Camry")) #[].INDEX
print(car.index("celta"))


car.pop(3)
car.pop(2)
car.pop(1)
car.pop(0)

print(car)

car.clear()

print(car)

car=["corolla","fusion","civic"]
print(car)
car.append("cerato")
print(car)
car.extend(["A5","A4"])
print(car)
print(car.index("civic"))
car.pop(1)
print(car)
car.insert(1,"Audi")
car.insert(5,"pomarola")
print(car)
car.reverse()
print(car)
car.sort(reverse=True)
print(car)
car.sort(key=lambda x: len(x))
print(car)
car.sort(key=lambda x: len(x), reverse=True)

print(car)

sorted(car,key=lambda x: len(x))
print(car)
sorted(car, key=lambda x: len(x), reverse=True)
print(car)