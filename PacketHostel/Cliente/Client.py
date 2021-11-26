# coding=utf-8

import sys
sys.path.append('PacketHostel/BD')
from PacketHostel.BD.Conecta_db import Banco

class RegistraCliente:
    def __init__(self, NomeH, TelH, CpfH, TempoH, NumeroQ, TipoQ, DataEntrada, Pagamento):
        self.Nome= NomeH
        self.Tel= TelH
        self.Cpf= CpfH
        self.Tempo= TempoH
        self.Numero= NumeroQ
        self.Tipo= TipoQ
        self.Data= DataEntrada
        self.SitPagamento= Pagamento
        print(self.RetornaListObj())
        #print(self.ListaMain())

    def getNome(self):
        return self.Nome

    def getTel(self):
        return self.Tel

    def getCpf(self):
        return self.Cpf

    def getTempoH(self):
        return self.Tempo

    def getNumeroQ(self):
        return self.Numero

    def getTipoQ(self):
        return self.Tipo

    def getDataEntrada(self):
        return self.Data

    def getSituacaoPagm(self):
        return self.SitPagamento

    def RetornaListObj(self):
        listaObj= [self.getNome(), self.getTel(), self.getCpf(), self.getTempoH(), self.getNumeroQ(), self.getTipoQ(), self.getDataEntrada(), self.getSituacaoPagm()]
        Banco().InsereLista(listaObj)
        return listaObj

  

    # def ListaMain(self):
    #     lista= self.RetornaListObj()
    #     listaAux= [lista[0], lista[6], str(lista[4]), lista[7]]
    #     return ('- '.join(map(str, listaAux)))


