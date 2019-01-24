import threading
import time
import timeit
from random import randint
import random
import string

QTD_PALAVRAS = 5

class Palavras(object):
    def __init__(self):
        self.caracteres = ""
        self.id = 0


# ----------------------------------------funções auxliares---------------------------------------- #


def imprimir_palavras(palavras = [Palavras()]):
    for p in palavras:
        print("id: {} -> {}".format(p.id, p.caracteres))

def gerar_palavra(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def remover_primeiro_caracter(palavra):
    palavra = palavra[1:]
    return palavra

def tempo_de_processo(tam_palavra, quantum, qtd_de_processos):
    tempo_de_processo = int(tam_palavra / (quantum / qtd_de_processos))
    return tempo_de_processo


# ----------------------------------------funções auxliares---------------------------------------- #



def garantido(quantum, palavras = [Palavras()]):
    print("-----------------------------")
    teste = 0
    qtd_de_processos = len(palavras)

    while len(palavras) > 0 or teste > 20:
        # teste +=1
        palavra = palavras.pop(0)
        # print("id: {} -> {}".format(palavra.id, palavra.caracteres))
        tmp = tempo_de_processo(len(palavra.caracteres), quantum, qtd_de_processos)
        print("Tempo de processo: {}".format(tmp))
        # break
        if tmp>0:
            for i in range(tmp):
                print("id: {} -> {}".format(palavra.id, palavra.caracteres))
                palavra.caracteres = remover_primeiro_caracter(palavra.caracteres)
                if len(palavra.caracteres) <= 0:
                    break
        # break
        if len(palavra.caracteres) > 0:
            palavras.append(palavra)
        
    
    
            

def main():

    id = QTD_PALAVRAS
    palavras = []

    for i in range(QTD_PALAVRAS):
        palavra = Palavras()
        palavra.caracteres = gerar_palavra(randint(1,10))
        palavra.id = id
        id = id-1
        palavras.append(palavra)
    palavras.reverse()
    
    
    
    # ----------------------------------------Palavras Geradas---------------------------------------- #
    print("-----------------------------")
    print("Palavras geradas:")
    imprimir_palavras(palavras)
    
    # --------------------------------------------Garantido------------------------------------------- #
    quantum = int(input("Quantidade de quantuns?"))
    # print(quantum)
    
    
    inicio = time.time()
    garantido(quantum, palavras)
    fim = time.time()
    time.sleep(0.5)
    print("Tempo de execucao Garantido: {} ms".format((fim-inicio)*1000))




if __name__ == '__main__':
    main()