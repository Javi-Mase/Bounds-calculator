# Archivo: validar.py
# -------------------
# Valida parámetros comunes para las cotas de códigos.
# n: longitud del código (entero >= 1)
# d: distancia mínima (0 <= d <= n)
# M: tamaño de código   (1 <= M <= q**n)
# q: tamaño del alfabeto (entero >= 2)
# Lanza ValueError si algún parámetro está fuera de rango.

def validar(n=None, d=None, M=None, q=None):
    if q is not None:
        if not isinstance(q, int) or q < 2:
            raise ValueError(f"q debe ser un entero ≥ 2 (valor dado: {q})")

    if n is not None:
        if not isinstance(n, int) or n < 1:
            raise ValueError(f"n debe ser un entero ≥ 1 (valor dado: {n})")

    if d is not None:
        if not isinstance(d, int):
            raise ValueError(f"d debe ser un entero (valor dado: {d})")
        if n is not None and not (0 <= d <= n):
            raise ValueError(f"d debe estar en [0, n] (valor dado: {d}, n = {n})")

    if M is not None:
        if not isinstance(M, int):
            raise ValueError(f"M debe ser un entero (valor dado: {M})")
        if M < 1:
            raise ValueError(f"M debe ser ≥ 1 (valor dado: {M})")
        if n is not None and q is not None and M > q**n:
            raise ValueError(f"M no puede exceder qⁿ ({q}^{n} = {q**n}), valor dado: {M}")
