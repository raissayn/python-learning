#  bootcamp DIO - Introdução a phyton
print("Olá mundo!")
print(1+10)
age =13
name = 'Giovana'
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

# phyton não tem constantes! - convensão: variável nome todo em MAIÚSCULO!
AMOUNT = 12.3
print(AMOUNT)

#conversão de tipos
preco = 10.30
preco= int(preco)
print(preco)
print(int(100))

prazo = 10
print(str(prazo))
texto = f"prazo: {prazo} meses"
print(texto)

#função entrada e saída
# lendo com input
# saída com print
nome = input("Informe o seu nome:")
idade = input("Informe a sua idade:")
print(nome, idade, end=" ...\n")
print(f"meu nome é  {nome}, e minha idade é {idade} anos",end=" .")