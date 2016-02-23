from operator import add
from itertools import tee, takewhile
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
def take(n, gen, consume = False):
    if not consume:
        _, it = tee(gen)
    else:
        it = gen
    for _ in range(n):
        yield next(it)

def zipWith(f, *args):
    yield from map(f, *args)
# Python 2 example
# def zipWith(f, it1, it2):
#     return (x for x in map(f, zip(it1, it2))

#Memoization c

def fibogen():
    a,b = 1,1
    yield a
    yield b
    while True:
        res = a+b
        a, b = b, res
        yield res

def autoStart(funct):
    @wraps(funct)
    def wrapper(*args, **kwars):
        gen = funct(*args, **kwars)
        next(gen)
        return gen
    return wrapper

@autoStart
def fiboSeq():
    gen     = fibogen()
    seq     = []
    size    = 0
    while True:
        required = (yield)
        if required  >= size:
            gap = required - size
            seq.extend(take(gap+1, gen, consume=True))
            size += gap
        yield seq[required]

def GenSendGet(v, gen):
    val = gen.send(v)
    next(gen)
    return val

if __name__ == "__main__":
    fiboseq = fiboSeq()
    print("Custom Range, puede ser infinito...")
    print(list(genRange(toN=10)))
    print("Llamadas a nuestro generador de fibonnacci con memoizacion")
    print(GenSendGet(0, fiboseq))
    print(GenSendGet(1, fiboseq))
    print(GenSendGet(2, fiboseq))
    print(GenSendGet(10, fiboseq))
    fibonnacci = fibogen()
    print("Coger 10 elementos de un generador de fibonacci y consumirlos (10)")
    print(list(take(10, fibonnacci, consume=True)))
    print("Sumar por pares los siguientes 10 numeros de la secuencia sin consumir esta")
    print(list(zipWith(add, take(10, fibonnacci), take(10, fibonnacci))))
    print("Sumar por pares de la secuencia de fibonacci hasta que estos sean mayores de 10000")
    print(list(takewhile(lambda x: x < 10000, zipWith(add, *tee(fibogen())))))
