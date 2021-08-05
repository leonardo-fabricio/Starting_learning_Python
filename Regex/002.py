import re

texto = '''
A Pró-Reitoria de Ensino do Instituto Federal de Educação, 
Ciência e Tecnologia do Rio Grande do Norte (IFRN), por 
meio do Edital n°34/2021-PROEN/IFRN, faz saber às pessoas 
interessadas que estarão abertas - entre 6 e 10 de agosto 
- as inscrições de processo seletivo para o curso de Formação
em Educação a Distância na Formação Inicial e Continuada (FIC),
modalidade Educação a distância (EaD), ofertado pelo Campus Avançado 
Natal-Zona Leste, com ingresso para o segundo semestre letivo de 2021.

aaaaaaaaaaaaaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbbbbbbb ccccccccccccccc campus.

'''
# O ponto vai buscar o caractere seguido de qualquer coisa, menos uma quebra de linha
# a barra | significa OU
# Os colchetes significam um conjunto de caracteres especificos, (funciona como um OU)
regex = re.compile(r'Natal|campus| p..| [Dd]istância | [Cc]ampus | [a-zA-Z]etivo| [0-9]021') 
print(regex.findall(texto)) 

print(re.findall(r'distâNciA|caMpus',texto, flags=re.IGNORECASE)) 
# vai encontrar as palavras da forma q elas estiverem