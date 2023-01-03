import os
from unidecode import unidecode

if(os.path.exists("coroinhas.txt") == False):
    open("coroinhas.txt","w")
    print("Digite os nomes dos coroinhas disponíveis no arquivo coroinhas.txt separando por linhas")
    quit()

def coroinhasLista():
    with open("coroinhas.txt",'r') as f:
        lines=f.readlines()
        size= len(lines)
        f.close()

    coroinhasLista=[]
#remove as linhas que começam com # e remove o \n do final
    for line in lines:
        lista = line.split("|")
        if(not lista[0][:1] == "#"):
            lista[2]=lista[2][:len(lista[2])-1]
            coroinhasLista.append(lista)
    return coroinhasLista


def devolveNome(id):
    lista= coroinhasLista()
    for item in lista:
        if(id == item[0]):
            return item[1]



def temIrmao(nomeIrmao):
    irmaos=[]
    for coroinha in coroinhasLista():
        hashtag = coroinha[2]
        hashtag = hashtag.strip() #removing white space
        if(coroinha[1] == nomeIrmao and hashtag != "#" ):
            if "," in coroinha[2] :
                listaIrmaos= coroinha[2].split(",")
                for irmao in listaIrmaos:
                    irmaos.append(devolveNome(irmao))
                return irmaos
            else:
                irmaos.append(devolveNome(coroinha[2]))
                return irmaos
