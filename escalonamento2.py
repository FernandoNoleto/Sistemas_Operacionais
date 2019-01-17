import threading
import time
import timeit
from random import randint
import random
import string
import pprint

QTD_PALAVRAS = 3
# ID = 0

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


# ----------------------------------------funções auxliares---------------------------------------- #


#Round robin da prioridade igual a todos os processos. 
#Cada processo é executado em uma mesma quantidade de tempo em uma lista circular
def round_robin(palavras = [Palavras()]):
    print("-----------------------------")
    while len(palavras) > 0:
        palavra = palavras.pop(0)
        print("id: {} -> {}".format(palavra.id, palavra.caracteres))
        palavra.caracteres = remover_primeiro_caracter(palavra.caracteres)
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
    
    # -----------------------------------------Round Robin-------------------------------------------- #
    round_robin(palavras)

	



if __name__ == '__main__':
    main()