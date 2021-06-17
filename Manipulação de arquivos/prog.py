#============================================ ARQUIVOS TXT

# #====================================================== 
arq1 = open("arquivo.txt","w") #ABRINDO PARA ESCRITA
print("Cadastro de usuario!!!\n")
print("Porfavor preencha seus dados para realizar cadastro!!!\n")
nome = input("NOME: \n")
cidade = input("CIDADE: \n")
nascimento= input("NASCIMENTO: \n")
email= input("EMAIL: \n")
senha= input("SENHA: \n")
	
arq1.write(nome+"\n"+cidade+"\n"+ nascimento+"\n"+email+"\n"+senha+"\n------------------------------")
# #======================================================

import os
#Escreve no arquivo todas as palavras da string, separada po \n
arquivo = open(os.path.join("arquivo.txt"),"w") #LEMBRANDO QUE O "w" ABRE O ARQUIVO PARA ESCRITA
txt = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
for x in txt.split():
	arquivo.write(x+"\n")

arquivo.close()

#ler dados do arquivo
arquivo = open(os.path.join("arquivo.txt"),"r")
print(arquivo.read())

#Outra Maneira de ler dados de um arquivo
with open("arquivo.txt", "r") as arquivo:
	txt = arquivo.read()
print(txt)

arquivo.close()

a = "askkaskdaks aksaksdkksdkas kaskaksk"
with open("arquivo.txt","w") as arquivo:
	arquivo.write(a[:4]) #Escrever dados da variavel ate o 4 caractere
	arquivo.write("\n")
	arquivo.write(a[:10]) #Escrever dados da variavel ate o 10 caractere
		
#============================================ ARQUIVOS CSV

import csv
with open("arquivo.csv","w") as arquivo:
	w = csv.writer(arquivo) #definindo que a variavel writer var poder modificar "arquivo"
	w.writerow(("primeira","segunda","terceira"))	
	w.writerow(("98","89","44","20"))

arquivo.close()

with open("arquivo.csv", "r") as arquivo:
	#print(arquivo.read())
	txt = csv.reader(arquivo) 
	dados= list(txt)

print (dados)

for x in dados:
	print(x)

#============================================ ARQUIVOS JSON

import json

dicio = {1:"Item 1",2:"Item 2",3:"Item 3",4:"Item 4"}
json.dumps(dicio)

with open("arquivo.json", "w") as arquivo:
	arquivo.write(json.dumps(dicio))

arquivo.close()

with open("arquivo.json","r") as arquivo:
	print(arquivo.read())

arquivo.close()
