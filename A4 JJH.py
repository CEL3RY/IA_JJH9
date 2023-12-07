import random

# Solicitamos al usuario la altura y el ancho del mapa
altura_mapa = int(input("Ingresa la altura del mapa: "))
ancho_mapa = int(input("Ingresa el ancho del mapa: "))

# Inicializamos el mapa como una lista vacía
terreno = []

# Llenamos el mapa con valores 0 o 1
for indice_altura in range(altura_mapa):
    fila_terreno = []  # Inicializamos una nueva fila para el terreno
    for indice_ancho in range(ancho_mapa):
        # Generamos un valor aleatorio y lo convertimos en entero
        valor_celda = int(random.uniform(0, 1.2))
        fila_terreno.append(valor_celda)  # Añadimos el valor a la fila
    terreno.append(fila_terreno)  # Añadimos la fila al terreno

# Imprimimos el mapa generado
print("Este es el mapa:")
for fila in terreno:
    for celda in fila:
        print("■" if celda == 1 else "·", end="  ")
    print()  # Nueva línea al final de cada fila

# Función recursiva para buscar islas
def explorarIslas(indice_altura, indice_ancho):
    # Verificamos si las coordenadas están fuera de los límites del mapa
    if indice_altura < 0 or indice_altura >= altura_mapa or indice_ancho < 0 or indice_ancho >= ancho_mapa:
        return
    # Verificamos si la celda actual no es parte de una isla
    if terreno[indice_altura][indice_ancho] != 1:
        return
    # Marcamos la celda actual como visitada
    terreno[indice_altura][indice_ancho] = 2
    # Recursividad para explorar las celdas adyacentes
    explorarIslas(indice_altura - 1, indice_ancho)
    explorarIslas(indice_altura + 1, indice_ancho)
    explorarIslas(indice_altura, indice_ancho - 1)
    explorarIslas(indice_altura, indice_ancho + 1)

# Contador de islas inicializado en 0
contador_islas = 0
for indice_altura in range(altura_mapa):
    for indice_ancho in range(ancho_mapa):
        # Si encontramos una isla, incrementamos el contador y exploramos
        if terreno[indice_altura][indice_ancho] == 1:
            contador_islas += 1
            explorarIslas(indice_altura, indice_ancho)

# Imprimimos el número de islas encontradas
print("Hay", contador_islas, "islas existentes")

# Método iterativo para contar islas (esta parte no está en uso y se puede eliminar)
# contador_islas_iterativo = 0
# for indice_altura in range(altura_mapa):
#     for indice_ancho in range(ancho_mapa):
#         if terreno[indice_altura][indice_ancho] == 1:
#             contador_islas_iterativo += 1
#             terreno[indice_altura][indice_ancho] = 2

# Imprimir el número de islas contadas iterativamente (esta línea también se puede eliminar)
# print("Hay", contador_islas_iterativo, "islas existentes")
