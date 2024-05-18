def sacar(valor):
    saldo = 1000
    if saldo >= valor:
        print("Saque Realizado com sucesso!")
    else:
        print("Saldo Insuficiente!")

# Exemplo de uso:
valor_saque = float(input("Digite o valor que deseja sacar: "))
sacar(valor_saque)
