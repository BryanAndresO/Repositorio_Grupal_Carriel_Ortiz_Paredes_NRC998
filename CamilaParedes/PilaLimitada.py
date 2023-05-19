#UNIVERSIDAD DE LAS FUERZAS ARMADAS "ESPE"
#INTEGRANTES: CARRIEL PAMELA, ORTIZ BRYAN, PAREDES CAMILA
#NRC: 9898
#IMPLEMNETAR UNA PILA CON CAPACIDAD LIMITADA
class Pila:
    def _init_(self, capacidad):
        self.capacidad = capacidad
        self.pila = []

    def esta_vacia(self):
        return len(self.pila) == 0

    def esta_llena(self):
        return len(self.pila) == self.capacidad

    def apilar(self, elemento):
        if self.esta_llena():
            print("La pila está llena. No se puede apilar el elemento.")
        else:
            self.pila.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            print("La pila está vacía. No se puede desapilar ningún elemento.")
        else:
            return self.pila.pop()

    def obtener_tamaño(self):
        return len(self.pila)
      # Crear una instancia de la pila con capacidad máxima de 5 elementos
pila = Pila(5)

# Apilar elementos
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)

# Intentar apilar un sexto elemento cuando la pila está llena
pila.apilar(6)

# Desapilar elementos
elemento = pila.desapilar()
print("Elemento desapilado:", elemento)  # Output: Elemento desapilado: 5

# Obtener el tamaño de la pila
print("Tamaño de la pila:", pila.obtener_tamaño())  # Output: Tamaño de la pila: 4