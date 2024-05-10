# **convertendo Inteiro para float** 
preco = 10
print("Preço:", preco)

preco = float(preco)
print("Preço:", preco)

preco = 10 / 2
print("Preço:", preco)

# convertendo de Float para Inteiro
preco = 10.30
print("Preço:", preco)

preco = 10.30
print("Preço:", round(preco))

preco = int(preco)
print("Preço:", preco)

# Conversão por divisão
preco = 10
print("Preço:", preco)

print("Preço:", preco / 2)

print("Preço:", preco // 2)

# Numérico para string

preco = 10.50
idade =28

print("Preço:", str( preco))

print("Idade:", str( idade))

texto = f"Idade: {idade}  Preço: {preco}"

print(texto)

# **convertendo string para Número**

preco ="10.50"
idade ="28"

print("Preço:", float(preco))

print("Idade:", int(idade))

# Erro de Conversão

preco ="Python"

#print(float(preco)) # erro na conversão de uma string que não contém números.

# Tipo de Dados
preco = 10.50
idade = str(preco)

print("Tipo float:",type(preco))

print("Tipo String:", type(idade))

preco = 10

print("Tipo Inteiro:", type(preco))