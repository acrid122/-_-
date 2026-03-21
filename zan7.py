#23_24801

from functools import cache

@cache
def f(x, y, count = 0):
    if x == 24 or x == 32:
        count += 1
    if x > y:
        return 0
    if x == y and count == 1:
        return 1
    return f(x + 1, y, count) + f(x + 2, y, count) + f(x + 4, y, count) + f(x + 8, y, count)

print(f(16, 48))

#23_24800

from functools import cache

@cache
def f1(x, y, count = 0):
    if x in {20, 30, 40}:
        count += 1
    if x < y:
        return 0
    if x == y and count >= 2:
        return 1
    return f1(x - 1, y, count) + f1(x - 3, y, count) + f1(x // 3, y, count)

print(f1(49, 12))

#23_20198
def f2(a, b, s):
    if a > b + 2 or s == 'aaa': #a > b + 2, так как не может быть больше двух подряд команд a (вычитание 1)
        return 0
    if a == b:
        return 1
    return f2(a - 1, b, s[-2:] + 'a') + f2(a + 5, b, s[-2:] + 'b') + f2(a * 2, b, s[-2:] + 'c') #работаем со срезами, чтобы было эффективнее. достаточно хранить последние 2 символа, 
    #так как не может быть больше двух подряд команд a

print(f2(5, 34, ''))

#23_2340
def f3(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f3(a + 2, b) + f3(a + 4, b) + f3(a + 5, b)

for x in range(32, 100):
    if f3(31, x) == 1001:
        print(x)
        break
    
#23_19883
def f4(a, b):
    if a < b or a == 24:
        return 0
    if a == b:
        return 1
    return f4(a - 1, b) + f4(int(a ** 0.5), b) + f4(a // 10, b)

print(f4(602, 7))

#23_5640

#Сумма цифр числа
x = 123213123125465475674535342
print(sum(map(int, str(x)))) #сумма цифр числа в 10 СС числа. у map два параметра: название функции и итерируемый объект
x = '342378A9023B'
print(sum(map(lambda y: int(y, 12), x))) #сумма цифр числа в 12 СС 

def f5(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f5(a - 4, b) + f5(a - sum(map(int, str(a))), b) 

print(f5(36, 14) * f5(14, 2))

#23_2674

def f6(x, used): #x - текущее число, used - список использованных чисел для каждого варианта
    total = 0
    for d in (1, 3, -1, -3):
        nx = x + d
        if not (40 <= nx <= 49):
            continue
        if nx == 42:
            total += 1
            continue
        if nx in used:
            continue
        total += f6(nx, used + [nx])
    return total

print(f6(42, []))

#23_14419


def f7(a, b, d):
    if a > b or a == 30:
        return 0
    if a == b:
        return 1
    return f7(a + d, b, d) + f7(a * 2, b, d)

summa = 0
for d in range(1, 10): #так как траектория вычислений содержит 10
    summa += f7(1, 10, d) * f7(10, 100, d)

print(summa)

#23_11240
def f8(a, b, s):
    if a > b or s == 'bb': #bbababac
        return 0
    if a == b:
        return 1
    return f8(a + 2, b, s[-1:] + 'a') + f8(a ** 2, b, s[-1:] + 'b') + f8(a * 3, b, s[-1:] + 'c')
print(f8(2, 64, ''))

#23_3162
def f9(a, b, c = 0):
    if a > b or c > 1:
        return 0
    if a == b and c == 1:
        return 1
    return f9(a + 1, b, c) + f9(a + 2, b, c) + f9(a * 2, b, c + 1)
print(f9(2, 12))


def f10(x, m):
    #x - текущее количество камней в куче
    #m - количество ходов, которое осталось в игре
    if x >= 125:
        return m % 2 == 0 #тут проверка на четность. проверяю, что выигрывает именно Ваня
    if m == 0:
        '''
        Если верхнее условие не сработало, то вернется 0 (False), так как за нужное количество ходов не набралась сумма/
        '''
        return 0
    #Формирование списка ходов
    sp = [f10(x + 2, m - 1), f10(x + 4, m - 1), f10(x * 2, m - 1)]
    '''
    Вычитаю 1, так как только что был сделан ход
    '''
    return any(sp) if m % 2 != 0 else all(sp)

print(19, min(x for x in range(1, 125) if f10(x, 2)))
print(20, [x for x in range(1, 125) if not f10(x, 1) and f10(x, 3)])
print(21, [x for x in range(1, 125) if not f10(x, 2) and f10(x, 4)])

def f11(x, y, m):
    if x * y >= 541:
        return m % 2 == 0
    if m == 0:
        return 0
    sp = [f11(x + 10, y, m - 1), f11(x * 2, y, m - 1), f11(x, y + 10, m - 1), f11(x, y * 2, m - 1)]
    return any(sp) if m % 2 != 0 else all(sp)

print(19, min(i for i in range(1, 91) if f11(6, i, 2)))
print(20, [i for i in range(1, 91) if not f11(6, i, 1) and f11(6, i, 3)])
print(21, [i for i in range(1, 91) if not f11(6, i, 2) and f11(6, i, 4)])


def f12(x, y, m):
    if x * y >= 541:
        return m % 2 == 0
    if m == 0:
        return 0
    sp = [f12(x + 10, y, m - 1), f12(x * 2, y, m - 1), f12(x, y + 10, m - 1), f12(x, y * 2, m - 1)]
    return any(sp) if m % 2 != 0 else all(sp)

print(19, min(i for i in range(1, 91) if f12(6, i, 2)))
print(20, [i for i in range(1, 91) if not f12(6, i, 1) and f12(6, i, 3)])
print(21, [i for i in range(1, 91) if not f12(6, i, 2) and f12(6, i, 4)])


def f13(x, m):
    if x >= 88:
        return m % 2 == 0
    if m == 0:
        return 0
    s = [f13(x + 1, m - 1), f13(x + 4, m - 1), f13(x * 3, m - 1)]
    return any(s) if m % 2 != 0 else all(s)

print(19, [i for i in range(1, 88) if f13(i, 2)])
print(20, [i for i in range(1, 88) if not f13(i, 1) and f13(i, 3)])
print(21, [i for i in range(1, 88) if not f13(i, 2) and f13(i, 4)])