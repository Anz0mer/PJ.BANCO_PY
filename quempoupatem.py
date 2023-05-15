#biblioteca que importa a data e o tempo real.
from datetime import datetime
data = datetime.now()

#função onde estão as escolhas que o cliente pode fazer.
def menu():
    print('''Por favor, digite o número da ação solicitada, sendo:
            1- Novo Cliente
            2- Apaga Cliente
            3- Débito
            4- Depósito
            5- Extrato
            6- Transferência entre contas
            7- Conversão em milhas
            0- Sair''')
#função que pede para o cliente escolher a ação que deseja realizar.
def escolhaMenu():
    x=int(input('Digite a sua escolha: '))
    return x


#função que pede os dados do novo cliente.
def novocliente():
    #arquivo que vai armazenar os dados do novo cliente.
    conta=open("clientes.txt", "a")
    nome=input('Nome: ')
    cpf=int(input('CPF: '))
    conta1=input('Tipo de conta (são dois: comum e plus): ')
    valor=float(input('Valor inicial da conta: R$'))
    senha=int(input('Senha do usuário: '))
    milhas = 0    
    
    #ação que vai armazenar os dados. 
    while nome != '':
        conta=open('clientes.txt', 'a')
        #são 5 '%s', pois é um para cada input colocado.
        conta.write('%s %s %s %s %s %s\n' % (nome, cpf, conta1, valor, senha, milhas))
        conta.close()
        break
    print('Conta criada, parabéns!!')

#função que vai apagar o cliente do arquivo.
def apagacliente():
    cpf1=int(input('CPF: '))
    clientes = []
    with open ('clientes.txt', 'r+') as f:
        clientes_arquivos = f.readlines()
        for cliente in clientes_arquivos:
            x = cliente.split(' ')
            if x[1] != cpf1:
                clientes.append(cliente)
    f.close()
    
    with open ('clientes.txt', 'w') as f:
        for c in clientes:
            f.write(c)
            
    f.close()
    print('Conta Apagada!')

#função que vai solicitar os dados para debitar um valor para a conta. 
def debito():
    cpf2=int(input('CPF: '))
    senha2=int(input('Senha: '))
    valor2=float(input('Qual valor deseja debitar?: '))
    clientes = []
    tarifa1 = valor2 * 0.05
    tarifa2 = valor2 * 0.03
    
    with open("clientes.txt", "r+") as f:
        clientes_arquivo = f.readlines()
        for cliente in clientes_arquivo:
            x = cliente.split()
            if int(x[1]) == cpf2 and int(x[4]) == senha2 and x[2] == "comum" and float(x[3]) >= -1000:
                x[3] = float(x[3])  - valor2 - tarifa1
                print(x[3]) 
                cliente = ("%s %s %s %s %s %s\n" % (x[0], x[1], x[2], x[3], x[4], x[5]))    
                with open ("extrato.txt", "a") as f:
                    f.write(f"{cpf2} Data: {datetime.now()} {valor2} Tarifa: {tarifa1} Saldo: {x[3]}\n") 
            if int(x[1]) == cpf2 and int(x[4]) == senha2 and x[2] == "plus" and float(x[3]) >= -5000:
                x[3] = float(x[3])  - valor2 - tarifa2
                cliente = ("%s %s %s %s %s %s\n" % (x[0], x[1], x[2], x[3], x[4], x[5]))
                with open ("extrato.txt", "a") as f:
                    f.write(f"{cpf2} Data: {datetime.now()} {valor2} Tarifa: {tarifa2} Saldo: {x[3]}\n")     
            clientes.append(cliente) 
    with open("clientes.txt","w") as f:
        for cliente in clientes:
            f.write(cliente)
    f.close() 
    print('Débito Realizado!')

#função que vai solicitar os dados para fazer um depósito na conta.
def deposito():
    cpf3=int(input('CPF: '))
    valor3=float(input('Qual o valor que deseja depositar?: '))

    clientes = []
    saldo = 0
    with open("clientes.txt", "r+") as f:
        clientes_arquivo = f.readlines()
        for cliente in clientes_arquivo:
            x = cliente.split()
            if int(x[1]) == cpf3:
                x[3] = float(x[3]) + valor3
                saldo = x[3]
                print(saldo)
            cliente = ("%s %s %s %s %s %s\n" % (x[0], x[1], x[2], x[3], x[4], x[5]))    
            clientes.append(cliente)
            with open ("extrato.txt", "a") as f:
                f.write(f"{cpf3} Data: {datetime.now()} {valor3} Tarifa: {0} Saldo: {saldo}\n") 
        with open("clientes.txt","w") as f:
            for cliente in clientes:
                f.write(cliente)
        f.close()
        print('Depósito Realizado!')

#função que vai solicitar os dados para mostrar o extrato da conta.
def extrato():
    cpf4=int(input('CPF: '))
    senha4=int(input('Senha: '))

    with open("clientes.txt", "r+") as f:
        clientes_arquivo = f.readlines()
        for cliente in clientes_arquivo:
            x = cliente.split()
            if cpf4 == int(x[1]) and senha4 == int(x[4]):
                with open ("extrato.txt", "r") as f:
                    
                    for linha in f.readlines():
                        
                        cpf4, texto = linha.split(" ", 1)
                        cpf4 = int(cpf4)
                        if int(x[1]) == cpf4 and int(x[4]) == senha4:
                            print(texto)

#função que vai solicitar os dados para realizar uma transferência bancária. 
def transferencia():
    cpf5=int(input('CPF (Origem): '))
    senha5=int(input('Senha (Origem): '))
    cpf6=int(input('CPF (Destino): '))
    valor5=float(input('Qual o valor da tranferência?: '))    

    clientes = []
    with open("clientes.txt", "r") as f:
        clientes_arquivo = f.readlines()
        for cliente in clientes_arquivo:
            x = cliente.split()
            if int(x[1]) == cpf5 and int(x[4]) == senha5:
                x[3] = float(x[3]) - valor5
                print(x[3])
                cliente = ("%s %s %s %s %s %s\n" % (x[0], x[1], x[2], x[3], x[4], x[5]))
                clientes.append(cliente)
                with open ("extrato.txt", "a") as f:
                    f.write(f"{cpf5} Data: {datetime.now()} {valor5} Tarifa: {0} Saldo: {x[3]}\n")  
            if int(x[1]) == cpf6:
                x[3] = float(x[3]) + valor5
                cliente = ("%s %s %s %s %s %s\n" % (x[0], x[1], x[2], x[3], x[4], x[5]))
                clientes.append(cliente)
                with open ("extrato.txt", "a") as f:
                    f.write(f"{cpf6} Data: {datetime.now()} {valor5} Tarifa: {0} Saldo: {x[3]}\n")     
    with open("clientes.txt","w") as f:
        for cliente in clientes:
            f.write(cliente)
    f.close()   
    print('Tranferência Realizada!!')     

#função que vai realizar a conversão de real para milhas. 
def milhas():
    cpf7= int(input("CPF: "))
    senha6= int(input("Senha: "))
    valor6 = float(input("Digite o valor que deseja converter: R$"))
    milhas = valor6 * 0.3
    clientes = []

    with open("clientes.txt", "r+") as f:
        clientes_arquivo = f.readlines()
        for cliente in clientes_arquivo:
            x = cliente.split()
            if int(x[1]) == cpf7 and int(x[4]) == senha6:
                x[3] = float(x[3]) - valor6
                x[5] = float(x[5]) + milhas
                print(x[5])
                cliente = ("%s %s %s %s %s %s\n" % (x[0], x[1], x[2], x[3], x[4], x[5]))
                clientes.append(cliente)
            else:
                clientes.append(cliente)             
    with open("clientes.txt","w") as f:
        for cliente in clientes:
            f.write(cliente)
    f.close()
    print("Conversão Realizada!")
    with open ("extrato.txt", "a") as f:
            f.write(f"{cpf7} Data: {datetime.now()} {valor6} Tarifa: {0} Saldo: {x[3]}\n")        
    

#função que vai sair do menu.
def sair():
    sair=('Operação encerrada!')
    print(sair)

while True:
    menu()
    #variável que armazena o menu.
    a = escolhaMenu()

    #ações que vão ser realizadas após a escolha do cliente no menu. 
    if (a==1):
        novocliente()

    if (a==2):
        apagacliente()

    if (a==3):
        debito()

    if (a==4):
        deposito()

    if (a==5):
        extrato()

    if (a==6):
        transferencia()

    if (a==7):
        milhas()

    if (a==0):
        sair()
        break 