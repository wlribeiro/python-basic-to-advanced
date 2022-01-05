from threading import Thread
from threading import Lock
from time  import sleep

class Ingressos:

    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        sleep(1)

        if self.estoque < quantidade:
            print('Nao temos ingressos suficientes...')

            self.lock.release()

            return

        print(f'voce comprou {quantidade} ingrecos, ainda temos {self.estoque}')

        self.estoque -= quantidade

        self.lock.release()


if __name__ == '__main__' :
    ingressos = Ingressos(10)
    
    t = Thread(target=ingressos.comprar, args=(3,))
    t.start()

    t = Thread(target=ingressos.comprar, args=(3,))
    t.start()
    
    t = Thread(target=ingressos.comprar, args=(3,))
    t.start()

    t = Thread(target=ingressos.comprar, args=(3,))
    t.start()

    t = Thread(target=ingressos.comprar, args=(3,))
    t.start()
    


