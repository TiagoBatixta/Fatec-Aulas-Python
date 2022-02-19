print("\n\nNomes:")
print("Igor Maximiliano de Jesus")
print("Karen Talissa da Costa Bembem")
print("Stephany Karolyne Silva Queiroz de Carvalho")
print("Tiago Batista da Silva")

def EstaNaLista(cod, Lista, Tam):#função para fazer saber se o Codigo está na lista
    j = 0
    while j < Tam:
        if Lista[j][0] == Cod:
            return True
        j += 1
    return False

def total(cod, Lista, Tam, qtd, valor):#função para fazer o calculo do total
    j = 0
    mult = 0
    while j < Tam:
        if Lista[j][0] == Cod:
            qtd = int (Lista[j][1])
            valor = float (Lista[j][2])
            mult += qtd * valor
        j += 1
    return mult

Arq = open("vendas.txt", "r")
armazena = [] #Lista para Armazenar os Dados do Arquivo Vendas

S = Arq.readline()
while S != "":#Laço para ler e armazenar os valores do arquivo
    S = S.split(";")
    Cod = int(S[0])
    if Cod >= 10000 and Cod <= 21000:
        quantidade = int(S[1])
        valor = float(S[2])
        armazena.append((Cod, quantidade, valor))#Armazena os dados em Lista na forma de Tuplas
    S = Arq.readline()

cont= 0
mult = 0
j = 0
while j < len(armazena):
    qtd = int (armazena[j][1])
    valor = float (armazena[j][2])
    mult += qtd * valor
    j += 1
print('\nValor geral total vendido: {:.2f}'.format(mult))

Cod = 1
while Cod != 0:#Laço para ser digitado os Dados pelo o usuario
    Cod = int(input("\nDigite o código: "))
    if Cod == 0:
        print('Fim do Programa')        
    elif Cod >= 10000 and Cod <= 21000:
        if EstaNaLista(Cod, armazena, len(armazena)):                   
            qtd = 0
            valor = 0
            soma = total(Cod, armazena, len(armazena), qtd, valor)
            total1 = float(soma)
            print ('Total vendido do produto {} = R$ {:.2f}'.format(Cod,total1))
        else:
            print("Código não Listado")
    else:
        print('{} Código inválido (deve ser entre 10000 e 21000)'.format(Cod))

Arq.close()

