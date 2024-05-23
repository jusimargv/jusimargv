menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITES_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito:"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            
        else:
            print("Operação falhou! O valor informado é inválido.")    
        

    elif opcao == "2":
        valor = float(input("Informe o valor do Saque:"))
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_limite_saques = numeros_saques >= LIMITES_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite de saque diário.")
            
        elif excedeu_limite_saques:
            print("Operação falhou! Você excedeu o limite de saques diários.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_saques += 1    
            
        else:
            print("Operação falhou! O valor informado é inválido.")    

    elif opcao == "3":
        print("\n================EXTRATO==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Opção inválida, por favor selecione novamente um operação valida.")
