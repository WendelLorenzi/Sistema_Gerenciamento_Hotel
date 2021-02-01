# coding=utf-8

from Tkinter import *
import sys
from Client import RegistraCliente
from datetime import datetime

class Cadastrar:
    def __init__(self):
        root= Tk()
        root.geometry("850x650")
        root.title("Cadastro cliente")
        root.configure(background='#4876FF')

        self.fonte= ("Times New Roman", 15, "bold")

        self.containerMaster= Frame(root)
        self.containerMaster.place(relx=0.02, rely=0.03, relheight=0.95, relwidth=0.96)
        self.containerMaster.configure(relief=GROOVE)
        self.containerMaster.configure(borderwidth='5')
        self.containerMaster.configure(width=850)
        self.containerMaster.configure(background='#27408B')

        self.LabelNome= Label(self.containerMaster)
        self.LabelNome.place(relx=0.04, rely=0.03, height=30, width=250)
        self.LabelNome.configure(font= self.fonte)
        self.LabelNome.configure(text= 'Nome do cliente: ')
        self.LabelNome.configure(background='#27408B')

        self.EntryNome= Entry(self.containerMaster)
        self.EntryNome.place(relx=0.3, rely=0.03, width=500)
        self.EntryNome.configure(font=self.fonte)

        self.LabelTel= Label(self.containerMaster)
        self.LabelTel.place(relx=0.08, rely=0.1, height=30, width=250)
        self.LabelTel.configure(font= self.fonte)
        self.LabelTel.configure(text= 'Telefone: ')
        self.LabelTel.configure(background='#27408B')

        self.EntryTel= Entry(self.containerMaster)
        self.EntryTel.place(relx=0.3, rely=0.1, width=250)
        self.EntryTel.configure(font=self.fonte)

        self.Labelcpf= Label(self.containerMaster)
        self.Labelcpf.place(relx=0.1, rely=0.17, height=30, width=250)
        self.Labelcpf.configure(font= self.fonte)
        self.Labelcpf.configure(text= 'CPF: ')
        self.Labelcpf.configure(background='#27408B')

        self.EntryCpf= Entry(self.containerMaster)
        self.EntryCpf.place(relx=0.3, rely=0.17, width=250)
        self.EntryCpf.configure(font=self.fonte)

        self.LabelTempo= Label(self.containerMaster)
        self.LabelTempo.place(relx=0.000004, rely=0.24, height=30, width=250)
        self.LabelTempo.configure(font= self.fonte)
        self.LabelTempo.configure(text= 'Tempo de hospedagem: ')
        self.LabelTempo.configure(background='#27408B')

        self.LabelTempoDias= Label(self.containerMaster)
        self.LabelTempoDias.place(relx=0.36, rely=0.24, height=30, width=50)
        self.LabelTempoDias.configure(font= self.fonte)
        self.LabelTempoDias.configure(text= 'Dias')
        self.LabelTempoDias.configure(background='#27408B')

        self.EntryTempo= Entry(self.containerMaster)
        self.EntryTempo.place(relx=0.3, rely=0.24, width=50)
        self.EntryTempo.configure(font=self.fonte)

        self.LabelTquarto= Label(self.containerMaster)
        self.LabelTquarto.place(relx=0.04, rely=0.3, height=100, width=250)
        self.LabelTquarto.configure(font= self.fonte)
        self.LabelTquarto.configure(text= 'Tipo de Quarto: ')
        self.LabelTquarto.configure(background='#27408B')

        self.containerCheck= Frame(self.containerMaster)
        self.containerCheck.place(relx=0.30, rely=0.3, height=100, width=200)
        self.containerCheck.configure(background='#27408B')
        self.op1= Label(self.containerCheck)
        self.op2= Label(self.containerCheck)
        self.op3= Label(self.containerCheck)
        self.Checkvar1= IntVar()
        self.Checkvar2= IntVar()
        self.Checkvar3= IntVar()
        self.op1 = Checkbutton(self.containerCheck, text='Individual', variable= self.Checkvar1)
        self.op2 = Checkbutton(self.containerCheck, text='Compartilhado', variable= self.Checkvar2)
        self.op3= Checkbutton(self.containerCheck, text='Luxo', variable= self.Checkvar3)
        self.op1.place(relx=0.001, rely=0.01, height=30, width=150)
        self.op1.configure(background='#27408B')
        self.op2.place(relx=0.001, rely=0.3, height=30, width=150)
        self.op2.configure(background='#27408B')
        self.op3.place(relx=0.001, rely=0.55, height=30, width=150)
        self.op3.configure(background='#27408B')

        self.LabelNumeroQ= Label(self.containerMaster)
        self.LabelNumeroQ.place(relx=0.020, rely=0.47, height=30, width=250)
        self.LabelNumeroQ.configure(font= self.fonte)
        self.LabelNumeroQ.configure(text= 'Número do Quarto: ')
        self.LabelNumeroQ.configure(background='#27408B')

        self.EntryQuarto= Entry(self.containerMaster)
        self.EntryQuarto.place(relx=0.3, rely=0.47, width=50)
        self.EntryQuarto.configure(font=self.fonte)

        self.BotaoSalvar= Button(self.containerMaster)
        self.BotaoSalvar.configure(text='''SALVAR ''')
        self.BotaoSalvar.configure(font=self.fonte)
        self.BotaoSalvar.place(relx=0.35, rely=0.6, width=100)
        self.BotaoSalvar.configure(command= self.Imprime)

        self.BotaoVoltar= Button(self.containerMaster)
        self.BotaoVoltar.configure(text='''VOLTAR ''')
        self.BotaoVoltar.configure(font=self.fonte)
        self.BotaoVoltar.place(relx=0.55, rely=0.6, width=100)
        self.BotaoVoltar.configure(command= root.destroy)

        root.mainloop()

    def Imprime(self):
        RegistraCliente((str(self.EntryNome.get())),
        (str(self.EntryTel.get())),
        (str(self.EntryCpf.get())),
        (int(self.EntryTempo.get())),
        (int(self.EntryQuarto.get())),
        (self.Verify_check()),
        (self.DataEntrada()),
        '0k')
        self.ClearEntry()

    def DataEntrada(self):
        data_e_hora_atuais = datetime.now()
        data_e_hora = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        return data_e_hora
    

    def ClearEntry(self):
        self.EntryNome.delete(0, 'end')
        self.EntryTel.delete(0, 'end')
        self.EntryCpf.delete(0, 'end')
        self.EntryTempo.delete(0, 'end')
        self.EntryQuarto.delete(0, 'end')
        self.Checkvar1.set(0)
        self.Checkvar2.set(0)
        self.Checkvar3.set(0)

    def Verify_check(self):
        if(self.Checkvar1.get() != 0): return 1
        if(self.Checkvar2.get() != 0): return 2
        if(self.Checkvar3.get() != 0): return 3

    def chamar():
        print('Fui chamado!')


if __name__ == '__main__':
    Cadastrar()