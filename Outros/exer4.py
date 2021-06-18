ewq def terceiraPotencia (a):
    return(a*a*a)

lista=[2,3,4]
print(list(map(terceiraPotencia,lista)))

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print(list(enumerate(lista)))

for ind, value in enumerate(lista):
    if(ind >= 5):
        print(ind," = ",value)
    else:
        print("-")

# PEGANDO CHAVVE SE UMA HASHMAP E UNINDO COM UMA VALOR DE OUTRO
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

print(dict1.keys())
dicio = dict(zip(dict1.keys(),dict2.values()))
print(dicio)

# HORA LOCAL
import datetime
import time

print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
print(time.asctime(time.localtime()))


