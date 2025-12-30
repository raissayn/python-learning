#ESTRUTURAS CONDICIONAIS E DE REPETIÇÃO

def sacar():
    valor = int(input("digite o valor para saque: "))
    saldo = 500
    if saldo >= valor:
        saldo -= valor 
        print("valor sacado!")
    else:
        print("saldo insuficiente!")
# utiliza elif + else para caso tenha mais condicionais
def depositar():
    valor = int(input("digite o valor para deposito: "))
    saldo = 500
    saldo += valor 
    print("valor depositado!")

opcao = int(input("digite o que você deseja, 1 para saque e 2 para deposito: "))
if opcao == 1:
    sacar()
elif opcao == 2:
    depositar()


#REPETIÇÃO 
# for percorre
numeros = [1, 2, 3, 4]

for n in numeros:
    print(n)

palavra = "Python"

for letra in palavra:
    print(letra)

for i in range(5):
    print(i)
# while faz até a condição não ser falsa
contador = 1

while contador <= 5:
    print(contador)
    contador += 1  # importante para evitar loop infinito

senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso liberado")


#BREAK = interrompe o loop
#Continue = pula p/ próxima iteração