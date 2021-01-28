# coding=utf-8

import sqlite3
import os

class Banco:
    def __init__(self):
        self.cursor= self.IniciaBD()
        ##self.CriaTabela(self.cursor)
    
    
    def IniciaBD(self):
        try:
            self.conn = sqlite3.connect('BD/hotel.db')
        except error:
            print('erro ao conectar banco')
        return self.conn.cursor()
    
    def EncerraBD(self):
        self.conn.close()

    def InsereLista(self, lista):
        self.cursor.executemany("""
            INSERT INTO clientes (Nome, Telefone, cpf, Tempo_hospedagem, Numero_quarto, Tipo_quarto, Data_entrada, Pagamento)
            VALUES (?,?,?,?,?,?,?,?)
            """, [lista])
        self.conn.commit()
        print('Dados inseridos com sucesso.')
        self.EncerraBD()
    
    def InsereUser(self, lista):
        self.cursor.executemany("""
            INSERT INTO UsersADM (user, hash_senha)
            VALUES (?,?)
            """, [lista])
        self.conn.commit()
        print('Dados inseridos com sucesso.')
        self.EncerraBD()
        return 1

    def VerificaUser(self, user):
        self.cursor.execute('''select 'ok'
                                from UsersADM 
                                where user= ?''', [user])
        for linha in self.cursor.fetchall():
            if(len(linha) != 0):
                return 'ok'
        self.EncerraBD()



# # criando a tabela (schema)
# cursor.execute("""
# CREATE TABLE clientes (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         Nome TEXT NOT NULL,
#         Telefone TEXT,
#         cpf     VARCHAR(14) NOT NULL,
#         Tempo_hospedagem INTEGER NOT NULL,
#         Numero_quarto INTEGER,
#         Tipo_quarto INTEGER,
#         Data_entrada TEXT NOT NULL,
#         Pagamento TEXT NOT NULL
# );
# """)

# cursor.execute("""
#             CREATE TABLE UsersADM (
#                 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 user text NOT NULL,
#                 hash_senha text NOT NULL
#             );
#             """)
#         print('Tabela criada com sucesso.')




    # criando a tabela (schema)
    
    # def CriaTabela(self, cursor):
    #     cursor.execute("""
    #         CREATE TABLE UsersADM (
    #             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #             user text NOT NULL,
    #             hash_senha text NOT NULL
    #         );
    #         """)
    #     print('Tabela criada com sucesso.')


    def BuscaHash(self):
        self.cursor.execute('''select hash_senha
                        from UsersADM;''')
        rec= []
        for linha in self.cursor.fetchall():
            rec.append(linha)
            # retorna uma tupla
        return rec
        self.EncerraBD()
# if __name__ == '__main__':
#     Banco()