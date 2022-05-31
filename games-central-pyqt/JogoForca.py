from pickle import FALSE
from random import randint, random
from secrets import choice
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys
import random

class JogoForca(QMainWindow):
    def __init__(self):
        super(JogoForca, self).__init__()
        
        #CARREGAR TELA DO JOGO
        self.jogoforca = uic.loadUi('telas\\jogo_forca.ui', self)
        self.esconder_elementos()
                
        #BOTÕES
        self.jogoforca.btn_insert.clicked.connect(self.enviar_letra)
        self.jogoforca.btn_iniciar.clicked.connect(self.mostrar_elementos)
        
        
        #MOSTRAR A TELA
        self.jogoforca.show()
    
    
    def esconder_elementos(self):    
        #ESCONDER ELEMENTOS
        self.jogoforca.lbl_img.setHidden(True)
        self.jogoforca.lbl_text_try.setHidden(True)
        self.jogoforca.lbl_try.setHidden(True)
        self.jogoforca.insert_line.setHidden(True)
        self.jogoforca.btn_insert.setHidden(True)
        self.jogoforca.lbl_palavra_certa.setHidden(True)
        self.jogoforca.label_dica.setHidden(True)
        self.jogoforca.line_2.setHidden(True)
        
    def mostrar_elementos(self):
        self.jogoforca.lbl_img.setHidden(False)
        self.jogoforca.lbl_text_try.setHidden(False)
        self.jogoforca.lbl_try.setHidden(False)
        self.jogoforca.insert_line.setHidden(False)
        self.jogoforca.btn_insert.setHidden(False)
        self.jogoforca.lbl_palavra_certa.setHidden(False)
        self.jogoforca.label_dica.setHidden(False)
        self.jogoforca.line_2.setHidden(False)
        self.jogoforca.btn_iniciar.setHidden(True)

        self.mostrar_dica()
    
    def enviar_letra(self):
        self.variavel = self.jogoforca.insert_line.text()
        return self.variavel

    def sortear_palavra(self):
        self.palavras = [{"banco de dados":"mongodb", "cloudcomputing":"aws", "linguagem de programação":"ruby", "framework": "flutter"}]
        return self.palavras[randint(0, len(self.palavras) -1)]
    
    def mostrar_dica(self):
        #dica
        self.palavra_sorted = self.sortear_palavra()
        self.chave = list(self.palavra_sorted.keys())
        self.escolhida = self.chave[randint(0,3)]
        self.jogoforca.label_dica.setText(f"Dica:{self.escolhida}")
        
        #palavra certa
        for i in self.palavras[0]:
            if i == self.escolhida:
               self.palavra_correta = self.palavras[0][i]

        self.jogoforca.lbl_palavra_certa.setText("_ " * len(self.palavra_correta))
            
    
    