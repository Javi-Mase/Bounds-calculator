import math

# Calculamos el denominador de Johnson
def denominador(n, d, w, q) -> int:
    return q * w ** 2 - 2 * (q - 1) * n * w + n * d * (q - 1)


def cotaJohnsonRestringida(n, d, w, q) -> int:
    den = denominador(n, d, w, q)
    if den <= 0:
        raise ValueError(f"Jonson no restringida: \n El denominador q * w ** 2 - 2 * (q - 1) * n * w + n * d * (q - 1) es negativo")
    num = n * d * (q - 1)
    return math.floor(num / den)


def cotaJohnsonRestringidaInversa(n, M, w, q) -> int:
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        M_max = cotaJohnsonRestringida(n, mid, w, q)
        if M_max is not None and M_max >= M:
            lo = mid           # todavía cabe, intenta mayor d
        else:
            hi = mid - 1       # mid es demasiado grande
    return lo


def cotaJohnsonRestringidaCheck(n, d, w, q, M) -> tuple[bool, int | None]:
    M_max = cotaJohnsonRestringida(n, d, w, q)
    if M_max is None:
        return False, None
    return M <= M_max, M_max

