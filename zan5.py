print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = w and ((z or y) == (z and x))
                if not f:
                    print(x, y, z, w)

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = w and ((y <= x) <= z)
                if not f:
                    print(x, y, z, w)

""" Фибоначчи без мемоизации
def fib(n):
    if n == 1: return 0
    if n == 2: return 1
    return fib(n - 2) + fib(n - 1)

print(fib(6))

print(fib(39)) """

#Чтобы добавить мемоизацию, надо использовать декоратор. Декоратор - просто надстройка над функцией.

from functools import cache #cache - декоратор, который добавляет возможность функции кэшировать значения

@cache #декоратор пишется сверху над определением функции через @
def fib(n):
    if n == 1: return 0
    if n == 2: return 1
    return fib(n - 2) + fib(n - 1)

print(fib(6))

print(fib(39))
print(fib(150))

#Любую рекурсию можно переписать в виде итеративного алгоритма. И любой итеративный алгоритм можно переписать в рекурсию

#Динамическое программирование.

sp = [0] * 151 #чтобы был 150-ый индекс. Чтобы найти 150-ый номер
sp[2] = 1
for i in range(3, 151):
    sp[i] = sp[i - 2] + sp[i - 1]

print(sp[150])

""" from sys import setrecursionlimit

setrecursionlimit(9000) """

from functools import cache

@cache 
def f(n):
    return n if n <= 10 else n - 7 + f(n - 21)

for i in range(185735):
    f(i)

print((f(185734) - f(185650)) / f(40))

#RecursionError: maximum recursion depth exceeded

sp = [0] * 10 ** 9
for n in range(185735):
    if n <= 10:
        sp[n] = n
    else:
        if n - 21 < 0:
            sp[n] = n - 7 + (n - 21)
        else:
            sp[n] = n - 7 + sp[n - 21]
print(((sp[185734] - sp[185650]) / sp[40]))