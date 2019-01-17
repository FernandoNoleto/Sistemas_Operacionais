# import threading
# import time
# import timeit
from random import randint
import random
import string
# import pprint

QTD_PALAVRAS = 5

class Palavras(object):
    def __init__(self):
        self.caracteres = ""
        self.id = 0
        self.prioridade = 0


# ----------------------------------------funções auxliares---------------------------------------- #


def imprimir_palavras(palavras = [Palavras()]):
    print("-----------------------------")
    for p in palavras:
        print("id: {} -> {}".format(p.id, p.caracteres))

def gerar_palavra(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def remover_primeiro_caracter(palavra):
    palavra = palavra[1:]
    return palavra

def organizar_por_menor_tamanho(palavras = [Palavras()]):
    nova_lista = []
    
    while 1:
        menor_tamanho = 100
        for palavra in palavras:
            if len(palavra.caracteres) < menor_tamanho:
                menor_tamanho = len(palavra.caracteres)
                menor_palavra = palavra
        nova_lista.append(menor_palavra)
        palavras.remove(menor_palavra)
        if len(palavras) == 0:
            break
    # imprimir_palavras(nova_lista)
    return nova_lista



# -----------------------------------------------função-------------------------------------------- #



def shortest_process_next(palavras = [Palavras()]):
    print("-----------------------------")
    for palavra in palavras:
        print("Processo de id: {}".format(palavra.id))
        while len(palavra.caracteres) > 0:
            print(palavra.caracteres)
            palavra.caracteres = remover_primeiro_caracter(palavra.caracteres)
        print("-----------------------------")

   

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
    _palavras = organizar_por_menor_tamanho(palavras)
    # imprimir_palavras(_palavras)
    
    # ------------------------------------------Prioridade-------------------------------------------- #
    shortest_process_next(_palavras)

	



if __name__ == '__main__':
    main()