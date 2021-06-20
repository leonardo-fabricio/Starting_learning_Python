from pymongo import MongoClient
import datetime

conn = MongoClient('localhost',27017) #CRIANDO CONEXAO
db = conn.cadastrodb #CRIANDO BASE DE DADOS
coletion = db.cadastrodb  #CRIANDO UMA COLLETION

# print(type(conn))
# print(type(coletion))

#DICIONARIOS OU ARQUIVO EM FORMATO JSON
dic = {"1":"value1","2":"value2","4":datetime.datetime.utcnow()}
dic2 = {"8":"value4","7":"value6","6":datetime.datetime.utcnow()}

coletion = db.posts #NOME DA COLETION

#INSERINDO DADOS DO DICIONARIO 1
post_id = coletion.insert_one(dic)
# print(post_id.inserted_id)

#INSERINDO DADOS DO DICIONARIO 2
post_id = coletion.insert_one(dic2)
# print(post_id.inserted_id)

#EXIBINDO DADOS
# for x in coletion.find():
#     print(x)

#EXIBINDO NOMA DA BASE DE DADOS
# print(db.name)
#EXIBINDO NOME DAS COLLECTIONS
# print(db.list_collection_names())


#===================================================

# RECUPERANDO DADOS MONGO DB

client_con = MongoClient()

# print(client_con.database_names())

db2 = client_con.cadastrodb #ESSE OBJT PERMITE O MANUSERIO NA BASE DE DADOS SELECIONADA

print(db2.list_collection_names())

#CRIANDO UMA NOVA COLLECTION PARA A BASE DE DADOS
# db2.create_collection("mycollection")

#INSERINDO VALORES EM UMA COLLECTION  =  <basededados>.<MinhaCollection>.insert_one
db2.mycollection.insert_one({'titulo':'Mongo DB em Python','descricao':'...','by':'Data Science Academy','url':'https://www.google.com'})

#EXIBINDO DADOS DA COLLECTION
for x in db2.mycollection.find():
    print(x)

#CONECTANDO A UMA COLEÇAO
col = db2["mycollection"]

#MANEIRA DE IMPRIMIR QUANTAS "TUPLAS" EXISTE DENTRO DAS COLLECTION
#print(col.count())
# print(col.estimated_document_count())

#TRANFERINDO O VALOR DE UMA LINHA DA COLLECTION PARA UM DICIONARIO
dicio_aux = col.find_one()

#IMPRIMINDO CHAVES E VALORES DESSE DICIONARIO
for x, y in dicio_aux.items():
    print(x,y)