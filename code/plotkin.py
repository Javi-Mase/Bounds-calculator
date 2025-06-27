import math



# Calcula la cota de Plotkin para el número máximo de palabras M (A_q(n, d)).
# Solo se aplica si d > (1 - 1/q)n
# Fórmula:  M ≤ floor(d / (d - r·n))    con r = 1 - 1/q
def cotaPlotkin(n, d, q):
    r = 1 - 1/q
    if d <= r * n:
        raise ValueError(f"Plotkin: \n Se tiene que cumplir d > rn. En este caso {d} <= {r}*{n}")
        return None
    return math.floor(d / (d - r * n))

# Estima la distancia mínima d tal que se cumple la cota de Plotkin para un código de longitud n, alfabeto q y M palabras.
def cotaPlotkinInversa(n, M, q):
    r = 1 - 1/q
    for d in range(1, n + 1):
        if d > r * n:
            max_M = math.floor(d / (d - r * n))
            if max_M < M:
                return d - 1  # Último valor válido
    return n

# Verifica si un código (n, d, q, M) cumple la cota de Plotkin.
# Devuelve una tupla (cumple, M_max). Si la cota no es aplicable, devuelve None.
def cotaPlotkinCheck(n, d, q, M):
    M_max = cotaPlotkin(n, d, q)
    if M_max is None:
        return None, None
    cumple = M <= M_max
    return cumple, M_max
