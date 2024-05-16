# operador AND
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)

print(saque<= limite)

print(saldo>= saque and saque <= limite)

#operador OR

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)

print(saque<= limite)

print(saldo>= saque or saque <= limite)

# operador de Negação
contatos_emergencia = [1,2,3]

print(not 1000 > 500)

not contatos_emergencia

not "saque 1500"

not ""

# AND = para ser True tudo tem que ser True
# OR  = para ser True apenas um tem que ser True


saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(True and True)
print(True and False)
print(True or True)
print(True or False)


saldo1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

saldo2 =(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(saldo1)

print(saldo2)