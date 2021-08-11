import re

txt = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''

# print(re.findall(r'<[pdiv]{1,3}>',txt)) # IDENTIFICA AS TAGS 
# print(re.findall(r'<[pdiv]{1,3}>.*',txt)) # O PONTO SIGINIFICA TODO CONTEUDO, OU SEJA TODO OU NENHUM ATRAVEZ DO *
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>',txt)) #O ? FAZ A EXPRESSAO SE COMPORTAR DE FORMA NAO GULOSA