class PrimeiraClass():
    def imprime(self):
        print(self.titulo," ",self.isbn)
    
    def __init__(self):
        self.titulo = "O monge executivo"
        self.isbn = 998888
    

e = PrimeiraClass()
e.imprime()