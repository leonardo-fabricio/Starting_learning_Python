import re

texto = '''
A Pró-Reitoria  de Ensino do Instituto FedErAl de Educação, 
Ciência e Tecnologia do Rio Grande do Norte (IFRN), por 
meio do Edital n°34/2021-PROEN/IFRN, faz saber às pessoas 
interessadas que estarão abertas - entre 6 e 10 de agosto 
- as inscrições de processo seletivo para o curso de Formação
em Educação a Distância na Formação Inicial e Continuada (FIC),
modalidade Educação a distância (EaD), 1 ofertaaado 2 ofertaaadoo 3 ofertaaaado pelo Campus Avançado 
Natal-Zona Leste, com ingresso para o segundo semestre letivo de 2021.

distannnnnnciaaaaaaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbbbbbbb ccccccccccccccc campuuuus.

distaniaaaaaaaaaaaaaaaaaaaa

'''
# O ponto vai buscar o caractere seguido de qualquer coisa, menos uma quebra de linha
# a barra | significa OU
# Os colchetes significam um conjunto de caracteres especificos, (funciona como um OU)

# regex = re.compile(r'Natal|campus| p..| [Dd]istância | [Cc]ampus | [a-zA-Z]etivo| [0-9]021') 
# print(regex.findall(texto)) 

# print(re.findall(r'distâNciA|caMpus',texto, flags=re.IGNORECASE)) 
# vai encontrar as palavras da forma q elas estiverem

#Meta Caracteres: | [] ^ $ () * + ? {n} {min,max}
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min,max}
# ()


# O + eh aplicado ao caracter a esquerda
print(re.findall(r'distan+cia',texto, flags=re.IGNORECASE)) 
print(re.findall(r'distan+cia+',texto, flags=re.IGNORECASE))

print(re.sub(r'distan+cia+','Felipe',texto, flags=re.IGNORECASE))

# O ? significa dizer que o caracter pode existir ou nao
print(re.sub(r'distan+c?ia+|...+reitoria|federal','TAVA AQUI',texto, flags=re.IGNORECASE))

# Nesse Caso especifico os {} funcionaram como o + pq nao passei o valor maximo
print(re.sub(r'distan{1,}cia{1,}','AAAAAAAAAAAAA', texto,flags=re.IGNORECASE))

print(re.sub(r'oferta{3}do{1,2}', 'OPAAAAAAAAA', texto, flags=re.IGNORECASE))

#retirando os espaços do texto 
print(re.sub(r' ','', texto, flags=re.I))