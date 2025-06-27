


# Calcula la cota de Singleton para el número máximo de palabras M en un código de longitud n, distancia mínima d, sobre un alfabeto de tamaño q.
# Fórmula: M <= q^{n - d + 1}
def cotaSingleton(n, d, q):
    return q ** (n - d + 1)

# Cálculo inverso: dado n, q y M, busca la mayor distancia mínima d tal que la cota de Singleton todavía permite al menos M palabras.
def cotaSingletonInversa(n, M, q):
    # Búsqueda binaria sobre el rango d = 0..n
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if cotaSingleton(n, mid, q) >= M:
            # Con d=mid la cota sigue admitiendo M palabras
            lo = mid
        else:
            # Con d=mid la cota ya no admite M → acotar por debajo
            hi = mid - 1

    return lo


#  Verifica si un código dado (n, d, q, M) cumple con la cota de Singleton.
def cotaSingletonCheck(n, d, q, M):
    M_max = cotaSingleton(n, d, q)
    cumple = M <= M_max
    return cumple, M_max
