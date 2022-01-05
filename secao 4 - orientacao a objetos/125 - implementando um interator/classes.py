class MinhaLista:
    def __init__(self):
        self.__itens = []
        self.__index = 0
    
    def add(self, valor):
        self.__itens.append(valor)

    def __iter__(self):
        return self

    def __getitem__(self, index):
        return self.__itens[index]

    def __setitem__(self, index, value):
        if index >= len(self.__itens):
            self.__itens.append(value)

        self.__itens[index] = value

    def __next__(self):
        try:
            item = self.__itens[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f"{self.__class__.__name__}({self.__itens})"

    def __delitem__(self, index):
        del self.__itens["index"]