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
        
        #VARIAVEIS
        self.lista_errada = []
        
        
        #CARREGAR TELA DO JOGO
        self.jogoforca = uic.loadUi('telas\\jogo_forca.ui', self)
        self.esconder_elementos()
                
        #BOTÕES
        self.jogoforca.btn_insert.clicked.connect(self.chute_usuario)
        self.jogoforca.btn_iniciar.clicked.connect(self.mostrar_elementos)
        
        #LABELS
        self.contador = 6
        self.jogoforca.lbl_num_skull.setText(str(self.contador))
        
        
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
        self.jogoforca.lbl_num_skull.setHidden(True)
        self.jogoforca.lbl_skull.setHidden(True)
        
    def mostrar_elementos(self):
        self.jogoforca.lbl_img.setHidden(False)
        self.jogoforca.lbl_text_try.setHidden(False)
        self.jogoforca.lbl_try.setHidden(False)
        self.jogoforca.insert_line.setHidden(False)
        self.jogoforca.btn_insert.setHidden(False)
        self.jogoforca.lbl_palavra_certa.setHidden(False)
        self.jogoforca.label_dica.setHidden(False)
        self.jogoforca.line_2.setHidden(False)
        self.jogoforca.lbl_num_skull.setHidden(False)
        self.jogoforca.lbl_skull.setHidden(False)
        self.jogoforca.btn_iniciar.setHidden(True)

        self.mostrar_dica()
        self.mostrar_palavra()

    def sortear_palavra(self):
        self.palavras = [{"banco de dados":"mongodb", "cloudcomputing":"aws", "linguagem de programação":"ruby", "framework": "flutter"}]
        return self.palavras[randint(0, len(self.palavras) -1)]
    
    def mostrar_dica(self):
        #dica
        self.palavra_sorted = self.sortear_palavra()
        self.chave = list(self.palavra_sorted.keys())
        self.escolhida = self.chave[randint(0,3)]
        self.jogoforca.label_dica.setText(f"Dica: {self.escolhida}")
        
    def mostrar_palavra(self):
        #palavra certa
        for i in self.palavras[0]:
            if i == self.escolhida:
               self.palavra_correta = self.palavras[0][i]
               
        self.jogoforca.lbl_palavra_certa.setText("_ " * len(self.palavra_correta))
        
        return self.palavra_correta        


    def chute_usuario(self):
        
        self.letra = self.jogoforca.insert_line.text().lower()
        
        if self.letra in self.palavra_correta:
            print("Letra certa")
            self.jogoforca.insert_line.setText("")
        else:
            self.lista_errada.append(self.letra)
            self.contador -= 1
            self.jogoforca.lbl_num_skull.setText(str(self.contador))
            self.jogoforca.insert_line.setText("")
            
            for l in self.lista_errada:
                self.jogoforca.lbl_try.setText(f"{self.lista_errada}")
            
            if self.contador == 0:
                self.jogoforca.setEnabled(False)