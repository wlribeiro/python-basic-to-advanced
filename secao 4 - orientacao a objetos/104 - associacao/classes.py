
class Writer:
    def __init__(self, name):
        self.__name = name
        self.__tool = None

    @property
    def name(self):
        return self.__name

    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool):
        self.__tool = tool


class Pen :
    def __init__(self, brand):
        self.__brand = brand

    @property
    def getbrand(self):
        return self.__name

    def write(self):
        print("caneta de escrever esta a escrvendo...")


class WriteMachine():
    def write(self):
        print("maquina de escrever esta a escrvendo...")