def resolver_laberinto(laberinto, x, y, solucion):
    # Si x, y es la salida, retorna True
    if (x, y) == (META_X, META_Y):
        solucion[x][y] = 1
        return True

    # Verifica si laberinto[x][y] es válido
    if laberinto[x][y] == 1:
        # Marca la celda como parte de la solución
        solucion[x][y] = 1
        
        # Mueve hacia adelante en la dirección x
        if resolver_laberinto(laberinto, x + 1, y, solucion):
            return True
        
        # Si mover hacia x no da solución, mueve hacia y
        if resolver_laberinto(laberinto, x, y + 1, solucion):
            return True
        
        # Si ninguna de las direcciones funciona, retrocede (backtrack)
        solucion[x][y] = 0
        return False

    return False
