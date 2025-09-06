def menu():
    menu = """\n
==============MENU=============
    [1] Depositar
    [2] Sacar
    [3] Novo usuário
    [4] Criar conta
    [5] Extrato
    [0] Sair

=>"""

    return input(menu)

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Operação realizada com sucesso!")

    else:
        print("Operação falhou! Valor inválido.")

    return saldo, extrato

def sacar(*, valor, saldo, extrato, limite_saque, numero_saques,limite):
    excedeu_saldo = valor > saldo
    excedeu_numero_saques = numero_saques >= limite_saque
    excedeu_limite_saques = valor > limite

    if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente.")

    elif excedeu_limite_saques:
        print("Operação falhou! Ultrapassou o limite de saque.")

    elif excedeu_numero_saques:
        print("Operação inválida! Atingiu o número de saques diário.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("Saque efetuado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF:")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (Somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def exibir_extrato( saldo, /,*, extrato,):
    print("\n==============EXTRATO==============")
    print("Não foram realizadas movimentações."if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("=====================================")

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas =[]
    
    while True:
        opção = menu()
    
        if opção == "1":
            valor = float(input("Informe seu depósito:"))
            saldo, extrato = depositar(valor,saldo,extrato)

        elif opção == "2":
            valor = float(input("Informe o valor do seu saque:"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUE,)
            
        elif opção == "3":
            criar_usuario(usuarios)


        elif opção == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opção == "5":
            exibir_extrato(saldo, extrato=extrato)

        elif opção == "0":
            break

        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")  

main()