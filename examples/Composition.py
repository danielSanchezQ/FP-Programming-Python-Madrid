from functools import partial, reduce
from operator import add, mul, mod


#Currying de funciones
#f(x,y,z) = f(x, g(y, h(z)))

f1 = lambda x, y, z : (x, y, z)
f2 = lambda x : lambda y : lambda z : (x,y,z)
print("Son iguales f1 y f2?")
print(f1(1,2,3) == f2(1)(2)(3))
#La ventaja de la f2, es que se puede aplicar parcialmente (llamado Uncurrying)
print("Aplicación parcial de f2 con valores x=2 y=3, llamamos a f3 con 5")
f3 = f2(2)(3)
print(f3(5))

#Python partial, uncurrying en python atraves de partial
add2 = partial(add, 2)
mul2 = partial(mul, 2)
print("usamos add2, que suma 2 al valor que le pasemos, 2 en este caso")
print(add2(2))

#Que pasa si queremos componerlas? a veces es facil, simplemente llamo una dentro de otra
# operateWith2 = add2(mul2())??????????
f1 = lambda x: x+1
f2 = lambda x: x*3
f3 = lambda x: x*x
l = [x for x in range(10)]
#IMPORTANTE, es mucho mas eficiente componer las fucniones que llamarlas por separado
#el siguiente ejemplo crea 3 listas
print("Composicion de funciones en map, mucho mas eficiente componerlas que no")
res = map(f1,map(f2,map(f3, l)))
print(list(res))
#este solo crea 1 lista
res = [f1(f2(f3(x))) for x in l]
print(res)
#entonces, si quiero usar map que hago¿?
#Herramientas para componer funciones

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


#ejemplo, componemos, sumar2, multiplicar por 2 y modulo en una sola funcion
print("operateWith2 = add2(mul2(mod(10,3)))")
operateWith2 = comp(add2, mul2, mod)
print(operateWith2(10, 3))

#Primer ejemplo
print("Primer ejemplo de composicion pero ahora con nuestra funcion")
ff = comp(f1, f2, f3)
print(list(map(ff, l)))
