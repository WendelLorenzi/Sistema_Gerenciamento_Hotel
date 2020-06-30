from tkinter import *
import sys

class InfoCliente:
    def __init__(self):
        root= Tk()
        root.geometry("850x650")
        root.title("Informaçoes do Cliente")
        root.configure(background='#4876FF')

        self.fonte= ("Times New Roman", 15, "bold")

        self.containerMaster= Frame(root)
        self.containerMaster.place(relx=0.02, rely=0.03, relheight=0.95, relwidth=0.96)
        self.containerMaster.configure(relief=GROOVE)
        self.containerMaster.configure(borderwidth='5')
        self.containerMaster.configure(width=850)
        self.containerMaster.configure(background='#27408B')

        self.LabelBusca= Label(self.containerMaster)
        self.LabelBusca.place(relx=0.04, rely=0.03, width=250)
        self.LabelBusca.configure(font= self.fonte)
        self.LabelBusca.configure(text= 'Digite o CPF: ')
        self.LabelBusca.configure(background='#27408B')

        self.EntryBusca= Entry(self.containerMaster)
        self.EntryBusca.place(relx=0.3, rely=0.03, width=500)
        self.EntryBusca.configure(font=self.fonte)

        self.BotaoBuscar= Button(self.containerMaster)
        self.BotaoBuscar.configure(text='''BUSCAR ''')
        self.BotaoBuscar.configure(font=self.fonte)
        self.BotaoBuscar.place(relx=0.5, rely=0.12, width=100)
        self.BotaoBuscar.configure(command= self.Abre)

        self.BotaoVoltar= Button(self.containerMaster)
        self.BotaoVoltar.configure(text='''VOLTAR ''')
        self.BotaoVoltar.configure(font=self.fonte)
        self.BotaoVoltar.place(relx=0.5, rely=0.9, width=100)
        self.BotaoVoltar.configure(command= root.destroy)

        root.mainloop()

    # def BuscaCPF(self, str(EntryBusca.get())):
    #     if(Encontrado):
    #         return 1
    

    # def AbreEncontrado(self, inteiro):
    #     if(inteiro == 1):
    
    def Abre(self):
        containerBaixo= Frame(self.containerMaster)
        containerBaixo.place(relx=0.2, rely=0.25, relheight=0.6, relwidth=0.65)
        containerBaixo.configure(relief=GROOVE)
        containerBaixo.configure(borderwidth='5')
        containerBaixo.configure(width=600)
        containerBaixo.configure(background='#27408B')





if __name__ == '__main__':
    InfoCliente()