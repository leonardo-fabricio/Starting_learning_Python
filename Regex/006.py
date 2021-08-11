import re
#^ -> COMEÇA COM
#$ -> TERMINA COM
#[^A-Z] -> NEGAÇAO

# cpf = 'meu cpf eh 703.104.724-23'
# print (re.findall('^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}',cpf))

cpf = 'aaaaaaaaa 703.104.724-23 eh meu cpf'
print (re.findall('^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$',cpf))