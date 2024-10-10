class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.Dormindo = False
        self.Dormindo = False
        self.Comendo = False

    def Falar(self):
        if self.Dormindo == False and self.Comendo == False and self.Falando == True:
            self.Falando = True
            print(f"{self.nome} foi falar")
        else:
            print(f"{self.nome} não esta falando")

    def Comer(self):
        if self.Falando == False and self.Dormindo == False and self.Comendo == True:
            self.Comer = True
            print(f"{self.nome} foi comer")
        else:
            print(f"{self.nome} não esta comendo")

    def Dormir(self):
        if self.Falando == False and self.Comendo == False and self.Dormindo == True:
            self.Dormir = True
            print(f"{self.nome} esta dormindo ")
        else:
            print(f"{self.Dormir} nao esta dormindo")

    def PararComer(self):
        self.Comer = False
    def PararFalar(self):
        self.Falar = False
    def PararDormir(self):
        self.Dormir = False
