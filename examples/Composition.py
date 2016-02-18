from functools import partial, reduce
from operator import add, mul, mod




#Python partial
add2 = partial(add, 2)
mul2 = partial(mul, 2)
# operateWith2 = add2(mul2())??????????
f1 = lambda x: x+1
f2 = lambda x: x*3
f3 = lambda x: x*x
l = [x for x in range(10)]
res = map(f1,map(f2,map(f3, l)))
print(list(res))
res = [f1(f2(f3(x))) for x in l]
print(res)


#Composicion simple
def comp(*args):
    def compose(f, g):
        return lambda x: f(g(x))
    return reduce(compose, args)


operateWith2 = comp(add2, mul2)

print(operateWith2(10))

#Que pasa con los argumentos??¿?¿?¿?
def comp(*args):
    def compose(f, g):
        def wrapperArgsFunction(*args, **kwargs):
            return f(g(*args, **kwargs))
        return wrapperArgsFunction
    return reduce(compose, args)


operateWith2 = comp(add2, mul2, mod)

print(operateWith2(10, 3))

#Primer ejemplo
ff = comp(f1, f2, f3)
print(list(map(ff, l)))

if __name__ == "__main__":
    pass