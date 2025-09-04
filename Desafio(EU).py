menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUE = 3
LIMITE_DEPOSITO = 10

while True:
    
    opção = input(menu)

    if opção == "1":
        valor = float(input("Informe seu depósito:"))

        excedeu_depositos = numero_depositos > LIMITE_DEPOSITO

        if excedeu_depositos:
            print("Operação inválida! Exceceu o limite de depósitos.")
        
        elif valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação realizada com sucesso!")

        else:
            print("Operação falhou! Valor inválido.")

    elif opção == "2":
        valor = float(input("Informe o valor do seu saque:"))

        excedeu_o_saldo = valor > saldo
        excedeu_o_limite = valor > limite_saque
        excedeu_o_numero_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_o_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_o_limite:
            print("Operação falhou! Ultrapassou o limite de saque.")

        elif excedeu_o_numero_saques:
            print("Operação inválida! Atingiu o número de saques diário.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque efetuado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opção == "3":
        print("\n==============EXTRATO==============")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=====================================")

    elif opção == "0":
        break

    else: 
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")        
    


