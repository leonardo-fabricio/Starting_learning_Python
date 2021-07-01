import urllib.request
from bs4 import BeautifulSoup
import re

with urllib.request.urlopen("https://portal.ifrn.edu.br/") as url:
    page = url.read()

soup = BeautifulSoup(page, "html.parser")
# print(soup.span)
# print(soup.span.string)

# for x in soup.find_all("span"):
#      with open("span.txt","a") as arquivo:
#         arquivo.write(str(x)+"\n")
#         arquivo.close()

# for x in soup.find_all("a"):
#     with open("links.txt","a") as arquivo:
#         arquivo.write(str(x)+"\n")
#         arquivo.close()

# lista = ['ifrn','pau dos ferros','campus', 'popular']

# texto = 'Iniciando as atividades do ano letivo 2021, o projeto Leiturize-se propôs, para os meses de junho e julho, a leitura conjunta do romance Harry Potter e a Pedra Filosofal (1997), obra escrita pela britânica J. K. '\
#     'Rowling que inicia a saga do bruxo mais popular da ficção. Junto com o cronograma de leitura, dividido em blocos, foram feitas postagens na página do Instagram do clube que apresentam particularidades sobre autora e obra, bem como do universo mágico representado na narrativa.' 

# for x in lista:
#     print('\nBuscando a palavra %s em: \n\n %s' % (x,texto))
#     if re.search(x,texto):
#         print('\nPalavra encontrada\n')

#     else:
#         print('\nPalavra não encontrada\n')

# quebra = ';'

# txt = 'dadadasdasdasd;sdasdasdasdaefrgssf;sefsrfrfsd;fsef;sfefsgsrgr;d'

# print(re.split(quebra,txt))

def encontra(lista,texto):
    for x in lista:
        print('Buscando padrao %s' % (x))
        print(re.findall(x,texto))
        print('\n')

frase = 'zLzL...zzzLLL...zLLLLzLLL...LzLz...dzzzzzz...zLLLLL'
    
lista = ['zL*', #z seguido de zero ou mais L
        'zL+', #z seguido por um ou mais L
        'zL?',  #z seguido por zero ou um L
        'zL{3}', #z seguido por três L
        'zL{2,3}' #z seguido dois a três L
    ]

#encontra(lista,frase)

# A expressao [^!.? ] verifica por valores q não seja pontuação
# O sinal de + verifica se o item aparece mais de uma vez
txt = 'kasksaskkaskaskkdaksdksakdaksdasdasdas. adkaslkdlaksdlaskdkasdkskdkasdsasjdjs! asdsjsdsdsdas?'
# print(re.findall('[^!.? ]+',txt)) #retorna tudo que não eh pontução

