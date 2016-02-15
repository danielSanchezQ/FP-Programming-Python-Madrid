from pprint import pprint


TEST_LIST = range(2, 1000)

def iterativePrimes(l):
    ret = []
    for e in l:
        for i in range(2, e):
            if (e % i) == 0:
                break
        else:
            ret.append(e)
    return ret

pprint(iterativePrimes(TEST_LIST))

def filterPrimes(l):
    return list(filter(lambda x: all(x % i for i in range(2, x)), l))

pprint(filterPrimes(TEST_LIST))

def isPrime(v):
    return all(v % i for i in range(2,v))

def filterPrimesNoLamda(l):
    return list(filter(isPrime, l))

pprint(filterPrimesNoLamda(TEST_LIST))

def comprehensionPrimes(l):
    return [x for x in l if all(x%i for i in range(2,x))]

pprint(comprehensionPrimes(TEST_LIST))

if __name__ == "__main__":
    from timeit import Timer
    itime   =   Timer("iterativePrimes(TEST_LIST)", "from __main__ import iterativePrimes, TEST_LIST").timeit(100)
    fptime  =   Timer("filterPrimes(TEST_LIST)", "from __main__ import filterPrimes, TEST_LIST").timeit(100)
    fpnolambdatime =  Timer("filterPrimesNoLamda(TEST_LIST)", "from __main__ import filterPrimesNoLamda, isPrime, TEST_LIST").timeit(100)
    comtime =   Timer("comprehensionPrimes(TEST_LIST)", "from __main__ import comprehensionPrimes, TEST_LIST").timeit(100)
    pprint("Iterative time,     100 repeticiones  ->"  + str(itime))
    pprint("FP time,            100 repeticiones  ->"  + str(fptime))
    pprint("FP time, no lambda  100 repeticiones  ->"  + str(fpnolambdatime))
    pprint("Comprehension time, 100 repeticiones  ->"  + str(comtime))