import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys
from JogoForca import JogoForca
from JogoVelha import JogoVelha
from JogoJokenpo import Jokenpo

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super(MenuPrincipal, self).__init__()
        
        #CARREGAR TELA
        self.menu = uic.loadUi('telas\\tela_principal.ui')
        
        #BOTÕES
        self.menu.botao_jogo_forca.clicked.connect(self.jogo_forca)
        self.menu.botao_jogo_velha.clicked.connect(self.jogo_velha)
        self.menu.botao_jogo_jokenpo.clicked.connect(self.jogo_jokenpo)

        #MOSTRAR MENU
        self.menu.show()
    
    def jogo_velha(self):
        self.game = JogoVelha()
        
    def jogo_forca(self):
        self.game2 = JogoForca()

    def jogo_jokenpo(self):
        self.game3 = Jokenpo()

if __name__ == "__main__":   
    app = QApplication(sys.argv)
    UIWindow = MenuPrincipal()
    app.exec()
