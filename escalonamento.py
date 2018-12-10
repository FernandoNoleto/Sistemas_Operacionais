import threading
import time
from random import randint
import random
import string



class MyThread(threading.Thread):
    def run(self):
        print("tam: {} -> {}    INICIADO!".format(len(self.getName()), self.getName()))
        time.sleep(len(self.getName())/10)
        print("tam: {} -> {}    FINALIZADO!".format(len(self.getName()), self.getName()))
        # print("{} finalizado!".format(self.getName()))



def gerar_palavra(size, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


def first_come_first_served(palavras):
    count = 0
    for p in palavras:
        print("{} ->  {}".format(count, p))
        count +=1

def shortest_job_first(palavras):
    count = 0
    palavras.sort(key=len)
    # palavras.sort(reverse=True)
    for p in palavras:
        print("{} - > {}".format(count, p))
        count +=1
    

def shortest_remaing_time_next():
    for x in range(5):
        # mythread = MyThread(name = "Thread-{}".format(gerar_palavra(randint(1,8))))
        mythread = MyThread(name = "{}".format(gerar_palavra(randint(8,15))))
        mythread.start()
        time.sleep(.1)



def main():
    count = 0
    palavras = []
    for i in range(5):
        palavras.append(gerar_palavra(randint(1,10)))
        # print(gerar_palavra(randint(1,10)))
    
    
    # ----------------------------------------palavras geradas---------------------------------------- #

    print("-----------------------------")
    print("Palavras geradas:")
    for p in palavras:
        print("{} ->  {}".format(count, p))
        count +=1


    # ------------------------------------first_come_first_served------------------------------------- #
    
    print("-----------------------------")
    print("first come first served:")
    first_come_first_served(palavras)
    print("-----------------------------")
    
    # ---------------------------------------shortest_job_first--------------------------------------- #
    
    print("shortest job first:")
    shortest_job_first(palavras)
    print("-----------------------------")
    
    # ------------------------------------shortest_remaing_time_next---------------------------------- #

    print("shortest remaing time next:")
    shortest_remaing_time_next()
    



if __name__ == '__main__':
    main()