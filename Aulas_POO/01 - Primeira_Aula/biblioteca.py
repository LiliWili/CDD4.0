class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.Dormindo = False
        self.Falando = False
        self.Comendo = False

    def Falar(self):
        if self.Dormindo == False:
            if self.Comendo == False:
                if self.Falando == False:
                   print(f"{self.nome} foi falar")
                   self.Falando= True
                else:
                    print(f"{self.nome} não pode falar pois ja esta falando")
            else:
                print(f"{self.nome} não pode falar pois esta comendo")
        else:
            print(f"{self.nome} não pode falar pois esta dormindo")

    def Comer(self):
        if self.Falando == False:
            if self.Dormindo == False:
                if self.Comendo == False:
                     self.Comendo = True
                     print(f"{self.nome} foi comer")
                else:
                    print(f"{self.nome} ja esta comendo")
            else:
                print(f"{self.nome} Nao pode comer pois esta dormindo")
        else:
            print(f"{self.nome} nao poder comer pois esta falando")

    def Dormir(self):
        if self.Falando == False:
            if self.Comendo == False:
                if self.Dormindo == False:
                    self.Dormindo = True
                    print(f"{self.nome} esta dormindo ")
                else:
                    print(f"{self.nome} ja esta dormindo")
            else:
                print(f"{self.nome} nao pode dormir pois esta comendo")
        else:
            print(f"{self.nome} nao pode dormir pois esta falando")

    def PararComer(self):
        self.Comendo = False
        print(f"{self.nome} Parou de comer")
    def PararFalar(self):
        self.Falando = False
        print(f"{self.nome} Parou de falar")
    def PararDormir(self):
        self.Dormindo = False
        print(f"{self.nome} parou de dormir")