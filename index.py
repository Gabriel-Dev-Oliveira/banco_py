saldo = 1000.0

def consultar_saldo():
    print(f"O seu saldo é: {saldo:.2f}")
    

def deposito():
    global saldo
    valor_deposito = float(input("Digite o valor do deposito: R$"))
    
    saldo += valor_deposito
    print(f"O deposito de R${valor_deposito:.2f} realizado com sucesso!")
    
    consultar_saldo()

def fazer_saque():
    global saldo
    valor_saque = float(input("Digite o valor do saque: R$"))
    
    if valor_saque <= saldo:
        print(f"Saque de  R${valor_saque:.2f} realizado com sucesso!")
    
    else:
        print("Valor do saque superior ao valor do saldo dísponível")
    
def caixa_eletronico():
    while True:
        print(f"\nEscolha uma opção: ")
        print("1. Consultar Saldo")
        print("2. Deposito")
        print("3. Saque")
        print("4. Sair")
        
        opcao = input("Digite a opção que deseja: ")
        
        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            deposito()
        elif opcao == "3":
            fazer_saque()
        elif opcao == "4":
            print("Obrigado por usar nosso caixa eletronico")
            
        else:
            print("Opção não disponível")
            
            break
            
caixa_eletronico()
