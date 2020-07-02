import sys

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
        print(self.PrintaMain())

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
        return listaObj
        

    def PrintaMain(self):
        lista= self.RetornaListObj()
        listaAux= [lista[0], lista[6], lista[4], lista[7]]
        return listaAux

    # def InsereObjLista(self):
    #     lista= self.RetornaListObj()
    #     listaAux= [lista[0], lista[6], lista[4], lista[7]]
    #     listaMain= []
    #     listaMain.append(listaAux)
    #     return ListaMain


