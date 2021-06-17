# FUNCAO MAP - APLICA DETERMINADA FUNCAO A CADA ELEMENTO DA LISTA
def fah (t):
	return ((t*1.8)+32)
def cel (t):
	return ((t-32)/1.8)

lista_t = [20, 18.5,37,42,19]
print(map(fah,lista_t))

# #METODO #1
lista2 = list(map(fah,lista_t))
print(lista2)

# #METODO #2
for x in map(fah,lista_t):
	print(x)
for y in map(cel,lista_t):
	print(y)

#FUNCAO REDUCE - APLICA REDUÇÕES

from functools import reduce
lista = [1,3,5,3,2,5,3,43,2,21,43,54,56]

def soma(a,b):
	return a+b

#print(reduce(soma,lista)) #FAZ A SOMA DE TODOS OS ELEMENTOS DA LISTA
#print(reduce (lambda x,y: x+y, lista))

#METODO #1
def maiorE (x):
	aux = 0
	for y in x: 
		aux = y
		if y > aux: aux = y

	return aux
#print(maiorE(lista))

#METODO #2
maiorElemento = lambda a, b: a if a > b else b #RETORNA A SE A>B E SE NAO B
#print(maiorElemento(5,2))
#print(reduce(maiorElemento,lista))

#FUNCAO FILTER - APLICA FILTROS NA FUNÇÃO

par = lambda x: True if (x % 2 == 0) else False
#print(par(5))
lista = [21,3,4,5,3,2,2,4,2,35,8,65,3,4]

print(list(filter(par,lista))) #RETORNA APENAS OS PARES

#FUNCAO ZIP - UNE CADA ELEMENTO COM CADA ELEMENTO DE DETERMINDAS LISTAS

x = ["a",1,4,6]
y = [2,54,"b"]

z = list(zip(x,y))
print(z) #UNE O PRIMEIRO COM PRIMEIRO SEGUNDO COM SEGUNDO...

#FUNCAO ENUMERATE - ENUMERA OS INDICES 
lista  = [232,43,76,54,43]
print(list(enumerate(lista)))

#PODESSE USAAR PARA PESQUISAR DETERMINADO INDICE
for indice , valor in enumerate(lista):
	if indice ==2:
		print(valor)
	else:
		print("-")


