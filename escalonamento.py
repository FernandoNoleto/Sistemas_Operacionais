from random import randint
import random
import string

class Palavras(object):
    
    def __init__(self):
        self.palavra = ""
        self.tamanho = 0
        self.prioridade = 0

    # def gerar_palavra():
        # randint(1, 10)
    def gerar_palavra(self, size, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))





def main():
    p = Palavras()
    for i in range(5):
        print(p.gerar_palavra(randint(1,10)))


if __name__ == "__main__":
    main()