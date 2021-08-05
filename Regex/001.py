import re

# findall search sub
# compile

string = 'Um teste de expressoes regulares'

print(re.search(r'teste',string)) # vai buscar na string a expressao regular
print(re.findall(r'teste',string)) # vai retornar um lista com todas as vezes q apareceu a expressao
print(re.sub(r'teste','ABC',string)) # Substitui teste para ABC

regexp = re.compile(r'teste') # Compilando expressoes

print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('AAAAAA', string))

