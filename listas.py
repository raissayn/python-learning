frutas = ["laranja", "uva", "melancia"]
print(frutas[0]) #laranja
print(frutas[-1]) #melancia
letras = list("python")
numeros = list(range(10))
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
carro = ["Ferrari", "F8", 1998, 1.0]

#listas aninhadas - lista dentro de listas
matriz = [[1,2],
          [1,3],
          [2,4]]
print(matriz)
#fatiamento
print(carro[:2])
print(carro[::])

#CLASSE LIST
list = []
list.append(10)
print(list)
list2 = list.copy()
print(list2)