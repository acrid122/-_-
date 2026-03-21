""" """ """ from functools import cache


@cache
def f(n):
    if n > 80_000:
        return 100
    return f(n + 1) * n

for i in range(80050, 0, -1):
    f(i)

print((f(50) // 100 + f(53)) // f(55))

from fractions import Fraction

@cache
def f(n):
    if n > 80_000:
        return 100
    return f(n + 1) * n

for i in range(80050, 0, -1):
    f(i)

print((Fraction(f(50), 100) + f(53)) // Fraction(f(55)))
#OverflowError: integer division result too large for a float


m = [0] * 10 ** 9
m[1] = 1
for n in range(2, 2100):
    m[n] = (n - 1) * m[n -1]
print((m[2024] + 2 * m[2023]) // m[2022])

from functools import cache

@cache
def f1(n):
    if n == 3:
        return 1
    return 5 * f1(n - 1) + 6 * g1(n - 1) - 3 * n + 8

@cache
def g1(n):
    if n == 3:
        return 1
    return 6 * f1(n - 1) + 5 * g1(n - 1) + 3

print(f1(9) + g1(9)) """

""" m = [0] * 10 ** 9
n = [0] * 10 ** 9

for i in range(10000):
    if i > 2029:
        m[i] = i
    else:
        m[i] = i + 2 + m[i + 2]


for k in range(10000):
    if k <= 2030:
        n[k] = k
    else:
        n[k] = k - 2 + n[k - 2]

print(n[2100] - m[2100])


m = [0] * 10 ** 9

for n in range(16):
    if n < 5:
        m[n] = 1 + 2 * n
    if n >= 5 and n % 3 == 0:
        m[n] = 2 * (n + 1) * m[n - 2]
    if n >= 5 and n % 3 != 0:
        m[n] = 2 * n + 1 + m[n - 1] + 2 * m[n - 2]
print(m[15]) 


from functools import cache

@cache
def f2(n):
    if n < 5:
        return 1 + 2 * n
    elif n >= 5 and n % 3 == 0:
        return 2 * (n + 1) * f2(n - 2)
    return 2 * n + 1 + f2(n - 1) + 2 * f2(n - 2)

print(f2(15)) """ """

f = [0] * 10 ** 6
g = [0] * 10 ** 6

for n in range(310000, -1, -1):
    if n > 303728:
        g[n] = n - 15
    else:
        g[n] = g[n + 8] / 2 - 109

for n1 in range(10000):
    if n1 < 128:
        f[n1] = 5 * g[n1 - 7] + 29
    else:
        f[n1] = f[n1 - 5] + 1092
print(f[2049])

f = [0] * 10 ** 5
c = 0

for n in range(10000):
    if n < 3:
        f[n] = n * 4
    if n >= 3 and n % 2 == 1:
        f[n] = n * 2
    if n >= 3 and n % 2 == 0:
        f[n] = 5 * f[n - 2] + n ** 2

for i in f:
    if 100 <= abs(i) < 1000 and abs(i) % 2 == 0:
        c += 1
print(c)

"""
def f(a, b):
    if a == b:
        return 1
    if a > b or a % 3 == 0:
        return 0
    return f(a - 1, b) + f(a + 3, b) + f(a * 2, b)

print(f(5, 100))


def f1(a, b, s = ''):
    if a < b or s[-3:] == 'AAA' or s[-3:] == 'BBB':
        return 0
    if a == b:
        return 1
    if a % 2 == 0:
        return f1(a - 2, b, s[-2:] + 'A') + f1(a / 2, b, s[-2:] + 'B')
    else:
        return f1(a - 2, b, s[-2:] + 'A') + f1(a - 7, b, s[-2:] + 'B')

print(f1(40, 1)) 


def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a // 10 % 10 < a % 10:
        s = str(a)
        s = s[:-2] + s[-1] + s[-2]
        return f(a + 1, b) + f(int(s), b)
    else:
        return f(a + 1, b) 
print(f(101, 154))