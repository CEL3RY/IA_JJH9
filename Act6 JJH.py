def josephus(n):
    p = 1
    while p <= n:
        p *= 2
    return 2 * n - p + 1

# Caso para 41 soldados
n = 41
safe_position = josephus(n)
print(f"Josephus debería sentarse en la posición: {safe_position}")
