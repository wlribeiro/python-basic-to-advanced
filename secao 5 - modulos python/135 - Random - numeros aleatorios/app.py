import random


inteiro = random.randint(10, 20)
print(inteiro)

print('\n')

inteiro = random.randrange(900, 1000, 10)
print(inteiro)

print('\n')

flutuante = random.uniform(10, 20)
print(flutuante)

print('\n')

lista = ['a', 'b', 'c', 'd', 'e']
sorteio = random.choice(lista)
print(sorteio)

print('\n')

lista = ['a', 'b', 'c', 'd', 'e']
sorteio = random.choices(lista, k=2)
print(sorteio)

print('\n')

lista = ['a', 'b', 'c', 'd', 'e']
sorteio = random.sample(lista, 2)
print(sorteio)

print('\n')

lista = ['a', 'b', 'c', 'd', 'e']
random.shuffle(lista)
print(lista)

print('\n')