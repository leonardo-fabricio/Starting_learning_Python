# ## QUESTAO 1
# lista = [1,2,3,4,5,6,7,8,9,10]
# # for x in lista:
# # 	print(x)

# # lista.sort(reverse = True)
# # print(lista)

# ##QUESTAO 2

# lista2= [1,2,"leonardo",[2, 3],True]

# # for x in lista2:
# #  	print(x)

# # QUESTAO 3

# # a = "leo"
# # b = "nardo"

# # c = a+b
# # print(c)

# #QUESTAO 4

# # tup = (1,2,3,4,4,4,5)
# # print(tup.count(6))



# # QUESTAO 5 E 6 E 7

# dic = {1:"", 2:"eh o 2", 3:"eh o 3"}
# dic2 = {"jose":42, "maria":25, "antonio":56}
# # print(dic[2])

# # dic[3] = "aaaaaaa"

# #fora a parteeeeeeee
# # dic.update(dic2)
# # print(dic.keys())
# # print(dic2.keys())

# #QUESTAOO 8

# # dic3 = {1:"leonardo", 2:"Euzimaria", 4:[5,2]}

# # print(dic3[4])

# #QUESTAO 9

# # lista3 = ["leo",("lindo",21),{"K1":"values1", 9:"values2"}, 18.25]
# # print(lista3[2]["K1"])

# #QUESTAO 10 

# frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

# x = 1
# while x<=18:
# 	print(frase[x])
# 	x=x+1

# ESTUDO DO PYTHON
# x = 0
# if(x==0):
# 	print("opção 1")
# elif(x==1):
# 	print("opção 2")
# else:
# 	print("opção 3")

# a = (input("digite um valor para a: "))
# b = (input("digite um valor para b: "))
# c = int(a) + int(b)
# print(c)

# a = ["lista1","lista2", 2]

# for x in a:
# 	if x == 2:
# 		print(x)
# 	else:
# 		print('nao achei')


#num intervalo de 0 a 101 andando de 2 em 2
# for x in range(0,101,2):
# 	print(x	)

# for x in "E a italia deu-lhe a bota":
# 	if x == "a":
# 		print(x)
# 	else:
# 		print("---")

# boublesort PYTHON
						# lista = [1,2,3,4,5,6,7,8,0]
						# for x in range(0,9,1):
						# 	for y in range(0,9-x,1):
	#ERRADO				# 		aux = lista[y]
						# 		if(aux <= lista[y]):
						# 			lista[y] = aux		

						# print(lista)


# count = 0 
# while count < 10:
# 	if count == 8:
# 		break
# 	else:
# 		pass
# 		print("o valor e: ",count)
# 		count+=1

# lst = [1,2,3,4,5,6,7,8,9,10]
# lst.append(2)

# #print(lst)
# help(lst.append(3))

# for x in dir(lst):
# 	if(x!=","):
# 		print(x)


#FUNÇOES EM PYTHON

	# def primeirafun(strg):
	# 	print(strg)

	# def soma (a,b):
	# 	return a+b

	# primeirafun(soma(1,4))


# QUEBRANDO	# def split_string (nome): 
# STRINGS	# 	return nome.split(" ")
			# strg = "asasas asasasd dsdsdsd erererer e544t4t4"
			# print(split_string(strg))

# def fun1(arg, *vartuple): VAI PERMITIR RECEBER VARIOS ARGUMENTOS 
# 	print(arg)
# for item in vartuple:  VAI RECEBER O PARAMETRO VARTUPLE E EXECUTALO CONFORMW O CODIGO
# 	print(item)

# COMPARANDO FUNCOES LAMBDAS E NORMAIS
# def potencia(num) : return num**2
# potencia = lambda num: num**2

# soma  = lambda num1, num2: num1+num2
# print(soma(2,4))

# dia = input("Qual o dia da semana hoje? ")
# if dia == "domingo" or dia== "Domingo" or dia == "Sabado" or dia == "Sábado" or dia =="sábado" or dia =="sabado":
# 	print("Hoje eh dia de descanso")
# else:
# 	print("CUIDE CUIDE TA NA HORA DO TRABALHO")

# lista=["pêra","manga","uva","morango","limão"]
# for x in lista:
# 	if x == "morango" or x=="Morango":
# 		print("======\n======\n")

# placeholde em python
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# EXEMPLO DE PLACEHOLDER PARA APRESENTAR QUANTAS VEZES UM CARACTERE APARECE
# r = "r"
# st = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
# txt = "O total de vezes q a letra " + r + " aparece eh: {total:.2f}"
# print(txt.format(total = st.count(r)))


#================================TRABALHANDO COM ARQUIVOS==============================================

#arq1 = open("arquivo.txt","r")  ABRINDO PARA LEITURA
# print(arq1.read())
# print(arq1.tell()) #contar o numero de caracteres
# print(arq1.seek(0,0)) # acessar um ponto especifico

#arq1 = open("PYTHON/arquivo.txt","w") #ABRINDO PARA ESCRITA
# print("Cadastro de usuario!!!\n")
# print("Porfavor preencha seus dados para realizar cadastro!!!\n")
# nome = input("NOME: \n")
# cidade = input("CIDADE: \n")
# nascimento= input("NASCIMENTO: \n")
# email= input("EMAIL: \n")
# senha= input("SENHA: \n")

	
# arq1.write(nome+"\n"+cidade+"\n"+ nascimento+"\n"+email+"\n"+senha+"\n------------------------------")

#================ Pegando uma string qualquer, quebrando e colocando no arquivo
# txt = "EU QUERO TE DAR A PAZ DO MEU SENHOR COM MUITO AMOR"
# for x in txt.split():
# 	arq1.write(x)