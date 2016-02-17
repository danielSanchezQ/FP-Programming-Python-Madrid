import math
from pprint import pprint



#MAP EXAMPLE
#RAIZ CUADRADA DE LOS PRIMERO 1000 DIGITOS
#Iterativo
res = []
for i in range(1, 1000):
    res.append(math.sqrt(i))
pprint(res)

#fp
pprint(list(map(math.sqrt, range(1, 1000))))

def iterativeSqrt():
    res = []
    for i in range(1, 1000):
        res.append(math.sqrt(i))
    return res

def fpSqrt():
    return list(map(math.sqrt, range(1, 1000)))

def comprehension():
    return [math.sqrt(x) for x in range(1, 1000)]

if __name__ == "__main__":
    from timeit import Timer
    itime   =   Timer("iterativeSqrt()", "from __main__ import iterativeSqrt").timeit(100)
    fptime  =   Timer("fpSqrt()", "from __main__ import fpSqrt").timeit(100)
    comtime =   Timer("comprehension()", "from __main__ import comprehension").timeit(100)
    pprint("Iterative time,     100 repeticiones  ->"  + str(itime))
    pprint("FP time,            100 repeticiones  ->"  + str(fptime))
    pprint("Comprehension time, 100 repeticiones  ->"  + str(comtime))