# from math import sqrt
# import random

# print(sqrt(9))	

# print(random.choice(["banana","Goiaba","Melão"])) #escolhe de maneira aleatoria

# print(random.sample(range(100),10)) #vai gerar 10 numeros aleatorios entre 100 e 0

# import sys
# sys.stdout.write('teste')
# print(sys.version)

#PEGA TODO CONTEUDO DE UMA PAGINA WEB E ARMAZENA NUMA VAR
import urllib.request
resp = urllib.request.urlopen('http://google.com')
#print(resp)
html_pagina = resp.read()

#-------------------------------#
# dados = list(html_pagina)#    #
# print(dados)                  #
#-------------------------------#
