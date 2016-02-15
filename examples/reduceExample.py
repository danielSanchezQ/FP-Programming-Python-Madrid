from functools import reduce
import random
from pprint import pprint

#REDUCE

RAND_LIST = [random.randrange(1000) for _ in range(1000)]
pprint(RAND_LIST)

#Iterative
def itMaxMin(l):
    itmax   = l[0]
    itmin   = l[0]
    for i in RAND_LIST:
        if i > itmax:
            itmax = i
        if i < itmin:
            itmin = 1
    return itmin, itmax

print(itMaxMin(RAND_LIST))

def builtinMaxMin(l):
    fmax = max(l)
    fmin = min(l)
    return fmin, fmax

print(builtinMaxMin(RAND_LIST))

def reduceMaxMin(l):
    return reduce(lambda vals, v: (min(v, vals[0]), max(v, vals[1])), l, (l[0], l[0]))
    #PYTHON2 return reduce(lambda (m, M), v: (v if v < m else m, v is v > M else M), l, (l[0], l[0]))

pprint(reduceMaxMin(RAND_LIST))

def maxMin(vals, v):
    m, M = vals
    return (v if v < m else m, v if v > M else M)

def noLambdaReduce(l):
    return reduce(maxMin, l, (l[0], l[0]))

if __name__ == "__main__":
    from timeit import Timer
    itime         =  Timer("itMaxMin(RAND_LIST)", "from __main__ import itMaxMin, RAND_LIST").timeit(100)
    builtin       =  Timer("builtinMaxMin(RAND_LIST)", "from __main__ import builtinMaxMin, RAND_LIST").timeit(100)
    reduceitime   =  Timer("reduceMaxMin(RAND_LIST)", "from __main__ import reduceMaxMin, RAND_LIST").timeit(100)
    nlreduceitime =  Timer("noLambdaReduce(RAND_LIST)", "from __main__ import noLambdaReduce, maxMin, RAND_LIST").timeit(100)
    pprint("Iterative time,             100 repeticiones  ->"  + str(itime))
    pprint("BuiltIn time,               100 repeticiones  ->"  + str(builtin))
    pprint("Reduceiime time,            100 repeticiones  ->"  + str(reduceitime))
    pprint("Reduceiime(No lambda) time, 100 repeticiones  ->"  + str(nlreduceitime))