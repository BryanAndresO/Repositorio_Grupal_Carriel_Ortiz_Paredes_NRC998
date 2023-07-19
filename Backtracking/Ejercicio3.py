"""Universidad de las Fuerzas Armadas ESPE
Integrantes: Carriel Pamela, Ortiz Bryan
NRC:9898
Tema:Sudoku Solver
Fecha: miércoles 19 de julio del 2023
"""
import time
from random import choice

def existe_num_fila(matriz, fila, numero):
  #Chequear si un número se encuentra en la fila especificada.
  return numero in matriz[fila]

def existe_num_col(matriz, col, numero):
  #Chequear si un número se encuentra en la columna especificada.
  return numero in (fila[col] for fila in matriz)

def existe_num_caja(matriz, fila, col, numero):
  #Chequear si un número se encuentra en la caja a la que corresponde la posición especificada.
  #Obtener la caja a la que pertenece el número.
  caja_fila, caja_col = posicion_por_caja(fila, col)
  # Construir una lista con los números en la caja.
  numeros_en_caja = desempaquetar(fila[caja_col * 3:caja_col * 3 + 3]
                          for fila in matriz[caja_fila * 3:caja_fila * 3 + 3])
  return numero in numeros_en_caja

def reduce_posicion(n):
  #Reducir la posición 9x9 a 3x3.
  n /= 3
  if n == 0 or n != int(n):
    n += 1
  return int(n)

def posicion_por_caja(fila, col):
  # Trabajar temporalmente con base 1.
  fila += 1
  col += 1
  # Obtener base 0 nuevamente.
  return reduce_posicion(fila) - 1, reduce_posicion(col) - 1

def desempaquetar(iterable):
  """
    >>> list(desempaquetar([[1, 2], [3, 4]]))
    [1, 2, 3, 4]
    """
  for item in iterable:
    yield from item


def obtener_posibles_numeros(matriz, fila, col):
  """
    Retorna números posibles para una determinada posición.
    """
  for numero in range(1, 10):
    if (not existe_num_fila(matriz, fila, numero)
        and not existe_num_col(matriz, col, numero)
        and not existe_num_caja(matriz, fila, col, numero)):
      yield numero

def main():
  while True:
    # Los ceros representan casilleros vacíos.

    matriz = [
      [0, 7, 0, 0, 0, 0, 0, 8, 0],
      [0, 5, 8, 6, 0, 0, 0, 0, 1],
      [0, 0, 3, 1, 4, 0, 0, 0, 0],
      [9, 0, 6, 0, 5, 0, 3, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 5, 0, 2, 0, 1, 0, 7],
      [0, 0, 0, 0, 6, 5, 7, 0, 0],
      [3, 0, 0, 0, 0, 1, 9, 2, 0],
      [0, 4, 0, 0, 0, 0, 0, 1, 0],
    ]

    salida = \
    """\
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        """
     #Crea una matriz vacia con valores none, para luego llenar los posibles valores  
    while True:
      posible_numero = {
        (fila, col): None
        for fila in range(9)
        for col in range(9)
      }

      # Obtener una lista de números posibles para cada una de
      # las posiciones vacías.
      for fila in range(9):
        for col in range(9):
          numero = matriz[fila][col]
          if numero == 0:
            options = list(obtener_posibles_numeros(matriz, fila, col))
            if options:
              posible_numero[(fila, col)] = options

      # Remover valores vacíos y ordenar por la cantidad de
      # posibilidades.
      posible_numero = sorted(
        ((k, v) for (k, v) in posible_numero.items() if v is not None),
        key=lambda kv: len(kv[1]))

      if posible_numero:
        # Obtener el primer item.
        (fila, col), numeros = posible_numero[0]
        """ Obtener un número aleatorio de la lista de posibilidades 
        hasta que la grilla esté completa."""
        matriz[fila][col] = choice(numeros)
      else:
        break

    """Chequear si la busqueda dió resultado: si no hay más
    # ceros en la grilla entonces el Sudoku está resuelto."""
    if 0 not in desempaquetar(matriz):
      print(salida.format(*(desempaquetar(matriz))))
      break


if __name__ == "__main__":
  start_time = time.time()
  main()
  end_time = time.time()
  execution_time = end_time - start_time
  print("Tiempo de ejecución: {:.5f} segundos".format(execution_time))