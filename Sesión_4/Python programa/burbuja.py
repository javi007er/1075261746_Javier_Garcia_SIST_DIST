# Definimos la función 

import random


def bubbleSort(array):
    length = len(array) -1
    # Bucle para las pasadas
    for i in range(0, length):
        # Bucle para las comparaciones
        for j in range(0, length):
            if array[j] > array[j + 1]:
                aux = array [j]
                array[j] = array[j + 1]
                array[j + 1] =  aux

    return array

# Cramos nustras lista
scores = random.sample(range(10),10)
print("Antes de ordenar")
print(scores)
print("Después de Ordenar")
print(bubbleSort(scores) )