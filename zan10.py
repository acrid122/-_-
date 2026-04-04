import string

s1 = string.printable

def f(a):
    s = ''
    while a:
        s = s1[a % 3] + s
        a //= 3
    return s


m = []
for n in range(1, 10000):
    n3 = f(n)

    if n % 2 == 0:
        n3 = '2' + n3 + f(int(n3[-1]) * 2) #срезы не нужны
    else:
        n3 = f(int(n3[0]) * 2) + n3 + '2'

    r = int(n3, 3)
    if r > 100:
        m.append(r)
print(min(m))

import string

s1 = string.printable

def f(x, base):
    s = ''
    while x:
        s = s1[x % base] + s
        x //= 12
    return s
    
m = []
for n in range(1, 1000):
    n_12 = f(n, 12)
    if n % 3 == 0:
        n_12 = '1' + n_12 + 'B'
    else:
        n_12 = '2' + n_12 + '0'
    r = int(n_12, 12)
    if r < 1996:
        m.append(r)
print(max(m))

import string

s1 = string.printable

def f(a):
    s = ''
    while a:
        s = s1[a % 6] + s
        a //= 6
    return s
    

m = []
for n in range(1, 10000):
    n1 = f(n)
    
    if n % 3 == 0:
        n1 += n1[:2]
    else:
        n1 = n1 + f((n % 3) * 10)
    
    r = int(n1, 6)
    if r > 680:
        m.append(r)
print(min(m))

m = []
for n in range(1, 10000):
    n1 = f'{n:b}'
    #sum(map(lambda x: int(x, 12), str(a)))

    if n % 2 == 0:
        n1 = f'{n1.count('1'):b}' + n1
        if n1.count('1') % 2 == 0:
            n1 += '0'
        else:
            n1 += '1'
    else:
        n1 = n1 + '0' + f'{n1.count('1'):b}'

    r = int(n1, 2)
    if r < 256:
        #если у тебя справшивают минимальное N, для которого должно быть максимальное R. или что-то подобное, то в список надо добавлять
        #ПАРУ ЭЛЕМЕНТОВ N И R, а потом сортировать
        m.append((r, n)) #нам надо найти такое n, чтобы r было максимальным -> первым элементом пары будет являться r, а вторым - n.
        #это связано с тем, что нам надо сначала найти максимальное r, а потом уже для него минимальное n. то есть первым критерием сортировки
        #должно быть именно r

m.sort(key = lambda x: (-x[0], x[1]))
print(m[:10])

m = []
for n in range(1, 10000):
    n1 = f'{n:b}'

    if n1.count('0') % 2 == 0:
        n1 = '1' + n1 + '1'
    else:
        n1 = '10' + n1

    r = int(n1, 2)
    if r < 100:
        m.append(r)
print(max(m))

import string

s1 = string.printable

def f(a):
    s = ''
    while a:
        s = s1[a % 3] + s
        a //= 3
    return s

        
m = []
for n in range(1, 10000):
    n1 = f(n)
    n2 = n1.replace('2', 'a').replace('0', '2').replace('a', '0') #когда ты переводишь в 10 СС при помощи int(), то там не учитывается
    r = int(n2, 3)
    res = abs(r - n) #модуль разности
    if res == 378:
        m.append(n)

print(min(m))

import string

s1 = string.printable

def f(x, base):
    s = ''
    while x:
        s = s1[x % base] + s
        x //= base
    return s

m = []

for n in range(1, 10000):
    n_4 = f(n, 4)
    if len(n_4) % 2 == 0: #len() - количество значащих цифр
        #1221 -> 12_0_21 -> len() = 4, 12 = n_4[:len(n_4)]
        n_4 = n_4[:len(n_4) // 2] + '0' + n_4[len(n_4) // 2:]
    r = int(n_4) #в задаче сказано, что получаемое число n_4 уже в десятичной системе
    if r <= 180:
        m.append(n)

print(max(m))

import string

s1 = string.printable

def f(a):
    s = ''
    while a:
        s = s1[a % 3] + s
        a //= 3
    return s


m = []


for n in range(1, 10000):
    n1 = f(n)
    q = sum(map(int, n1))
    if q % 2 == 0:
        n1 = '1' + n1 + '2'
    else:
        n1 = '2' + n1 + '0'

    r = int(n1, 3)
    if r > 100:
        m.append(r)
print(min(m))

m = []
for n in range(1, 10000):
    n1 = f'{(n * 2):b}'
    n2 = n1 + str(n1.count('1') % 2)
    n3 = n2 + str(n2.count('1') % 2)
    r = int(n3, 2)
    if r > 249:
        m.append(n)
print(min(m))

import string

s1 = string.printable

def f(a):
    s = ''
    while a:
        s = s1[a % 6] + s
        a //= 6
    return s
    

m = []
for n in range(1, 10000):
    n1 = f(n)
    q = sum(map(int, n1))
    if q % 5 == 0:
        n1 = '11' + n1.replace('0', 'q').replace('3', '0').replace('q', '3')
    else:
        n1 = n1[0] + '05' + n1[3:] + '44'
        
    r = int(n1, 6)
    if r >= 1500:
        m.append((r, n))
m.sort(key = lambda x: (x[0], -x[1]))
print(m[:10])



s = [(1, 2), (1, 3), (2, 4), (0, 5), (0, 6)] #отсортировать в порядке убывания первого элемента пары (R), но по возрастанию второго элемента (N)

s.sort(key = lambda x: (-x[0], x[1]))


# '''
# key = - ключ сортировки. сюда надо прописывать функцию, по которой осуществляется сортировка.
# эта функция будет применяться к каждому элементу итерируемого объекта и возвращать результат. к результатам применяется сортировка

# если функции нет, то реализуем через lambda.

# lambda x: ... - в x последовательно будет передавать по порядку элементы итерируемого объекта

# (1, 2) -> (-1, 2)
# (1, 3) -> (-1, 3)
# (2, 4) -> (-2, 4)
# (0, 5) -> (0, 5)
# (0, 6) -> (0, 6)

# к этим результатам применяется сортировка. если мы работаем просто с .sort() - сортировка по возрастанию, если с .sort(reverse = True) - 
# то с сортировкой по убыванию.

# итерируемые объекты сравниваются поэлементно.

# первый элемент будет (-2, 4), так как у него наименьший первый элемент среди всех пар.

# (-2, 4), (-1, 2), (-1, 3), (0, 5), (0, 6) - отсортированные результаты

# [(2, 4), (1, 2), (1, 3), (0, 5), (0, 6)] - готовый список. подтягиваем исходные данные

# при сортировке по убыванию ставим -
# '''

m = []

a, b = (1, 2) #a = 1, b = 2

sp = [1, 2]
sp1 = [3, 4, 5]
sp.extend(sp1)
#[1, 2, 3, 4, 5]
#sp.append(sp1)
#[1, 2, [3, 4, 5]]
print(sp)

for i in range(1000, 10 ** 4):
    x, y, w, z = map(int, str(i)) #str(i) = '1000' -> map(int, str(i)) -> map-object из 4 элементов
    pr = [x * y, x * w, x * z]
    pr.sort()
    max_pr, max_pr2 = pr[1:]
    s = str(max_pr) + str(max_pr2)
    if s == '5472':
        m.append(i)
print(min(m))


def f(a, b, count = 0):
    if a in {48, 61}:
        count += 1
    if a < b or count > 1:
        return 0
    if a == b and count == 1:
        return 1
    return f(a - 1, b, count) + f(a // 2, b, count) + f(a // 3, b, count)
    
    
print(f(106, 6))

def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    sp = [] #в этот список будем записывать результаты каждого вызова
    if a % 10 == 0:
        if a < 20:
            if len(set(str(a))) != len(str(a)): #проверка на то, что нет одинаковых цифр
                pass
            else:
                s_a = str(a)
                maxa, mina = int(max(s_a)), int(min(s_a))
                sp.append(f(a + maxa - mina, b))
        else:
            sp.append(f(a * int(str(a)[0]), b))
            if len(set(str(a))) != len(str(a)): #проверка на то, что нет одинаковых цифр
                pass
            else:
                s_a = str(a)
                maxa, mina = int(max(s_a)), int(min(s_a))
                sp.append(f(a + maxa - mina, b))
    else:
        sp.append(f(a + a % 10, b))
        if a < 20:
            if len(set(str(a))) != len(str(a)): #проверка на то, что нет одинаковых цифр
                pass
            else:
                s_a = str(a)
                maxa, mina = int(max(s_a)), int(min(s_a))
                sp.append(f(a + maxa - mina, b))
        else:
            sp.append(f(a * int(str(a)[0]), b))
            if len(set(str(a))) != len(str(a)): #проверка на то, что нет одинаковых цифр
                pass
            else:
                s_a = str(a)
                maxa, mina = int(max(s_a)), int(min(s_a))
                sp.append(f(a + maxa - mina, b))
                
    return sum(sp)
print(f(21, 62))


def f(a, b):
    if int(a, 2) < int(b, 2):
        return 0
    if a == b:
        return 1
    return f(f'{int(a, 2) - 1:b}', b) + f(a[:-1], b)

print(f('100001', '100'))

def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a - 1, b) + f(int(f'{a:b}'[:-1], 2), b)

print(f(33, 4))