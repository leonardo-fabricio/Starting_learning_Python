import sqlite3
import random
from sqlite3.dbapi2 import Cursor
import time
import datetime
import matplotlib.pyplot as plt 


class Banco():
    def __init__(self,banco):
        self.query = ''
        self.conn = sqlite3.connect(banco)
        self.cursor = self.conn.cursor()

    def create_table_f(self):
        query = 'create table if not exists funcionarios (id interger primary key not null, nome varchar(20))'
        self.cursor.execute(query)

    def create_table_p(self):
        query = 'create table if not exists produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome varchar(20), preco varchar(30), data date)'
        self.cursor.execute(query)

    def insert_table(self,dados,op):
        sql_insert = ' '
        if op == 0:
            sql_insert = 'insert into funcionarios values (?, ?)'
        else:
            sql_insert = 'insert into produtos values (?, ?, ?, ?)'
        
        for x in dados:
            self.cursor.execute(sql_insert,x)
        self.conn.commit()
        self.conn.close()

    def select_todos_dados(self,op):
        if op == 0:
            self.query = 'select * from produtos'
        else:
            self.query = 'select * from funcionarios'
        self.cursor.execute(self.query)
        for x in self.cursor.fetchall():
            print(x)
        print("\n")
    
    def atualizar_dados(self):
        self.query = "update produtos set preco = 100 where id = 10"
        self.cursor.execute(self.query)
        self.conn.commit()

    def excluir_tupla(self,id):
        self.query = 'delete from produtos where id = ' + str(id)
        self.cursor.execute(self.query)
        self.conn.commit()
    
    def grafico(self):
        self.query = 'select id,preco from produtos'
        self.cursor.execute(self.query)
        ids = []
        precos = []
        dados = self.cursor.fetchall()

        for x in dados:
            ids.append(x[0])
            precos.append(x[1])

        plt.bar(ids,precos)
        plt.show()
       
    
data = datetime.datetime.now()
dados = [(11,"MONITOR",random.randrange(50,100),data),(31,"MOUSE",random.randrange(50,100),data),(21,"TECLADO",random.randrange(50,100),data),(42,"CADEIRA GAMER",random.randrange(50,100),data)]
obj = Banco("escola.db")

# obj.create_table_p()
#obj.insert_table(dados,1)

#OPTANDO ENTRE 1 E 0 ELE IMPRIME OS DADOS DE DETER TABELAS
# obj.select_todos_dados(0)

#ATUALIZANDO DADOS
# obj.atualizar_dados()
# obj.select_todos_dados(0)

#REMOVENDO DADOS
obj.excluir_tupla(0)
# obj.select_todos_dados(0)

#GERANDO GRAFICO
obj.grafico() 

