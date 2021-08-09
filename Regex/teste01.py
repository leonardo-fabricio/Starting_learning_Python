import re

txt = ''' 
A Direção-Geral do Campus São Gonçalo do Amarante do IFRN, subsidiada pela Política de Desenvolvimento Científico e Tecnológico, 
de Inovação e de Empreendedorismo, divulgou o Edital  n° 11/2021-DG/SGA/RE/IFRN. O documento traz a abertura de processo seletivo
de empresas para acesso ao Programa de Incubação da Trevo Incubadora. 

O edital, na modalidade de fluxo contínuo, tem como objetivo selecionar, empreendimentos residentes e empreendimentos não residentes, 
aptos a participarem do programa da incubadora do Campus, mediante existência de vagas.

Seleção: inscrições e prazos

O período de inscrições do edital é de 27 de julho a 31 de dezembro de 2021, podendo ser prorrogado por até 12 meses, a critério da 
equipe gestora da Trevo Incubadora. Serão realizadas através do preenchimento do formulário de inscrição on-line. Após o preenchimento 
do formulário, a empresa ou os proponentes da ideia deverão enviar e-mail para trevo@ifrn.edu.br com cópia para marcella.assuncao@ifrn.edu.br,
com Título "INCUBAÇÃO 2021 FLUXO CONTÍNUO" para formalizar sua inscrição. Caso a empresa ou proponente preencha a ficha de inscrição mas 
não envie o e-mail de formalização de inscrição, será eliminada do processo seletivo.

São disponibilizadas duas vagas para empreendimentos residentes e duas vagas para empreendimentos não residentes. Para tanto, a avaliação 
das empresas proponentes se dará em duas etapas:

Triagem das propostas inscritas - etapa eliminatória;
Apresentação do Modelo de Negócio - etapa eliminatória e classificatória. Defendida oralmente em um pitch de cinco minutos e mais 20 minutos
para discussão com a banca, via Google Meet. Além disso, entrevista com os sócios da empresa ou proponentes da ideia realizada pela Trevo Incubadora.
Entre as empresas classificadas, serão levadas em consideração pontos como inovação da ideia, abrangência de mercado e perspectiva de retorno
financeiro, serão selecionadas as duas empresas com maior pontuação para participarem do programa de incubação da Trevo Incubadora.

Uma vez que o edital é na modalidade de fluxo contínuo, as datas e prazos serão definidos através de comunicação entre o empreendimento 
e a incubadora, através do e-mail trevo@ifrn.edu.br com cópia para marcella.assuncao@ifrn.edu.br. Estes mesmos e-mails serão utilizados para 
esclarecimentos e informações, bem como possíveis interposições de recurso.

Propósitos

A incubadora de empresas tem como propósito orientar empreendedores locais para viabilização de seus projetos e negócios de inovação,
promovendo conexões e apoio técnico especializado. Poderão participar desta seleção Pessoas Jurídicas (CNPJ) classificadas como empresas 
privadas sem quaisquer débitos ou pendências trabalhistas, ou Pessoas Físicas (CPF) no processo de ideação de seus negócios. Os proponentes 
devem apresentar produtos, serviços e/ou processos inovadores que busquem a solução de problemas ou desafios sociais, ambientais ou tecnológicos, 
independente do ramo de atuação.

Destaques

As empresas e/ou empreendedores responsáveis que já tenham integrado o Programa de Incubação da Incubadora Tecnológica não poderão participar
deste processo seletivo. Enquanto perdurar decretos que determinem o fechamento das instituições de ensino no âmbito federal, estadual ou 
municipal, a Trevo Incubadora não terá funcionamento presencial.

'''

#Meta Caracteres: | [] ^ $ () * + ? {n} {min,max}
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min,max}
# ()

# print(re.findall('incu{0,}badora', txt, flags=re.IGNORECASE))
# print(re.findall('incu{3}badora', txt, flags=re.IGNORECASE))
# print(re.findall('incu{0,3}badora', txt, flags=re.IGNORECASE))
print(re.findall(r'incubadoras? | pessoa[sl]', txt, flags=re.IGNORECASE))