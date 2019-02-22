import threading
import time
import timeit
from random import randint
import random
import string
# import pprint

QTD_PALAVRAS = 15

class Palavras(object):
    def __init__(self):
        self.caracteres = ""
        self.id = 0
        self.prioridade = 0


# ----------------------------------------funções auxliares---------------------------------------- #


def imprimir_palavras(palavras = [Palavras()]):
    for p in palavras:
        print("id: {} -> {} -> prioridade: {}".format(p.id, p.caracteres, p.prioridade))

def gerar_palavra(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def remover_primeiro_caracter(palavra):
    palavra = palavra[1:]
    return palavra


# -----------------------------------------------função-------------------------------------------- #


#O algoritmo estabelece uma prioridade para um processo
#Aquele algoritmo que tem prioridade maior é executado primeiro
def prioridade(palavras = [Palavras()]):
    print("-----------------------------")
    maior_prioridade_atual = 0
    palavra_atual = Palavras()
    
    while len(palavras) > 0:
        maior_prioridade_atual = 0
        for palavra in palavras:
            if palavra.prioridade > maior_prioridade_atual:
                maior_prioridade_atual = palavra.prioridade
            
        for palavra in palavras:
            if palavra.prioridade == maior_prioridade_atual:
                palavra_atual = palavra
                palavras.remove(palavra)
                while len(palavra_atual.caracteres) > 0:
                    print("id: {} -> {}".format(palavra_atual.id, palavra_atual.caracteres))
                    palavra_atual.caracteres = remover_primeiro_caracter(palavra_atual.caracteres)

def main():

    id = QTD_PALAVRAS
    palavras = []

    for i in range(QTD_PALAVRAS):
        palavra = Palavras()
        palavra.caracteres = gerar_palavra(randint(1,10))
        palavra.id = id
        id = id-1
        palavra.prioridade = randint(1,3)
        palavras.append(palavra)
    palavras.reverse()
    
    
    
    # ----------------------------------------Palavras Geradas---------------------------------------- #
    print("-----------------------------")
    print("Palavras geradas:")
    imprimir_palavras(palavras)
    
    # ------------------------------------------Prioridade-------------------------------------------- #
    
    inicio = time.time()
    prioridade(palavras)
    fim = time.time()
    time.sleep(0.5)
    print("Tempo de execucao Prioridade: {} ms".format((fim-inicio)*1000))

	



if __name__ == '__main__':
    main()