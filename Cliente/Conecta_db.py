import sqlite3
import os

class Banco:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('hotel.db')
        except error:
            print('erro ao conectar banco')
        self.cursor = self.conn.cursor()


    def InsereLista(self, lista):
        self.cursor.executemany("""
            INSERT INTO clientes (Nome, Telefone, cpf, Tempo_hospedagem, Numero_quarto, Tipo_quarto, Data_entrada, Pagamento)
            VALUES (?,?,?,?,?,?,?,?)
            """, [lista])
        self.conn.commit()
        print('Dados inseridos com sucesso.')

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

# print('Tabela criada com sucesso.')
# # desconectando...

        self.conn.close()