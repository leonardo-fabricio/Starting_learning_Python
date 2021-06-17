arq1 = open("arquivo.txt","w") #ABRINDO PARA ESCRITA
print("Cadastro de usuario!!!\n")
print("Porfavor preencha seus dados para realizar cadastro!!!\n")
nome = input("NOME: \n")
cidade = input("CIDADE: \n")
nascimento= input("NASCIMENTO: \n")
email= input("EMAIL: \n")
senha= input("SENHA: \n")

	
arq1.write(nome+"\n"+cidade+"\n"+ nascimento+"\n"+email+"\n"+senha+"\n------------------------------")