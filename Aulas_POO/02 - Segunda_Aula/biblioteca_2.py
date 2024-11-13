class Atleta:
    def __init__(self, nome, peso):
        self.peso=peso
        self.nome=nome
        self.aquecido=False
        self.aposentado=False

    def Aposetar(self):
        if self.aposentado == False:
            self.aposetado = True
            print(f"{self.nome} Esta aposentado")
        else:
            print(f"{self.nome} ja esta aposentado")

    def Aquecer(self):
        if self.aquecido == False:
            self.aquecido = True
            print(f"{self.nome} esta aquecido")
        if self.aposentado == True:
            print(f"{self.nome} Esta aposentado")

    def NaoAposentado(self):
        self.aposentado = False
        print(f"{self.nome} nao esta aposentado")

class Corredor(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def Correr(self):
        if self.aquecido == True:
            print(f"{self.nome} Esta correndo")
class Nadador(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def Nadar(self):
        if self.aquecido == True:
            print(f"{self.nome} Esta nadando")
class Ciclista(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def Pedalar(self):
        if self.aquecido == True:
            print(f"{self.nome} Foi pedalar")
class Triatleta(Ciclista, Nadador, Corredor):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)