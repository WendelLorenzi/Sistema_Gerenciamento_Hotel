from tkinter import *
import sys
import bcrypt
from BD.Conecta_db import Banco 
from Sistema.Financa import TelaGerenciaF

class LoginAdmSistema:
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
        self.BotaoSalvar.configure(text='''ENTRAR ''')
        self.BotaoSalvar.configure(font=("Times New Roman", 10, "bold"))
        self.BotaoSalvar.place(relx=0.5, rely=0.4, width=90)
        self.BotaoSalvar.configure(command= self.verificaUser)

        self.BotaoSair= Button(self.containerMaster)
        self.BotaoSair.configure(text='''VOLTAR ''')
        self.BotaoSair.configure(font=("Times New Roman", 9, "bold"))
        self.BotaoSair.place(relx=0.53, rely=0.5, width=70)
        self.BotaoSair.configure(command= root.destroy)

        root.mainloop()

    def GeraHash(self):
        hashed = bcrypt.hashpw(str(self.getSenha()).encode('utf-8'), bcrypt.gensalt())
        return hashed
    
    def getUser(self):
        return self.EntryUser.get()

    def getSenha(self):
        return self.EntrySenha.get()
    
    def EnviaBD(self):
        list= [self.getUser(), self.GeraHash()]
        Banco().InsereUser(list)
    
    def verificaUser(self):
        user= self.getUser()
        print(user)
        if(len(user) != 0):
            passou= Banco().VerificaUser(user)
        if(passou == 'ok'):
            self.verificaSenha()
        else:
            self.ErroEntrar(1)
    
    def verificaSenha(self):
        senha= self.getSenha()
        print(senha)
        passouSh= ()
        # Busca as hashes do banco e insere
        passouSh= Banco().BuscaHash()
        for hash_separada in passouSh:
            #passa a tupla de posição i da lista(passouSh) 
            print('hash_banco: ', hash_separada[0])
            achou= 0
            if(self.CompareHash(senha, hash_separada[0]) == True):
                print('O banco de dados continha o hash da senha')
                achou= 1
                TelaGerenciaF()
                break
                if(achou != 1):
                    self.NaoEncontrouHash()
    
    def CompareHash(self, nome, hash):
        verifica= bcrypt.checkpw(nome.encode('utf-8'), hash)
        return verifica
                


    def NaoEncontrouHash(self):
        print('Não achou no banco')
        self.ErroEntrar(2)
            
    def ErroEntrar(self, caso):
        if(caso == 1):
            LabelErro= Label(self.containerMaster)
            LabelErro.place(relx=0.2, rely=0.7, height=30, width=250)
            LabelErro.configure(font=("Times New Roman", 10))
            LabelErro.configure(text= 'Usuário não encontrado')
            LabelErro.configure(background='#27408B')
            self.EntryUser.delete(0, 'end')
        if(caso == 2):
            LabelErro= Label(self.containerMaster)
            LabelErro.place(relx=0.2, rely=0.7, height=30, width=250)
            LabelErro.configure(font=("Times New Roman", 10))
            LabelErro.configure(text= 'Senha Errada')
            LabelErro.configure(background='#27408B')
            self.EntrySenha.delete(0, 'end')


            


if __name__ == '__main__':
    LoginAdmSistema()