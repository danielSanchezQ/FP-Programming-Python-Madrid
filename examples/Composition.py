from functools import partial, reduce, wraps
from operator import add, mul, mod


# HASKELL STYLE: operateWith2 = (+) 2 . (*) 2
add2 = partial(add, 2)
mul2 = partial(mul, 2)
# operateWith2 = add2(mul2())??????????

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


