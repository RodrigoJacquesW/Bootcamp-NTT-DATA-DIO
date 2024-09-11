print("\n===BEM VINDO===")
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3
deposito = 0
saque= 0

while True:

    opcao = input(menu)

    if opcao =="d":
        print("Depósito")
        deposito = int(input("Digite o valor que você quer depositar: "))
        if deposito < 0:
                print("Você não pode depositar valores negativos\n")
        if deposito > 0:
                saldo += deposito
                print("Seu saldo é:",saldo,"R$")
                extrato += str(f"Depósito:{deposito:.2f} R$\n")
    elif opcao =="s":
        print("Sacar")
        saque = int(input("Quanto você quer sacar: "))
        if saque > limite:
            print("Você não pode sacar acima de 500 R$")
        elif numero_saques > LIMITE_SAQUES:
            print("Você atingiu seu limite diário de saques.")
        elif saque > saldo:
            print("Você não tem dinheiro suficiente para essa transação.")
            print("Você tem apenas R$ ",saldo," Na conta") 
        else:
            saldo -= saque
            numero_saques += 1
            print("Você sacou R$ ", saque)   
            print("Seu saldo é: ", saldo) 
            extrato += str(f"Saque:{saque:.2f} R$\n")
    elif opcao =="e":
        print("Extrato\n")
        print("Suas transições:\n")
        print(extrato)
        print(f"Seu saldo é:{saldo:.2f}")

    elif opcao =="q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    