# coding=utf-8

from tkinter import *
import sys

class ConfigSistema:
    def __init__(self):
        root= Tk()
        root.geometry("850x650")
        root.title("Configuraçoes geral do Sistema")
        root.configure(background='#4876FF')

        self.fonte= ("Times New Roman", 15, "bold")

        self.containerMaster= Frame(root)
        self.containerMaster.place(relx=0.02, rely=0.03, relheight=0.95, relwidth=0.96)
        self.containerMaster.configure(relief=GROOVE)
        self.containerMaster.configure(borderwidth='5')
        self.containerMaster.configure(width=850)
        self.containerMaster.configure(background='#27408B')

        self.Botao1= Button(self.containerMaster)
        self.Botao1.place(relx=0.3, rely=0.1, height=50, width=300)
        self.Botao1.configure(pady='0')
        self.Botao1.configure(text='''ADICIONAR NOVO QUARTO ''')
        self.Botao1.configure(font=self.fonte)

        self.BotaoVoltar= Button(self.containerMaster)
        self.BotaoVoltar.configure(text='''VOLTAR ''')
        self.BotaoVoltar.configure(font=self.fonte)
        self.BotaoVoltar.place(relx=0.45, rely=0.9, width=100)
        self.BotaoVoltar.configure(command= root.destroy)



        root.mainloop()


if __name__ == '__main__':
    ConfigSistema()