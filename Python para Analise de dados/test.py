import numpy as np
from numpy.core.records import array
from pandas import Series
from pandas import DataFrame
import json

# # print(np.__version__) VERSAO DO NUMPY

# # help(np.array)

# #Criar Vetores
# vetor = np.array([0,1,2,3,4,5])
# print(vetor)
# print(vetor.cumsum())
# print(vetor.shape)

# print(vetor.dtype)
# print(np.zeros(10))

# #Criar Matrizes

# matriz = np.array([[0,1,2,3],[4,5,6,7]])
# print(matriz)

# lista = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
# matriz2 = np.array(lista)
# print(matriz2)
# print(np.shape(matriz2))
# matriz.size
# matriz.nbytes

# #=========
# import matplotlib.pyplot as plt
# print(np.random.rand(10))

# plt.show((plt.hist(np.random.rand(1000))))

# a = np.diag(np.arange(3))
# b= np.diag(np.arange(2))
# print(b)
# print("")
# print(a)
# arr = np.arange(10)
# b[2:9:3] #COMEÇA NA POSIÇAO 2, VAI ATE A 9 E SALTA DE 3 EM 3

#=============== PANDAS
# 2 in Obj

Obj = Series([67,80,13,-20])
# print(Obj.values)
# print(Obj.index)

dic = {"Ano":[2002,2003,2004,2005], "Estado":["Santa Catarina","Sao Paulo","Bahia","Minas Gerais"],"População":[1.5,1.7,3.6,2.4]}
frame = DataFrame(dic)
# print(frame)


# json.dumps(dic)

with open("arquivo.json", "w") as arquivo:
	arquivo.write(json.dumps(dic))

arquivo.close()

with open("arquivo.json","r") as arquivo:
	txt = json.loads(arquivo.read()) #loads carrega os dados num formato de dict
	frame2 = DataFrame(txt)
	print(frame2)
    



# print(frame2)
    


