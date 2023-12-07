## Definición de Heurística

La *heurística* es un enfoque práctico para resolver problemas que busca una solución **suficientemente buena y eficiente** cuando las respuestas perfectas son impracticables de obtener. En problemas de búsqueda y optimización, una heurística puede ser una función que **estima la cercanía al objetivo**, como la distancia de Manhattan en laberintos.

## Resolver con Recursividad

Resolver un laberinto con recursividad implica explorar cada camino posible hasta encontrar la salida. Si un camino conduce a un callejón sin salida, el algoritmo **retrocede** y prueba una dirección diferente.

Aquí está el pseudocódigo básico:

```plaintext
función resolverLaberinto(posición):
    si posición es la salida:
        devolver éxito
    si posición es una pared o ya fue visitada:
        devolver fracaso
    marcar posición como visitada
    para cada dirección (arriba, abajo, izquierda, derecha):
        si resolverLaberinto(posición + dirección) es éxito:
            devolver éxito
    desmarcar posición como visitada
    devolver fracaso

## Descripción del Algoritmo

El algoritmo usa *backtracking* para encontrar la salida del laberinto. Comienza en un punto inicial y explora todas las direcciones posibles. Si encuentra un obstáculo o un camino sin éxito, **retrocede** para probar una ruta alternativa. El proceso continúa hasta que se encuentra la salida o se determina que no hay camino. Este algoritmo es efectivo para laberintos que tienen un único camino a seguir, como los laberintos clásicos o univiarios que mencionas. En un laberinto más complejo con múltiples rutas y posibles puntos muertos, el backtracking sigue siendo una técnica válida, aunque puede no ser la más eficiente en términos de tiempo de ejecución.
