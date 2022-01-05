from threading import Thread
from time import sleep

'''
class MeuThread(Thread):

    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo


        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t = MeuThread("esse e um teste", 5)
t.start()

for i in range(20):
    print(i)
    sleep(1)
'''

'''
def espere(texto, tempo):
    sleep(tempo)
    print(texto)

t = Thread(target=espere, args=('estou retornando', 5))
t.start()

for i in range(20):
    print(i)
    sleep(.5)
'''

'''
def espere(texto, tempo):
    sleep(tempo)
    print(texto)

t = Thread(target=espere, args=('estou retornando', 5))
t.start()

while t.is_alive():
    print('Aguardando')
    sleep(3)
'''
