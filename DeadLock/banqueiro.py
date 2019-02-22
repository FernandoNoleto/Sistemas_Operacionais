import threading
import time
import timeit
from random import randint
import random
from random import shuffle
import string
from threading import Thread
from time import sleep

class Palavras(object):
    def __init__(self):
        self.caracteres = ""
        self.id = 0
        self.mem_necessario = randint(1, 2) #1gb - 2gb 
        self.pro_necessario = randint(5, 30) #5% - 30%
        self.hd_necessario = randint(3, 50) #3gb - 50gb
        

class Recurso(object):
    def __init__(self):
        self.memoria_total = randint(4, 16) #4gb - 16gb
        self.processador_total = 100 #100% de processador
        self.disco_total = randint(500, 1000) #500gb - 1000gb
        self.mem_alocada = 0
        self.pro_alocada = 0
        self.hd_alocada = 0


QTD_PALAVRAS = 10
FILA_DE_ESPERA = []
PROCESSOS_JA_EXECUTADOS = []
recursos = Recurso()



# ----------------------------------------funções auxliares---------------------------------------- #


def imprimir_palavras(palavras = [Palavras()]):
    for p in palavras:
        print("id: {} -> {}; mem:{}; proc:{}; hd:{}".format(p.id, p.caracteres, p.mem_necessario, p.pro_necessario, p.hd_necessario))

def imprimir_recursos():
    print("memoria: {}gb; processador: {}%; hd: {}gb".format(recursos.memoria_total, recursos.processador_total, recursos.disco_total))
        

def gerar_palavra(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def remover_primeiro_caracter(palavra):
    palavra = palavra[1:]
    return palavra



# ----------------------------------------funções auxliares---------------------------------------- #   



def banqueiro():
    
    while(len(FILA_DE_ESPERA) > 0):
        alocou = False
        for p in FILA_DE_ESPERA:
            # print("recursos.memoria_total {}".format(recursos.memoria_total))
            # print("recursos.mem_alocada {}".format(recursos.mem_alocada))

            mem_disponivel = recursos.memoria_total - recursos.mem_alocada
            print("Memoria disponivel",format(mem_disponivel))

            if(p.mem_necessario <= mem_disponivel): #Se a memoria necessaria <= memoria disponivel
                recursos.mem_alocada = recursos.mem_alocada + p.mem_necessario #aloco a memoria para o processo 
                # print("recursos.mem_alocada",format(recursos.mem_alocada))               
                print("Processo de ID: {} -> \"{}\" alocou {}mb de memoria".format(p.id, p.caracteres, p.mem_necessario))
                print("Memoria restante: {}gb".format(recursos.memoria_total - recursos.mem_alocada))
                print("----------------------------------------------------------")
                # sleep(0.1)
                # print("Processo de ID: {} -> {} executou!".format(p.id, p.caracteres))

                # recursos.mem_alocada = recursos.mem_alocada - p.mem_necessario 
                # recursos.mem_alocada = 0
                # print(recursos.mem_alocada)
                # recursos.mem_alocada = recursos.mem_alocada - p.mem_necessario 
                FILA_DE_ESPERA.remove(p) #Tiro o processo da lista de execução
                # thread = Thread(target = executar_processo, args = (p, ))
                # recursos.memoria_total += p.mem_necessario
                
            else:
                print("Processo de ID: {} -> {} não alocou memoria e será colocado na lista de espera".format(p.id, p.caracteres))
                print("Memoria necessária para alocar: {}".format(p.mem_necessario))
                print("Memoria disponivel: {}gb".format(recursos.memoria_total - recursos.mem_alocada))
                print("----------------------------------------------------------")
              
        sleep(0.1)
        print("Processo de ID: {} -> \"{}\" executou!".format(p.id, p.caracteres))

        recursos.mem_alocada = recursos.mem_alocada - p.mem_necessario 
            
            

def executar_processo(processo = Palavras()):
    print ("Processo de ID {} -> \"{}\" -- Executando!".format(processo.id, processo.caracteres))
    for i in range(len(processo.caracteres)):
        sleep(0.1)
    print ("Processo de ID {} -> \"{}\" -- Finalizado!".format(processo.id, processo.caracteres))
    recursos.mem_alocada = recursos.mem_alocada - processo.mem_necessario 
    # recursos.mem_alocada = recursos.mem_alocada - processo.mem_necessario 
    # recursos.memoria_total += processo.mem_necessario
    # FILA_DE_ESPERA.remove(processo)
    # return processo




# def adicionar_na_lista_de_executados(removido = Palavras()):
    
#     thread = Thread(target = executar_processo, args = (removido, ))
#     thread.start()
#     thread.join()
#     print("----------------------------------------------------------")
#     PROCESSOS_JA_EXECUTADOS.append(removido)
#     #libero o espaço alocado e devolvo para a memoria_total
#     recursos.mem_alocada = recursos.mem_alocada - removido.mem_necessario 
#     recursos.memoria_total += removido.mem_necessario
#     return recursos

#     # if(len(PROCESSOS_JA_EXECUTADOS) == QTD_PALAVRAS):
#     #     return
            
            
            




if __name__ == "__main__":


    # ----------------------------------------------------------------------------------------------- #
    id = QTD_PALAVRAS
    palavras = []

    for i in range(QTD_PALAVRAS):
        palavra = Palavras()
        palavra.caracteres = gerar_palavra(randint(1,10))
        palavra.id = id
        id = id-1
        palavras.append(palavra)
    palavras.reverse()

    # ----------------------------------------------------------------------------------------------- #

    # recursos_disponiveis = Recurso()
    FILA_DE_ESPERA = palavras


    # ------------------------------------------------------------------------------------------------- #
    
    
    
    # ----------------------------------------Palavras Geradas---------------------------------------- #
    print("----------------------------------------------------------")
    print("Palavras geradas:")
    imprimir_palavras(FILA_DE_ESPERA)

    # -------------------------------------Recursos Disponiveis--------------------------------------- #

    print("----------------------------------------------------------")
    print("----------------------------------------------------------")
    print("Recursos Disponiveis:")
    imprimir_recursos()


    # ------------------------------------Algoritmo do Banqueiro-------------------------------------- #

    print("----------------------------------------------------------")
    print("----------------------------------------------------------")
    banqueiro()
    
    # print(recursos.memoria_total)
    # print(recursos.mem_alocada)
