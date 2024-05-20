# Exemplo_1

conta_normal = False
conta_universitaria = False
saldo = 2000.0
saque = 500
cheque_especial = 450
# Adicione um input para escolher o tipo de conta
tipo_conta = int(input(
    "Informe o tipo de conta: \n [1] Conta Normal \n [2] Conta Universitária: "))

if tipo_conta == 1:
    conta_normal = True
    cheque_especial = float(input("Informe o valor do cheque especial: "))
elif tipo_conta == 2:
    conta_universitaria = True


opcao = int(input("Informe uma opção[1] para saque \n [2] para extrato: "))

if opcao == 1:
    saque = float(input("Informe o valor do saque:"))
    if saldo >= saque:
        saldo -= saque
        print("Saque Realizado com sucesso!")
        print("Retire seu Dinheiro")
    else:
        print("Saldo Insuficiente!")

elif opcao == 2:
    print("Exibindo Extrato")
    print("Saldo Atual: ", saldo)

else:
    SystemExit("Opção Inválida")


if conta_normal:
    if saldo >= saque:
        print("Saque Realizado com sucesso!")

    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque Realizado com sucesso!")
