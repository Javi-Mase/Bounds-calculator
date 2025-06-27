import math
from hamming import volumenBolaHamming


# Obtiene la cota de Gilbert-Varshamov inferior para A_q(n, d)
# A_q(n, d) >= q^n / V_q(n, d-1)
def cotaGilbert(n, d, q):
    volumen = volumenBolaHamming(n, d - 1, q)
    return q ** n // volumen

# Cálculo inverso, dado n, q y M, busca la menor distancia d tal que todavía cabe M palabras
# con la cota de Gilbert-Varshamov (útil para estimar rendimiento mínimo)
def cotaGilbertInversa(n, M, q):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if cotaGilbert(n, mid, q) >= M:
            hi = mid
        else:
            lo = mid + 1
    return lo

# Verifica si un código dado (n, d, q, M) cumple con la cota inferior de Gilbert–Varshamov
# Devuelve una tupla (cumple, M_min), donde:
#   cumple: True si M >= M_min según la cota
#   M_min: el valor mínimo garantizado por la cota
def cotaGilbertCheck(n, d, q, M):
    minimaM = cotaGilbert(n, d, q)
    cumple = M >= minimaM
    return cumple, minimaM
