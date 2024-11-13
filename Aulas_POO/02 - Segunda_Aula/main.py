from biblioteca import *

animal=Animal("Guepardo", "Laranja")
print(animal.nome)
animal.Comer()

gato=Gato("Aghata", "Frajola")
print(gato.nome)
gato.Miar()
gato.Comer()

vaca=Vaca("Mimosa", "Frajola")
print(vaca.nome)
vaca.DarLeite()

coelho=Coelho("Charlote","Branco")
print(coelho.nome)
coelho.Pular()

cachorro=Cachorro("Leleco","Preto")
print(cachorro.nome)
cachorro.Latir()

from biblioteca_2 import *

atleta=Atleta("Wiliane", 68)
atleta.Aquecer()
atleta=Corredor("Wiliane", 68)
atleta.Correr()