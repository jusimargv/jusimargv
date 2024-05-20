for numero  in range(0,11):
    print(numero, end="  ")
print()
print("exibindo a tabuada do 5")
for numero in range(0,51,5):
    print(numero, end="  ")

print()
print("Exemplo while  ")
# Exemplo while
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] extrato \n[0]  Sair \n:"))
    
    if opcao == 1:
        print("Sacando ...")
        
    elif opcao == 2:
        print("Exibindo o Extrato")    