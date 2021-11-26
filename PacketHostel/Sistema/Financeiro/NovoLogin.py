
# coding=utf-8

from tkinter import *
import sys
import bcrypt
from PacketHostel.BD.Conecta_db import Banco 


class NewUser:
    def __init__(self):
        root= Tk()
        root.geometry("500x500")
        root.title("Configuraçoes geral do Sistema")
        root.configure(background='#4876FF')

        self.fonte= ("Times New Roman", 15, "bold")

        self.containerMaster= Frame(root)
        self.containerMaster.place(relx=0.02, rely=0.03, relheight=0.95, relwidth=0.96)
        self.containerMaster.configure(relief=GROOVE)
        self.containerMaster.configure(borderwidth='10')
        self.containerMaster.configure(width=300)
        self.containerMaster.configure(background='#27408B')

        self.LabelUser= Label(self.containerMaster)
        self.LabelUser.place(relx=0.0009, rely=0.2, height=30, width=250)
        self.LabelUser.configure(font= self.fonte)
        self.LabelUser.configure(text= 'Usuário: ')
        self.LabelUser.configure(background='#27408B')

        self.EntryUser= Entry(self.containerMaster)
        self.EntryUser.place(relx=0.38, rely=0.2, width=200)
        self.EntryUser.configure(font=self.fonte)

        self.LabelSenha= Label(self.containerMaster)
        self.LabelSenha.place(relx=0.0009, rely=0.3, height=30, width=250)
        self.LabelSenha.configure(font= self.fonte)
        self.LabelSenha.configure(text= 'Senha: ')
        self.LabelSenha.configure(background='#27408B')

        self.EntrySenha= Entry(self.containerMaster, show='*')
        self.EntrySenha.place(relx=0.38, rely=0.3, width=200)
        self.EntrySenha.configure(font=self.fonte)

        self.BotaoSalvar= Button(self.containerMaster)
        self.BotaoSalvar.configure(text='''SALVAR ''')
        self.BotaoSalvar.configure(font=("Times New Roman", 10, "bold"))
        self.BotaoSalvar.place(relx=0.5, rely=0.4, width=90)
        self.BotaoSalvar.configure(command= self.EnviaBD)

        self.BotaoSair= Button(self.containerMaster)
        self.BotaoSair.configure(text='''VOLTAR ''')
        self.BotaoSair.configure(font=("Times New Roman", 9, "bold"))
        self.BotaoSair.place(relx=0.53, rely=0.5, width=70)
        self.BotaoSair.configure(command= root.destroy)

        root.mainloop()

    def GeraHash(self, senha='a'):
        if(senha == 'a'):
            hashed = bcrypt.hashpw(str(self.getSenha()).encode('utf-8'), bcrypt.gensalt())
        else:
            hashed = bcrypt.hashpw(str(senha).encode('utf-8'), bcrypt.gensalt())
        return hashed
    
    def getUser(self):
        return self.EntryUser.get()
    def getSenha(self):
        self.EntrySenha.get()
    
    def EnviaBD(self):
        list= [self.getUser(), self.GeraHash()]
        inserido= Banco().InsereUser(list)
        if (inserido != 1):
            self.ErroEntrar(1)
        else:
            self.ErroEntrar(2)

    
    def ErroEntrar(self, caso):
        if(caso == 1):
            LabelErro= Label(self.containerMaster)
            LabelErro.place(relx=0.2, rely=0.7, height=30, width=250)
            LabelErro.configure(font=("Times New Roman", 10))
            LabelErro.configure(text= 'Erro ao cadastrar no Banco de Dados')
            LabelErro.configure(background='#27408B')
            self.EntryUser.delete(0, 'end')
            self.EntrySenha.delete(0, 'end')
        if(caso == 2):
            LabelErro= Label(self.containerMaster)
            LabelErro.place(relx=0.2, rely=0.7, height=30, width=250)
            LabelErro.configure(font=("Times New Roman", 10))
            LabelErro.configure(text= 'Usuário Cadastrado com Sucesso')
            LabelErro.configure(background='#27408B')

if __name__ == '__main__':
    NewUser()