menu = "[d] depositar [s] sacar [e] extrato [q] sair =>"

saldo = 0
limitePorSaque = 500
limiteSaques = 3
numeroSaques = 0
extrato = []
encerrar = False

while not encerrar:
    opcao = input(menu)
    if opcao == "d":
        deposito = input("Digite o valor a ser Depositado")
        try:
            deposito = float(deposito.strip())
            if deposito > 0:
                saldo = saldo + deposito
                deposito = (f"Deposito + : R${deposito}")
                extrato.append(deposito)
                print(deposito + " Realizado com Sucesso!")
            else:
                print("Valor inserido invalido, por favor inserir valores inteiros maiores que 0")    
        except:
            print("Erro: Valor inserido não é um numero")
    elif opcao == "s":
        valorSacar = input("insira o valor a ser sacado, limite de 500 por saque")
        try:
            valorSacar = float(valorSacar.strip())
            if valorSacar > saldo:
                print(f"Error: saldo insuficiente seu saldo é: R${saldo}")
            elif valorSacar > limitePorSaque:
                print(f"Error: Seu limite por saque é {limitePorSaque}")
            elif numeroSaques == 3:
                print(f"Error: você já realizou {numeroSaques} saques hoje, tente novamenta amanhã.")
            else:
                print("Saque Realizado Com Sucesso!")
                saldo = saldo - valorSacar
                numeroSaques = numeroSaques + 1
                valorSacar = (f"Saque - : R${valorSacar}")
                extrato.append(valorSacar)
        except:
            print("Erro: Valor inserido não é um numero")
    elif opcao == "e":
        for transacao in extrato:
            print(transacao)
        print(f"Seu Saldo Atual é: R${saldo}")
    elif opcao == "q":
        print("Atendimento Encerrado Tenha um Otimo Dia!")
        encerrar = True
    else:
        print(f"Escolha apenas as opções: {menu}")