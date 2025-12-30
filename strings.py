nome = "Raissa"
print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   TESTE  "
print(texto.strip()+ ".")
print(texto.lstrip() + ".")
print(texto.rstrip())

menu = "olá"
print(menu.center(10,"#"))
print(".".join(menu))

# interpolar variáveis em strings
# old style % 
nome = "Raissa"
idade = 20

print("Olá, me chamo %s, tenho %d anos." % (nome,idade))
# %s = string, %d = int

#método format
print("Olá, me chamo {}, minha idade é {}.".format(nome,idade))

#f-string
print(f"Olá, me chamo {nome}, eu tenho {idade} anos.")

#formatar strings com f-string = .2fy

print(nome[:2])
print(nome[2:])
print(f"""
      Olá meu nome é {nome},
      tenho {idade} anos.""")