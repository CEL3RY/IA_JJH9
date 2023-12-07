# Algoritmo de Etiquetado de Componentes Conectados

El problema presentado es un ejemplo clásico del algoritmo de etiquetado de componentes conectados. La matriz en cuestión, de dimensiones 14x22, representa una estructura de datos donde los elementos de la matriz pueden tomar valores de 0 o 1, correspondientes a espacios en blanco o espacios en gris, respectivamente, en una representación visual.

## Definición de una "Isla"

Una "isla" se define como un conjunto de unos ('1') que están adyacentes entre sí, ya sea horizontal o verticalmente, pero no diagonalmente. Dos '1' son parte de la misma isla si comparten un borde común en la matriz.

## Proceso de Conteo de Islas

Para contar el número de islas en la matriz, se lleva a cabo un proceso de exploración que revisa cada elemento de la matriz. Al encontrar un '1', el algoritmo comienza un proceso de búsqueda en profundidad o en amplitud para identificar todos los '1' conectados a ese elemento, marcándolos como parte de la misma isla y asegurándose de no contarlos más de una vez.

La solución al problema implica iterar a través de cada elemento de la matriz y aplicar el algoritmo de búsqueda cada vez que se encuentra un '1' no marcado, incrementando el conteo de islas. Una vez que se ha visitado y marcado todo el conjunto de '1' conectados, se ha identificado y contabilizado una isla completa. Este proceso se repite hasta que se han explorado todos los elementos de la matriz.


En el ámbito de la informática, el desafío de contar islas dentro de una matriz binaria es un problema clásico que se aborda con el algoritmo de etiquetado de componentes conectados. La matriz de 14x22 es un entorno que simula un espacio donde los '0' representan el agua y los '1' representan tierra. El objetivo es determinar cuántas islas de '1' contiguos existen dentro de esta matriz.

El método de exploración y conteo es fundamental en áreas como el análisis de datos, la visión por computadora y la inteligencia artificial. A través de este enfoque, se revela la estructura subyacente de la matriz, proporcionando una comprensión clara de la distribución y la cantidad de islas dentro de ella. El resultado de este análisis confirmó la presencia de una única isla, destacando la utilidad y eficiencia del algoritmo para resolver problemas de conteo en entornos discretos y estructurados.
