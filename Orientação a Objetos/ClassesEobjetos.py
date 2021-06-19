from typing import Callable


class PrimeiraClass():
    def imprime(self):
        print(self.titulo," ",self.isbn)
    
    def __init__(self,titulo,isbn):
        self.titulo = titulo
        self.isbn = isbn
    

obj = PrimeiraClass("Guardioes da galaxia", 999090090)
# obj.imprime()

#===================#
#hasattr            #
#getattr            #
#setattr            #
#delattr            #
#__str__            #
# __len__           #
#===================#


class Circulo():
    pi = 3.14
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return (self.raio*self.raio)*Circulo.pi

    def getraio(self):
        return self.raio

    def setraio(self, Nraio):
        self.raio = Nraio


c = Circulo(2)

# print(c.getraio())
# print(c.area())
# c.setraio(5)
# print(c.getraio())
# print(c.area())

#HERANÇA

class Animal():
    def __init__(self,tipo):
        self.tipo = tipo
        print("animal criado")

    def iden(self):
        print(self.tipo)

    def comer(self):
        print("ANIMAL COMENDO")

class Cachorro(Animal):
    def __init__(self, tipo):
        super().__init__(tipo)
        print("Cachorro Criado")

    def latir(self):
        print("auauauau")


a = Animal("Baleia")
# print("-----")
c = Cachorro("Cachorro")
# print("-----")

# a.iden()
# a.comer()

# print("-----")

# c.latir()
# c.iden()


# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.
class Smartphone():
    def __init__(self,tam,interface):
        self.tam = tam
        self.interface = interface
    def __str__(self):
        return "Tamanho: %s, Interface: %s" % (self.tam, self.interface)
        
class MP3player(Smartphone):
    def __init__(self,capacidade,tam, interface):
        Smartphone.__init__(self,tam,interface)
        self.capacidade = capacidade

m = MP3player("2gb","20cm","IOS")
s = Smartphone("15cm","Andoid")

str(m)
str(s)
print(m)
print(s)


# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():
    def __init__(self,nome,cidade,telefone,email,altura):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        self.altura = altura
    def __str__(self):
        return "Dados do usuario: %s, %s, %s, %s, %s" %(self.nome, self.cidade,self.telefone,self.email,self.altura)
#     def __len__(self):
#         return self.altura A FUNÇAO LEN SO RETORNA VALORES INTEIROS...
    
leo = Pessoa(nome = "Leonardo",telefone="99889897",email="l@gmail.com",cidade="Alexandria",altura = 1.67)
print(leo)


# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        
roc1 = Rocket(2,5)
roc1.print_rocket()
roc1.move_rocket(1,2)
roc1.print_rocket()
