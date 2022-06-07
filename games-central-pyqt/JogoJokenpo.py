from secrets import choice
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget
from PyQt5 import uic
import sys
import random

class Jokenpo(QWidget):
    def __init__(self):
        super(Jokenpo, self).__init__()
        #CARREGAR TEÇA
        self.jokenpo = uic.loadUi("telas\\jokenpo.ui")

        #VARIAVEIS E BOTÕES
        self.computador = ['pedra', 'papel', 'tesoura']
        self.jokenpo.btn_pedra.clicked.connect(self.press_pedra)
        self.jokenpo.btn_tesoura.clicked.connect(self.press_tesoura)
        self.jokenpo.btn_papel.clicked.connect(self.press_papel)

        
        #MOSTRAR TELA
        self.jokenpo.show()

    def press_pedra(self):
        self.jokenpo.lbl_user.setText(f"PEDRA")
        self.logica_jogo()
        
    def press_papel(self):
        self.jokenpo.lbl_user.setText(f"PAPEL")
        self.logica_jogo()

    def press_tesoura(self):
        self.jokenpo.lbl_user.setText(f"TESOURA")
        self.logica_jogo()


    def sorteio_pc(self):
        self.escolha_pc = choice(self.computador).upper()
        self.jokenpo.lbl_comp.setText(self.escolha_pc)
    
    def logica_jogo(self):
        self.sorteio_pc()
        user = self.jokenpo.lbl_user.text()
        pc = self.jokenpo.lbl_comp.text()

        if user == pc:
            self.jokenpo.lbl_winner.setText("EMPATE")
        elif user == "TESOURA" and pc == "PAPEL":
            self.jokenpo.lbl_winner.setText("USER")
        elif user == "PEDRA" and pc == "TESOURA":
            self.jokenpo.lbl_winner.setText("USER")
        elif user == "PAPEL" and pc == "PEDRA":
            self.jokenpo.lbl_winner.setText("USER")
        elif pc == "TESOURA" and user == "PAPEL":
            self.jokenpo.lbl_winner.setText("MACHINE")
        elif pc == "PEDRA" and user == "TESOURA":
            self.jokenpo.lbl_winner.setText("MACHINE")
        elif pc == "PAPEL" and user == "PEDRA":
            self.jokenpo.lbl_winner.setText("MACHINE")

    
