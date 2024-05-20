# Receba um número do teclado e exiba os 2 números seguintes

a = int(input("Informe um número inteiro:"))
print(a)

a += 1
print(a)

a += 1
print(a)

# Exemplo FOR

texto = input("Informe um texto")
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:        

    print()