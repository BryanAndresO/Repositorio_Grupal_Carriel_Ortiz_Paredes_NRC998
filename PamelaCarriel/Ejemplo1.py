#UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE
#INTEGRANTES: CAMILA PAREDES, BRYAN ORTIZ, PAMELA CARRIEL
#NRC: 9898
#FECHA: 17/05/2023
#EJEMPLO DE PILAS
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print(pila.desapilar())
