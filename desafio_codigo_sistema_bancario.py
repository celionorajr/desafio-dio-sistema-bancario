menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
        elif valor > limite:
            print("Valor de saque excede o limite permitido.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n=== Extrato Bancário ===")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=======================\n")

    elif opcao == "q":
        print("Saindo do sistema bancário. Até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
