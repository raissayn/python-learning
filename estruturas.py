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
