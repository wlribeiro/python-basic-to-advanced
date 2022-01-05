""" 31458663116"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow
from validacpf import validacpf


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


        self.btnVerificaCpf.clicked.connect(self.valida_cpf)

    def valida_cpf(self):
        cpf = self.inputValidaCpf.text()
        response = ''
        if validacpf(cpf) :
            response = "CPF valido"
        else:
            response = "CPF invalido"
            
        self.respostaValidaCpf.setText(
            response
        )


if __name__ == '__main__' :
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
