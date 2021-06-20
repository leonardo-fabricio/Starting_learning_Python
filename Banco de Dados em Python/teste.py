# COMANDOS DCL
#REVOKE
#GRANT
#====================================


import os
from sqlite3.dbapi2 import connect
os.remove("escola.db") if os.path.exists("escola.db") else None

import sqlite3

con = sqlite3.connect('escola.db')
cur = con.cursor()  

print(type(con))
print(type(cur))

query_create = 'create table cursos ( id integer primary key, nome varchar(30), cat varchar(50))'
cur.execute(query_create)

sql_insert = 'insert into cursos values (?, ?, ?)'
dados = [(1000,"python","a"),(1001,"POO","b"),(1002,"Arquitetura de Software","c")]

for x in dados:
    cur.execute(sql_insert,x)

con.commit()

query = 'select * from cursos'
cur.execute(query) #Armazena os dados do banco nessa funcao fetchall
dados = cur.fetchall()

for x in dados:
    print(x)

con.close()