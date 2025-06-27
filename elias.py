

import math
from hamming import volumenBolaHamming

# Cota de Elias–Bassalygo para A_q(n, d):
# 1) calcular w = floor( r*n - sqrt(r*n*d) ), con r = (q-1)/q
# 2) M <= (r * n * d) / (w^2 - 2 r n w + r n d)  *  q^n / V_q(n, w)
# Se devuelve floor de todo el producto.
def cotaElias(n: int, d: int, q: int) -> int:
    r = (q - 1) / q
    # radio óptimo de la capa constante
    w = math.floor(r * n - math.sqrt(r * n * d))
    # volumen de la bola de radio w
    V = volumenBolaHamming(n, w, q)
    # parte fraccional de Johnson
    denom = w * w - 2 * r * n * w + r * n * d
    if denom <= 0 or V == 0:
        return 10**18
    M1 = (r * n * d) / denom
    M2 = (q ** n) / V
    return math.floor(M1 * M2)


def cotaEliasInversa(n: int, M: int, q: int) -> int:
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if cotaElias(n, mid, q) >= M:
            # con d = mid todavía caben M palabras
            lo = mid
        else:
            # mid es demasiado grande, reducir
            hi = mid - 1
    return lo

# Comprueba si un código (n, M, d)_q cumple la cota de Elias–Bassalygo.
# Devuelve (cumple: bool, M_max: int).
def cotaEliasCheck(n: int, d: int, q: int, M: int):
    M_max = cotaElias(n, d, q)
    return (M <= M_max, M_max)
