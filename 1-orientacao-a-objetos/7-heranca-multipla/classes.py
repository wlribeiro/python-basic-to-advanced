from log import LogMix


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado :
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False



class Smartphone(Eletronico, LogMix):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False


    def conectar(self):
        if not self._ligado :
            info = f'{self._nome} nao esta ligado'
            self.log_info(info)
            return
        
        if self._conectado :
            error = f'{self._nome} JA ESTA CONECTADO'
            self.log_error(error)
            return

        info = f'{self._nome} ESTA CONECTADO'
        self.log_info(info)

        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} NAO ESTA CONECTADO'
            self.log_error(error)

            return

        info = f'{self._nome} foi desligado com sucesso'
        self.log_info(info)
        self._conectado = False