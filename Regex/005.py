import re
from pprint import pprint

txt = '''
<p>Frase 5</p> <p>Frase 3</p> <p>Frase 4</p> <div>Frase 1</div>
<p>Frase 2</p>
'''

# print(re.findall(r'<([divp]{1,3})>.*?<\/\1>', txt)) # RETONA APANAS OD GRUPOS "()" QUE SAO ACESSADOS NO \1  
# tags  = (re.findall(r'(<([divp]{1,3})>.*?<\/\2>)', txt)) # RETORNA OS GRUPOS (()) 

# for tag in tags:
#     print(tag)
       
# for tag in tags:
#     grp1, grp2 = tag # como o tag tem nos valores posso inseri-los em variaveis diferentes
#     pprint(grp1)

# tags  = (re.findall(r'(<([divp]{1,3})>(.*?)<\/\2>)', txt)) #CRIANDO UM TERCEIRO GRUPO APENAS PROS VALORES, AGORA EU POSSO PEGAR APENAS ELES
# for tag in tags:
#     grp1, grp2, grp3 = tag # IMPRIMINDO APENAS OS VALORES
#     pprint(grp3)

# tags  = (re.findall(r'<([divp]{1,3})>(?:.*?)<\/\1>', txt)) # COM ?: ELE NAO SALVA MAIS OS RESULTADOS DAQUELE GRUPO
# pprint(tags)


# cpf = '703.104.724-23'
# print (re.findall('[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}',cpf))
# print (re.findall('((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})',cpf)) # MESMO EXEMPLO SO QUE UTILIZANDO GRUPOS

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', txt))