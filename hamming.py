import math


# Calcula el volumen de una bola de Hamming de radio t en F_q^n
# V_q(n, t) = sum_{i=0}^{t} binom(n, i) * (q - 1)^i
def volumenBolaHamming(n, t, q):
    volumen = 0
    for i in range(t + 1):
        coef_binomial = math.comb(n, i)  # Coeficiente binomial binom(n, i)
        volumen += coef_binomial * (q - 1) ** i
    return volumen


# Obtiene la cota de Hamming para A_q(n, d)
# A_q(n, d) ≤ q^n / V_q(n, t) donde t = floor((d - 1) / 2)
def cotaHamming(n, d, q):
    # Division entera para obtener el radio de empaquetamiento
    t = math.floor((d - 1) / 2)
    # Volumen de la bola de Hamming
    volumen = volumenBolaHamming(n, t, q)
    # División entera para obtener el valor máximo de M
    return q ** n // volumen

# Cálculo inverso, dado n, q y M, busca la mayor distancia mínima d tal que la cota de Hamming todavía permite M palabras.
def cotaHammingInversa(n, M, q):
    # Realizamos una busqueda binaria
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if cotaHamming(n, mid, q) >= M:
            # aún cabe M palabras con d = mid
            lo = mid
        else:
            # mid es demasiado grande, bajar el límite
            hi = mid - 1
    return lo

# Verifica si un código dado (n, d, q, M) cumple con la cota de Hamming.
#Devuelve una tupla (cumple, M_max) donde:
#   cumple: True si M <= M_max según la cota
#   M_max: el valor máximo permitido por la cota de Hamming
def cotaHammingCheck(n, d, q, M):
    # Cota superior teórica
    maximaM = cotaHamming(n, d, q)
    cumple = M <= maximaM
    return cumple, maximaM
