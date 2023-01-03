from random import randrange
from leitorParametros import coroinhasLista,temIrmao
import gravadorEscala

# print("coroinhas disponíveis para a escala\n",coroinhas)

def numeroRandom(coroinhas):
    return randrange(0,len(coroinhas))

def eRepetido(escala,coroinha):
    if(escala.count(coroinha) == 0):
        return True
    else:
        return False

def eRepetidoFDS(escalas,coroinha):
    count = 0
    for escala in escalas:
        count+= escala.count(coroinha)
    if count == 0: 
        return True
    else: 
        return False

def maximoEscalaPorMes(escalaMensal,coroinha,nMaxMes):
    count = 0
    numeroMaximoDeCoroinhasPorMes=nMaxMes
    for escalas in escalaMensal:
        for escala in escalas:
            count+= escala.count(coroinha)
    if count <numeroMaximoDeCoroinhasPorMes: 
        return True
    else: 
        return False

def coroinhasMaxPorMissa(escala,nMax):
    numeroMaximoDeCoroinhasPorMissa= nMax
    if(len(escala)<numeroMaximoDeCoroinhasPorMissa):
        return True
    else: 
        return False

def coroinhaMinPorMissa(escalas,nMin):
    numeroMinDeCoroinhasPorMissa=nMin
    verificador = False
    for escala in escalas:
        if( len(escala)>= numeroMinDeCoroinhasPorMissa):
            verificador= False
        else:
            return True
    return verificador

def imprimirEscalas(escalaMensal):
    i,j=1,1
    for escalas in escalaMensal:
        print("Escala Semana", j)
        for escala in escalas:
            print(i,"- ",escala)
            i+=1
        i=1
        j+=1
        print("")

def criarEscala(coroinhas, escalas, escalaMensal,numeroMinDeCoroinhasPorMissa,numeroMaximoDeCoroinhasPorMissa,numeroMaximoDeRepeticaoDeCoroinhasPorMes):
    while(coroinhaMinPorMissa(escalas,numeroMinDeCoroinhasPorMissa)):
        for escala in escalas:
            coroinha = coroinhas[numeroRandom(coroinhas)]
            if( eRepetido(escala,coroinha) and eRepetidoFDS(escalas,coroinha) and 
            coroinhasMaxPorMissa(escala,numeroMaximoDeCoroinhasPorMissa) and 
            maximoEscalaPorMes(escalaMensal,coroinha,numeroMaximoDeRepeticaoDeCoroinhasPorMes)):
                escala.append(coroinha)
                irmaos= temIrmao(coroinha)
                if(irmaos != None):
                    for item in irmaos:
                        escala.append(item)
                
def contadorDeCoroinhas(escalaMensal,coroinhas):
    count = 0
    i=0
    contador=[]
    while(i<len(coroinhas)):
        coroinha=coroinhas[i]
        for escalas in escalaMensal:
            for escala in escalas:
                count+= escala.count(coroinha)
        numeroContado=str(count)
        numeroContado=numeroContado + " - " + coroinha
        contador.append(numeroContado)
        numeroContado=""
        count=0
        i+=1
    #imprimindo e gravando o contador
    gravadorEscala.gravarContador("Contador de Coroinhas")
    for cor in contador:
        print(cor)
        gravadorEscala.gravarContador(cor)
    
def main():

    # coroinhas sendo importado do arquivo coroinhas.txt
    coroinhas = coroinhasLista()
    coroinhasNomes=[]
    for coroinha in coroinhas:
        coroinhasNomes.append(coroinha[1])

    print("Total de coroinhas: ",len(coroinhasNomes),"\n")
    coroinhasNomes.sort()
    

    """
    escala1 = sabado 18:00  | escala4 = domingo 12:00 
    escala2 = domingo 08:00 | escala5 = domingo 17:30
    escala3 = domingo 10:00 | escala6 = domingo 19:30
    """
    escalas = [[],[],[],[],[],[]]
    escalaMensal=[]
    
    # Dados de Entrada
    numeroDeFDS = 4
    numeroMinDeCoroinhasPorMissa=1
    numeroMaximoDeCoroinhasPorMissa= 2
    numeroMaximoDeRepeticaoDeCoroinhasPorMes=3

    # total de missas(6*4 = 24) * numeroMIN(2) = 48 coroinhas
    # 48 corinhas / Numero maximo por mes(2) = 24 coroinhas

    for i in range(numeroDeFDS):
        criarEscala(coroinhasNomes, escalas,escalaMensal,numeroMinDeCoroinhasPorMissa,numeroMaximoDeCoroinhasPorMissa,numeroMaximoDeRepeticaoDeCoroinhasPorMes)
        escalaMensal.append(escalas)
        escalas = [[],[],[],[],[],[]]


    imprimirEscalas(escalaMensal)
    gravadorEscala.gravarEscala(escalaMensal)
    contadorDeCoroinhas(escalaMensal,coroinhasNomes)


main()
