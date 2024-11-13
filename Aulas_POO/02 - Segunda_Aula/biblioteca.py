class Animal:
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor
    def Comer(self):
        print(f"{self.nome} foi comer")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def Miar(self):
        print(f"{self.nome} esta miando")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def Pular(self):
        print(f"{self.nome} esta pulando")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def Latir(self):
        print(f"{self.nome} esta latindo")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def DarLeite(self):
        print(f"{self.nome} esta produzindo leite nas tetas")