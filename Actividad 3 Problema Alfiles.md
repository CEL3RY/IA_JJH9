# Introducción
AJEDRES
# Descripción del Problema
Dado un tablero de ajedrez 4x4 con alfiles blancos en la fila inferior y negros en la superior, debemos intercambiar sus posiciones alternando movimientos entre blancos y negros, asegurando que no se amenacen entre sí.

# Estrategia de Solución
Enumeramos los alfiles blancos de 1 a 4 y los negros de 5 a 8. La secuencia de movimientos es planificada para evitar ataques y minimizar el total de movimientos necesarios.

# Secuencia de Movimientos

- Mover el alfil blanco 1 a la casilla 2B.
- Mover el alfil negro 5 a la casilla 3C.
- Mover el alfil blanco 2 a la casilla 1A.
- Mover el alfil negro 6 a la casilla 4D.
- Mover el alfil blanco 3 a la casilla 2A.
- Mover el alfil negro 7 a la casilla 3D.
- Mover el alfil blanco 4 a la casilla 1B.
- Mover el alfil negro 8 a la casilla 4C.

Los alfiles ahora están en posiciones seguras. Procedemos a intercambiarlos a las posiciones finales.

- Mover el alfil blanco 1 a la casilla 3C (posición original del alfil negro 5).
- Mover el alfil negro 5 a la casilla 2B.
- Mover el alfil blanco 2 a la casilla 4D (posición original del alfil negro 6).
- Mover el alfil negro 6 a la casilla 1A.
- Mover el alfil blanco 3 a la casilla 3D (posición original del alfil negro 7).
- Mover el alfil negro 7 a la casilla 2A.
- Mover el alfil blanco 4 a la casilla 4C (posición original del alfil negro 8).
- Mover el alfil negro 8 a la casilla 1B.



