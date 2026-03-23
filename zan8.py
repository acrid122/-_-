""" '''
#Как перевести из 10 СС в 2СС
'''

#1. bin()
print(bin(10)[2:]) #0b1010
#2. f''
print(f'{10:b}')
#3. format
print(format(10, 'b'))

'''
#Как перевести из 10 СС в 8СС
'''

#1. oct()
print(oct(10)[2:])
#2. f''
print(f'{10:o}')
#3. format
print(format(10, 'o'))

'''
#Как перевести из 10 СС в 16СС
'''

#1. hex()
print(hex(10)[2:])
#2. f''
print(f'{10:x}')
#3. format
print(format(10, 'x'))

#В результате перевода в 16 СС получаются буквы в нижнем регистре.

print('A' in hex(10)[2:]) #False из-за нижнего регистра

'''
Как перевести из N СС (2 <= N <= 36) в 10 СС
'''
print(int('a', 16))
#int поддерживает СС в диапазоне (2 <= N <= 36). Всего 10 цифр и 26 латинских букв

'''
Перевести из СС > 36
'''

#456 в 70 СС
print(70 ** 0 * 6 + 70 ** 1 * 5 + 70 ** 2 * 4)

'''
Как перевести из 10 СС в любую другую.
'''

import string

print(string.digits) #все цифры
print(string.ascii_uppercase) #все заглавные
print(string.printable) #все печатные символы

s = string.printable

def f(number, base):
    s1 = ''
    while number > 0:
        s1 = s[number % base] + s1
        number //= base
    return s1

print(f(99, 25))

def f_rec(number, base):
    return '' if number == 0 else f_rec(number // base, base) + string.printable[number % base]

print(f_rec(99, 25))
#1. Подсчет суммы цифр числа

#Число в СС <= 10

s = 12345
print(sum(map(int, str(s))))

#Число в СС > 10 (например, 16)

print(sum(map(lambda x: int(x, 16), str(s))))

#2. Множественная замена

#Заменить 3 -> 4, 5 -> 6, 7 -> 8, 9 -> 0

s = '3456895637569382456'

s = s.replace('3', '4').replace('5', '6').replace('7', '8').replace('9', '0')
print(s)

s = '3456895637569382456'
#maketrans, translate
table = str.maketrans('3579', '4680', '12') #создание таблицы перевода
print(s.translate(table)) #применение таблицы перевода.
#третий параметр в maketrans - то, что нужно "удалить"

#3. Как брать последние N цифр:

#N < 10
for n in range(10): #range(2, 10)
    bin_n = f'{n:b}'
    #last_2_letters = bin_n[-2] + bin_n[-1]
    '''
    если использовать прямое обращение по индексу, то 
    возникнет ошибка IndexError, так как есть числа, которые
    просто не содержат два знака.

    Пофиксить можно только обрезанием диапазона
    '''
    #Лучший вариант - использование срезов, так как срезы не дают ошибок
    last_2_letters = bin_n[-2:]
    pass

#4. Как сделать N-битную двоичную запись.

#1. .zfill(n) - заполнить нулями слева до длины n

t = f'{10:b}'
print(t.zfill(8))

#2. Использование f-строк
t = f'{10:08b}'
print(t)

#5. Что делать, если в 5 номере требуется определить (например)
#максимальное N, при котором R максимально и меньше или равно чему-то
#В список добавляем пары.
sp = []

for n in range(1, 10 ** 4):
    n_2 = f'{n:b}'
    if n % 2 == 0:
        n_2 = n_2.replace('0', '1')
        #1010 -> 1111 -> 0000 | 0101. промежуточный .replace()
    else:
        n_2 = '1' + n_2[1:].replace('1', '00')
    r = int(n_2, 2)
    if r < 600:
        sp.append((r, n))
        #первым в пару добавляется r, так как по нему необходимо сначала проводить сортировку, а потом уже n

sp.sort(reverse = True)
print(sp[:10])

"""
s = []

for n in range(1, 10000):
    n_2 = f'{n:b}'
    if n % 3 == 0:
        n_2 += n_2[-3:]
    else:
        n_2 += f'{(n % 3) * 3:b}'
    r = int(n_2, 2)
    if r >= 200:
        s.append(n)
print(min(s))


m = []

for n in range(1, 10000):
    n2 = f'{n:b}'
    if n % 2 == 0:
        n2 = n2 + '10'
    else:
        n2 = '1' + n2 + '01'
    r = int(n2, 2)
    if r < 30:
        m.append(n)
print(max(m))

import string
s1 = string.printable


def f(a):
    s = ''
    while a > 0:
        s = s1[a % 3] + s
        a //= 3 
    return s


m = []

for n in range(1, 10000):
    n3 = f(n)
    if n % 3 == 0:
        n3 = '1' + n3 + '02'
    else:
        n3 += f((n % 3) * 4)

    r = int(n3, 3)
    if r < 100:
        m.append(n)
print(max(m))


m = []

for n in range(1, 10000):
    n2 = f'{n:b}'
    if n % 3 == 0:
        n2 += n2[-3:]
    else:
        n2 += f'{((n % 3) * 3):b}'

    r = int(n2, 2)
    if r < 130:
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
    n3 = f(n)
    """ n4 = n3.count('1') + n3.count('2') * 2 """
    if n % 3 == 0:
        n3 += n3[:3]
    else:
        n3 += f(sum(map(int, n3)) * 5)

    r = int(n3, 3)
    if r > 2500 and r % 2 == 1:
        m.append(r)
print(min(m))