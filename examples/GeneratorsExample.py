from operator import add
from itertools import tee
from functools import wraps


#Haskell example fibonacci
# Prelude> let fibo = 1:1:zipWith (+) fibo (tail fibo)
# Prelude> take 10 fibo
# [1,1,2,3,5,8,13,21,34,55]

#Haskell [1..] -> [1,2,3,4,5,6,7...]
def genRange(fromN = 0, toN = -1):
    while True:
        yield fromN
        fromN += 1
        if toN != -1 and fromN > toN:
            raise StopIteration

#Haskell take 5 [1..] -> [1,2,3,4,5]
def take(n, gen):
    _, it = tee(gen)
    for _ in range(n):
        yield next(it)

def zipWith(f, *args):
    yield from map(f, *args)
# Python 2 example
# def zipWith(f, it1, it2):
#     return (x for x in map(f, zip(it1, it2))

#Memoization

def autoStart(funct):
    @wraps(funct)
    def wrapper(*args, **kwars):
        gen = funct(*args, **kwars)
        next(gen)
        return gen
    return wrapper

@autoStart
def fiboSeq():
    seq     = [1,1]
    size    = 2
    while True:
        required = (yield)
        if required  > size:
            while size < required+1:
                a, b = seq[size-2], seq[size-1]
                seq.append(a+b)
                size += 1
        yield seq[required]

fiboseq = fiboSeq()

def fibo(n):
    val = fiboseq.send(n)
    next(fiboseq)
    return val

def fibonacci():
    n = 0
    while True:
        val = fiboseq.send(n)
        next(fiboseq)
        yield val
        n += 1


if __name__ == "__main__":
    print(list(genRange(toN=10)))
    print(fibo(1))
    print(fibo(10))
    print(list(fibo(x) for x in range(10)))
    fibonacciSeq = fibonacci()
    print(list(take(10, fibonacciSeq)))
