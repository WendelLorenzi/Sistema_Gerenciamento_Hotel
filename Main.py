# coding=utf-8

from Tkinter import *
import sys
from PacketHostel.Cliente.Cadastro import Cadastrar
from PacketHostel.Cliente.Saida import DarSaida
from PacketHostel.Cliente.Info import InfoCliente
from PacketHostel.Sistema.Login import LoginAdmSistema
from PacketHostel.Sistema.Gerencial import ConfigSistema
from PacketHostel.Cliente.Client import RegistraCliente
class Hotel_Gerenciamento:
    def __init__(self):
        root= Tk()
        root.geometry("850x650")
        root.title("Sistema Gerenciamento")
        root.configure(background='#4876FF')

        self.containerMaster= Frame(root)
        self.containerMaster.place(relx=0.02, rely=0.03, relheight=0.95, relwidth=0.96)
        self.containerMaster.configure(relief=GROOVE)
        self.containerMaster.configure(borderwidth='5')
        self.containerMaster.configure(width=850)
        self.containerMaster.configure(background='#27408B')

        self.MensagemIni= Message(self.containerMaster)
        self.MensagemIni.place(relx=0.00, rely=0.00, relheight=0.1, relwidth=1.0)
        self.MensagemIni.configure(text='''Projeto - Sistema Gerenciamento de Hotel''')
        self.MensagemIni.configure(font=("Times New Roman", 25, "bold"))
        self.MensagemIni.configure(width=700)
        self.MensagemIni.configure(background='#27408B')


        self.Botao1= Button(self.containerMaster)
        self.Botao1.place(relx=0.04, rely=0.15, height=50, width=300)
        self.Botao1.configure(pady='0')
        self.Botao1.configure(text='''DAR ENTRADA ''')
        self.Botao1.configure(font=("Times New Roman", 10, "bold"))
        self.Botao1.configure(command= Cadastrar)

        self.Botao2= Button(self.containerMaster)
        self.Botao2.place(relx=0.04, rely=0.27, height=50, width=300)
        self.Botao2.configure(pady='0')
        self.Botao2.configure(text='''DAR SAÍDA ''')
        self.Botao2.configure(font=("Times New Roman", 10, "bold"))
        self.Botao2.configure(command= DarSaida)


        self.Botao3= Button(self.containerMaster)
        self.Botao3.place(relx=0.04, rely=0.39, height=50, width=300)
        self.Botao3.configure(pady='0')
        self.Botao3.configure(text='''INFORMAÇõES DO CLIENTE ''')
        self.Botao3.configure(font=("Times New Roman", 10, "bold"))
        self.Botao3.configure(command= InfoCliente)

        self.Botao4= Button(self.containerMaster)
        self.Botao4.place(relx=0.04, rely=0.51, height=50, width=300)
        self.Botao4.configure(pady='0')
        self.Botao4.configure(text='''CONFIGURAÇÕES DO SISTEMA ''')
        self.Botao4.configure(font=("Times New Roman", 10, "bold"))
        self.Botao4.configure(command= ConfigSistema)

        self.Botao5= Button(self.containerMaster)
        self.Botao5.place(relx=0.04, rely=0.63, height=50, width=300)
        self.Botao5.configure(pady='0')
        self.Botao5.configure(text=''' FUNÇOES ADMINISTRATIVAS ''')
        self.Botao5.configure(font=("Times New Roman", 10, "bold"))
        self.Botao5.configure(command= LoginAdmSistema)

        self.Botao6= Button(self.containerMaster)
        self.Botao6.place(relx=0.04, rely=0.75, height=50, width=300)
        self.Botao6.configure(pady='0')
        self.Botao6.configure(text='''REALIZAR PAGAMENTO ''')
        self.Botao6.configure(font=("Times New Roman", 10, "bold"))

        self.Botao7= Button(self.containerMaster)
        self.Botao7.place(relx=0.04, rely=0.87, height=50, width=300)
        self.Botao7.configure(pady='0')
        self.Botao7.configure(text='''SAIR ''')
        self.Botao7.configure(font=("Times New Roman", 10, "bold"))
        self.Botao7.configure(command= root.destroy)

        self.containerListaC= Frame(root)
        self.containerListaC.place(relx=0.45, rely=0.18, relheight=0.75, relwidth=0.5)
        self.containerListaC.configure(relief=GROOVE)
        self.containerListaC.configure(borderwidth='5')

        self.ListaClientes= Text(self.containerListaC)
        self.ListaClientes.place(relx=0.01, rely=0.1, relheight=0.88, relwidth=0.98)
       # self.ListaClientes.insert(INSERT, RegistraCliente.ListaMain)

        self.LabelInfoCliente= Label(self.containerListaC)
        self.LabelInfoCliente.place(relx=0.1, rely=0.01, height=40, width=350)
        self.LabelInfoCliente.configure(font=("Times New Roman", 10, "bold"))
        self.LabelInfoCliente.configure(text= 'Nome  -  Data e hora de Entrada  -  Quarto  -  Pagamento ')

        root.mainloop()


if __name__ == '__main__':
    Hotel_Gerenciamento()