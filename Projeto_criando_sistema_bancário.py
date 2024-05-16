menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
limite_saques_diarios = 3
saques_feitos = 0
valor_saques_diarios = 0

while True:
    print(menu)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito >= 0:
            saldo += valor_deposito
            extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
        else:
            print("Não é possível depositar um valor negativo.")

    elif opcao == "2":
        if saques_feitos < LIMITE_SAQUES and limite_saques_diarios > 0:
            valor_saque = float(input("Digite o valor do saque: "))
            if valor_saque >= 0:
                if valor_saque <= saldo:
                    if valor_saque <= limite:
                        saldo -= valor_saque
                        extrato += f"Saque de R$ {valor_saque:.2f}\n"
                        saques_feitos += 1
                        valor_saques_diarios += valor_saque
                        limite_saques_diarios -= 1
                        print(f"Saque de R$ {valor_saque:.2f} efetuado com sucesso!")
                    else:
                        print("Limite de saque por transação é de R$ 500.00.")
                else:
                    print("Não foi possível realizar o saque. Verifique o saldo.")
            else:
                print("Não é possível sacar um valor negativo.")
        elif saques_feitos >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
        else:
            print("Limite de saque por transação é de R$ 500.00.")

    elif opcao == "3":
        print("*********************** Extrato *****************************")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("*************************************************************")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Escolha novamente.")
