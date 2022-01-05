from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self,msg): pass


class B(A):
    
    def fala(self, msg):
        print("B esta falando...")