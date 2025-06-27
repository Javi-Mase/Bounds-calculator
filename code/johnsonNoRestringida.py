import math

def cotaJohnsonNoRestringida2(n, d, w, q) -> int:
    qEstrella = q - 1
    e = math.ceil(d / 2)

    # En el caso de d para elegimos condiciones de parada
    if d % 2 == 1:
        iParada = w - e + 1
        parada = 1
        
    # En el caso de d impar elegimos condiciones de parada
    else:
        iParada = w - e
        # la parte final que viene de A_q(n-i, d, w-i) ≤ floor((n-w+e)q*/e)
        parada = math.floor((n - w + e) * qEstrella / e)

    # si i_stop ≤ 0, no multiplicamos ningún término intermedio
    value = parada
    # desanidamos: j = iParada, iParada-1, ..., 1
    for j in range(iParada, 0, -1):
        numer = (n - j + 1) * qEstrella
        denom = (w - j + 1)
        # anidamos el piso sobre el valor anterior
        value = math.floor( (numer / denom) * value )

    return value


# Variante binaria (q = 2)
def cotaJohnsonNoRestrictivaBinario(n, w, e) -> int:

    # Número de pisos anidados: j = 0,1,...,w-e
    max_j = w - e

    # Valor inicial: floor((n - max_j) / (w - max_j))
    value = math.floor((n - max_j) / e)

    # Anidar los restantes pisos, de j = max_j-1 down to 0
    for j in range(max_j - 1, -1, -1):
        factor = (n - j) / (w - j)
        value = math.floor(factor * value)

    return value


def cotaJohnsonNoRestringida(n, d, w, q) -> int:
    e = math.ceil(d / 2) 

    if 2 * w < d:
        return 1
    
    if 2*w >= d and d in (2*e - 1, 2*e):
        return cotaJohnsonNoRestringida2(n, d, w, q)
        

    # --- casos binarios vs no binarios -------------------------------
    if q == 2:
        if w < e:
            return 1          
        return cotaJohnsonNoRestrictivaBinario(n, w, e)
    
    else:
        raise ValueError(f"Johnson no restringida: \n No se cumple ninga de las condiciones para aplicar esta cota")
        


def cotaJohnsonNoRestringidaInversa(n: int, M: int, w: int, q: int) -> int:
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if cotaJohnsonNoRestringida2(n, mid, w, q) >= M:
            lo = mid
        else:
            hi = mid - 1
    return lo


def cotaJohnsonNoRestringidaCheck(n, d, w, q, M) -> tuple[bool, int]:
    M_max = cotaJohnsonNoRestringida2(n, d, w, q)
    return M <= M_max, M_max
