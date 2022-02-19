def TotalVendas(Cod, Lista, Tam, qtd):
    j = 0
    vendas = 0
    while j < Tam:
        if Lista[j][0] == Cod:
            if Lista[j][2] == 100 or Lista[j][2] == 102:
                qtd = int (Lista[j][1])
                vendas = vendas + qtd 
        j += 1
    return vendas

print("\n\nNomes:")
print("Igor Maximiliano de Jesus")
print("Karen Talissa da Costa Bembem")
print("Stephany Karolyne Silva Queiroz de Carvalho")
print("Tiago Batista da Silva")


Arq = open("c1_produtos.TXT", "r")
produtos = []
produtoscod = []
S = Arq.readline()
while S != "":
    S = S.split(";")
    Cod = int(S[0])
    produtoscod.append(Cod)
    qtd = int(S[1])
    qtdm = int(S[2])
    produtos.append((Cod, qtd, qtdm))
    S = Arq.readline()
Arq.close()

Arq = open("c1_vendas.TXT", "r")
vendas = []
S = Arq.readline()
while S != "":
    S = S.split(";")
    Cod = int(S[0])
    qtdv = int(S[1])
    SV = int(S[2])
    CV = int(S[3])
    vendas.append((Cod, qtdv, SV, CV))
    S = Arq.readline()
Arq.close()


#Relatório de Vendas / Estoque
cont = 0
cod = 0
j = 0
Gravar = open("TRANSFERE.TXT", "w")
Gravar.write('Necessidade de Transferência Armazém para CO\n\n')
Gravar.write('{} {:>5}   {:>5}   {:>5}   {:>5}   {:>5}  {:>5}\n'.format("Produto","QtCO", 'QtMin', 'QtVendas', 'Estq. após', 'Necess.', 'Transf. de'))
Gravar.write('{:>45} {:>21}\n'.format( 'Vendas', 'Arm p/ CO'))
while cont < len(produtos): 
    cod = produtos[j][0]
    totalV = TotalVendas(cod, vendas, len(vendas), qtd)
    total = int(totalV)
    qtCO = produtos[j][1]
    qtMin = produtos[j][2]
    posvenda = qtCO - total
    necess = qtMin - posvenda
    if necess < 0:
        necess = 0
    transf = necess
    if transf >= 1 and transf < 10:
        transf = 10
    Gravar.write('{:>5}'.format(cod) + '{:>8}'.format(qtCO) + '{:>8}'.format(qtMin) +'{:>11}'.format(total) +'{:>11}'.format(posvenda) + '{:>11}'.format(necess) + '{:>12}\n'.format(transf))
    j +=1                
    cont +=1
Gravar.close()

#Relatório de Divergências / Versão burra porém funciona
cod = 0
cont = 0
j = 0
linha = 0
Gravar = open("DIVERGENCIAS.TXT", "w")
while j < len(vendas):
    cod = vendas[j][0]
    linha+=1
    if cod in produtoscod:
        if vendas[j][2] == 135:
            Gravar.write("Linha {} - Venda Cancelada\n".format(linha))
        elif vendas[j][2] == 190:
            Gravar.write("Linha {} - Venda não Finalizada\n".format(linha))
        elif vendas[j][2] == 999:
            Gravar.write("Linha {} - Erro desconhecido. Acionar equipe de TI\n".format(linha))
    else:
        Gravar.write("Linha {} - Código de Produto não encotrado {}\n".format(linha,cod))
    j+=1 
Gravar.close()

#Tarefa Bônus
cont = 0
j = 0
repre = 0
web = 0
android = 0
iphone = 0
while j < len(vendas):
    if vendas[j][2] == 100 or vendas[j][2] == 102:
        if vendas[j][3] == 1:
            repre += vendas[j][1]
        elif vendas[j][3] == 2:
            web += vendas[j][1]
        elif vendas[j][3] == 3:
            android += vendas[j][1]
        elif vendas[j][3] == 4:
            iphone += vendas[j][1]
    j+=1

Gravar = open("TOTCANAIS.TXT", "w")
Gravar.write('Quatidade de vendas por Canal\n\n')
Gravar.write('{}    {:>17}\n'.format("Canal","QtVendas",))
Gravar.write('1 - Representante {:>8}\n'.format(repre))
Gravar.write('2 - Website {:>14}\n'.format(web))
Gravar.write('3 - Android {:>14}\n'.format(android))
Gravar.write('4 - Iphone {:>14}\n'.format(iphone))
Gravar.close()


print('\n\n### DADOS GRAVADOS COM SUCESSO ###')

print('\nFim Programa')
