import os

if(os.path.exists("escala.txt") == False):
    open("escala.txt","w+")

def gravarEscala(escalaMensal):
    with open ("escala.txt","w") as f:
        i,j=1,1
        for escalas in escalaMensal:
            f.write("Escala Semana %d\n" % j)
            for escala in escalas:
                coroinhas = ""
                for coroinha in escala: #separando cada coroinha da lista escala
                    coroinhas = coroinhas + coroinha + ", "
                coroinhas = coroinhas[:len(coroinhas)-2]
                linha = str(i)+"- "+ str(coroinhas) + "\n"
                f.write(linha)
                i+=1
            i=1
            j+=1
            f.write("\n")

def gravarContador(coroinha):
    with open ("escala.txt","a") as f:
        f.write("%s\n" % coroinha)