import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys


class JogoVelha(QMainWindow):
    def __init__(self):
        super(JogoVelha, self).__init__()
        #Carregar a Janela
        self.jogovelha = uic.loadUi("telas\\jogo_velha.ui", self)

        #Contador
        self.contador = 0

        #Clicar no botão
        self.jogovelha.botao1.clicked.connect(lambda: self.clicar(self.jogovelha.botao1))
        self.jogovelha.botao2.clicked.connect(lambda: self.clicar(self.jogovelha.botao2))
        self.jogovelha.botao3.clicked.connect(lambda: self.clicar(self.jogovelha.botao3))
        self.jogovelha.botao4.clicked.connect(lambda: self.clicar(self.jogovelha.botao4))
        self.jogovelha.botao5.clicked.connect(lambda: self.clicar(self.jogovelha.botao5))
        self.jogovelha.botao6.clicked.connect(lambda: self.clicar(self.jogovelha.botao6))
        self.jogovelha.botao7.clicked.connect(lambda: self.clicar(self.jogovelha.botao7))
        self.jogovelha.botao8.clicked.connect(lambda: self.clicar(self.jogovelha.botao8))
        self.jogovelha.botao9.clicked.connect(lambda: self.clicar(self.jogovelha.botao9))
        self.jogovelha.botao_reset.clicked.connect(self.resetar_jogo)
        self.jogovelha.btn_return.clicked.connect(self.fechar_jogo)

        
        #Mostrar o jogo
        self.jogovelha.show()

    #Condições para verificar vencedor
    def verificar_vencedor(self):
        if self.jogovelha.botao1.text() != "" and self.jogovelha.botao1.text() == self.jogovelha.botao4.text() and self.jogovelha.botao1.text() == self.botao7.text():
            self.venceu(self.jogovelha.botao1, self.jogovelha.botao4, self.jogovelha.botao7)

        if self.jogovelha.botao2.text() != "" and self.jogovelha.botao2.text() == self.jogovelha.botao5.text() and self.jogovelha.botao2.text() == self.jogovelha.botao8.text():
            self.venceu(self.jogovelha.botao2, self.jogovelha.botao5, self.jogovelha.botao8)

        if self.jogovelha.botao3.text() != "" and self.jogovelha.botao3.text() == self.jogovelha.botao6.text() and self.jogovelha.botao3.text() == self.jogovelha.botao9.text():
            self.venceu(self.jogovelha.botao3, self.jogovelha.botao6, self.jogovelha.botao9)
            # Down
        if self.jogovelha.botao1.text() != "" and self.jogovelha.botao1.text() == self.jogovelha.botao2.text() and self.jogovelha.botao1.text() == self.jogovelha.botao3.text():
            self.venceu(self.jogovelha.botao1, self.jogovelha.botao2, self.jogovelha.botao3)

        if self.jogovelha.botao4.text() != "" and self.jogovelha.botao4.text() == self.jogovelha.botao5.text() and self.jogovelha.botao4.text() == self.jogovelha.botao6.text():
            self.venceu(self.jogovelha.botao4, self.jogovelha.botao5, self.jogovelha.botao6)

        if self.jogovelha.botao7.text() != "" and self.jogovelha.botao7.text() == self.jogovelha.botao8.text() and self.jogovelha.botao7.text() == self.jogovelha.botao9.text():
            self.venceu(self.jogovelha.botao7, self.jogovelha.botao8, self.jogovelha.botao9)

            # Diagonal
        if self.jogovelha.botao1.text() != "" and self.jogovelha.botao1.text() == self.jogovelha.botao5.text() and self.jogovelha.botao1.text() == self.jogovelha.botao9.text():
            self.venceu(self.jogovelha.botao1, self.jogovelha.botao5, self.jogovelha.botao9)

        if self.jogovelha.botao3.text() != "" and self.jogovelha.botao3.text() == self.jogovelha.botao5.text() and self.jogovelha.botao3.text() == self.jogovelha.botao7.text():
            self.venceu(self.jogovelha.botao3, self.jogovelha.botao5, self.jogovelha.botao7)

    def venceu(self, um, dois, tres):
        #Mudar a cor dos botões
        um.setStyleSheet('QPushButton {background: green; color: white; border:none;}')
        dois.setStyleSheet('QPushButton {background: green; color: white; border:none;}')
        tres.setStyleSheet('QPushButton {background: green; color: white; border:none;}')
        #Adicionar label de vencedor
        self.jogovelha.label_winner.setText(f"{um.text()} VENCEU!!")
        self.jogovelha.label_winner.setStyleSheet('QLabel {background: green; color: white;}')
        #Desabilitar teclado
        self.desabilitar()

    def desabilitar(self):
        lista_botoes = [
            self.jogovelha.botao1,
            self.jogovelha.botao2,
            self.jogovelha.botao3,
            self.jogovelha.botao4,
            self.jogovelha.botao5,
            self.jogovelha.botao6,
            self.jogovelha.botao7,
            self.jogovelha.botao8,
            self.jogovelha.botao9,
        ]
        #Resetar botões
        for botao in lista_botoes:
            botao.setEnabled(False)


    def clicar(self, botao):
        if self.contador % 2 == 0:
            marcar = "X"
            self.jogovelha.label_winner.setText("VAI 'O'")
        else:
            marcar = "O"
            self.jogovelha.label_winner.setText("VAI 'X'")

        botao.setText(marcar)
        botao.setEnabled(False)
        self.contador += 1
        self.verificar_vencedor()
        
    def resetar_jogo(self):
		# Create a List of all our buttons
        lista_botoes2 = [
            self.jogovelha.botao1,
            self.jogovelha.botao2,
            self.jogovelha.botao3,
            self.jogovelha.botao4,
            self.jogovelha.botao5,
            self.jogovelha.botao6,
            self.jogovelha.botao7,
            self.jogovelha.botao8,
            self.jogovelha.botao9,
        ]

        #Resetar botões
        for botao in lista_botoes2:
            botao.setText("")
            botao.setEnabled(True)
            # Reset The Button Colors
            botao.setStyleSheet('QPushButton {background: rgb(58, 58, 58); color: rgb(255, 255, 255); border: none;}')
		# Resetar a Label
        self.jogovelha.label_winner.setText("VAI 'X'")
        self.jogovelha.label_winner.setStyleSheet('QLabel {background: rgb(58,58,58); color:white;}')

        # Resetar o contador
        self.contador = 0
    
        
    def fechar_jogo(self):
        self.close()
