/*#UNIVERSIDAD DE LAS FUERZAS ARMADAS "ESPE"
#INTEGRANTES: CARRIEL PAMELA, ORTIZ BRYAN, PAREDES CAMILA
#NRC: 9898
#IMPLEMNETAR UNA PILA CON CAPACIDAD LIMITADA*/
void revertirPila(stack<int> &pila) {
    stack<int> auxiliar; // Crea una pila auxiliar vacía.
    while (!pila.empty()) { // Mientras la pila original no esté vacía:
        int temp = pila.top(); // Almacena el elemento superior de la pila original en una variable temporal.
        pila.pop(); // Desapila el elemento superior de la pila original.
        auxiliar.push(temp); // Apila el elemento almacenado en la variable temporal en la pila auxiliar.
    }
    while (!auxiliar.empty()) { // Mientras la pila auxiliar no esté vacía:
        int temp = auxiliar.top(); // Almacena el elemento superior de la pila auxiliar en una variable temporal.
        auxiliar.pop(); // Desapila el elemento superior de la pila auxiliar.
        pila.push(temp); // Apila el elemento almacenado en la variable temporal en la pila original.
    }
}
