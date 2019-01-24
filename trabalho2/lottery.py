import threading
import time
import timeit
from random import randint
import random
from random import shuffle
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



# ----------------------------------------funções auxliares---------------------------------------- #



def lottery(palavras = [Palavras()]):
    print("-----------------------------")

    tickets = []
    for i in range(len(palavras)):
        tickets.append(i+1)
    
    while len(palavras) > 0:
        
        palavra = palavras.pop(randint(0, len(palavras)-1))
        print("palavra sorteada: {}".format(palavra.id))
        while len(palavra.caracteres) > 0:
            print("id: {} -> {}".format(palavra.id, palavra.caracteres))
            palavra.caracteres = remover_primeiro_caracter(palavra.caracteres)
    
    
    
            

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

    # for i in range(QTD_PALAVRAS):
    #     palavras.pop(i)
    
    
    
    # ----------------------------------------Palavras Geradas---------------------------------------- #
    print("-----------------------------")
    print("Palavras geradas:")
    imprimir_palavras(palavras)

    
    # --------------------------------------------Lottery-------------------------------------------- #
    
    inicio = time.time()
    lottery(palavras)
    fim = time.time()
    time.sleep(0.5)
    print("Tempo de execucao Lottery: {} ms".format((fim-inicio)*1000))
	



if __name__ == '__main__':
    main()