import math


def h_q(x: float, q: int) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return (x * math.log(q - 1, q)
            - x * math.log(x,      q)
            - (1 - x) * math.log(1 - x, q))


def singletonAsintotica(delta: float) -> float:
    return max(0.0, 1.0 - delta)



def hammingAsintotica(delta: float, q: int) -> float:
    return max(0.0, 1.0 - h_q(delta / 2.0, q))



def plotkinAsintotica(delta: float, q: int) -> float:
    r = 1.0 - 1.0 / q
    if delta >= r:
        return 0.0
    return max(0.0, 1.0 - delta / r)



def eliasAsintotica(delta: float) -> float:
    if delta >= 0.5:
        return 0.0
    z = (1.0 - math.sqrt(1.0 - 2.0 * delta)) / 2.0
    if z <= 0.0 or z >= 1.0:
        return 1.0          # extremo δ=0
    return 1.0 + (z*math.log2(z) + (1-z)*math.log2(1-z))   # 1 − H₂(z)



def gilbertVarshamovAsintotica(delta: float, q: int) -> float:
    return max(0.0, 1.0 - h_q(delta, q))




def _h2(x: float) -> float:           # entropía binaria auxiliar
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1-x)*math.log2(1-x)

def lpAsintotica(delta: float) -> float:
    if not 0.0 <= delta <= 0.5:
        return 0.0                    # fuera del dominio útil
    root = math.sqrt(delta * (1.0 - delta))
    return _h2(0.5 - root)
