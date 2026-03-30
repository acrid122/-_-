#работа через import string

#разложение в виде a1 * p1 ** 0 + a2 * p2 ** 0 ...
#1010_2 = 2 ** 0 * 0 + 2 ** 1 * 1 ...


import string

s = string.printable

#Метод .index для поиска буквы H

number_H = s.index('h') + 1 #минимальная СС, где может быть H
#в .printable сначала идут цифры, а потом МАЛЕНЬКИЕ ЛАТИНСКИЕ БУКВЫ
for p in range(number_H, 37): #предположим, что p < 37, чтобы использовать int(), так как 2 <= int() <= 36
    ch1 = int('22A12E', p)
    ch2 = int('2F1391', p)
    ch3 = int('1H05D0', p)
    v = ch1 + ch2 - ch3
    if v % 19 == 0:
        print(v // 19)
        break


import string

s = string.printable

for x in s[:29][::-1]: #до 29 индекса невключительно, так СС - 29
    ch1 = int(f"923{x}874", 29)
    ch2 = int(f"524{x}6152", 29)
    v = ch1 + ch2
    if v % 28 == 0:
        print(v // 28)
        break

#0123....
#индексы
#0123... s[:3] -> 012

#надо наибольшее: переворачиваем строку -> break
#надо наименьшее: просто break

def summa(x, v):
    #[5, x, 3, 2, 1]
    #enumerate(...)
    '''
    [
        (5, 0) -> 68 ** 0 * 5
        (x, 1) -> 68 ** 1 * x
        (3, 2)
        (2, 3)
        (1, 4)
    ]
    '''
    return sum(v ** ind * i for ind, i in enumerate(x))

""" for x in range(67, -1, -1): #перевернул, чтобы применить break и найти максимальный x
    ch1 = 68 ** 0 * 5 + 68 ** 1 * x + 68 ** 2 * 3 + 68 ** 3 * 2 + 68 ** 4 * 1
    ch2 = 68 ** 0 * 3 + 68 ** 1 * 3 + 68 ** 2 * 2 + 68 ** 3 * x + 68 ** 4 * 1
    v = ch1 + ch2
    if v % 12 == 0:
        print(v // 12)
        break """

for x in range(67, -1, -1): #перевернул, чтобы применить break и найти максимальный x
    ch1 = summa([5, x, 3, 2, 1], 68)
    ch2 = summa([3, 3, 2, x, 1], 68)
    v = ch1 + ch2
    if v % 12 == 0:
        print(v // 12)
        break 

import string 

string.printable

for x in s[1:11]:
    ch1 = int(f"3364{x}", 11)
    ch2 = int(f"{x}7946", 12)
    ch3 = int(f"55{x}87", 14)
    if ch1 + ch2 == ch3:
        print(ch3)
        break

    '''
    for x in range(1, 60):
        ch1 = int(f"{x}893423", 14)

    ТАК ДЕЛАТЬ НЕПРАВИЛЬНО. НЕ НАДО МИКСИТЬ ДВА СПОСОБА (ЧЕРЕЗ СТРОКИ И ЧЕРЕЗ RANGE)
    то есть тут двухзнчаные значения будут воспринимать как отдельные цифры

    то есть 11 не как B, а как 1 и 1
    '''

    def summa(x, v):
        return sum(v ** ind * i for ind, i in enumerate(x))

    for x in range(6):
        for y in range(1, 6):
            ch1 = summa([x, y, x, 0, 1], 6)
            ch2 = summa([x, 1, 1, y], 7)
            if ch1 == ch2:
                print(x + y)



import string

s = string.printable[:21]

sp = []

for x in s:
    for y in s:
        ch1 = int(f"943697{x}21", 21)
        ch2 = int(f"2{y}9253", 21)
        v = ch1 - ch2
        if v % 20 == 0:
            sp.append((int(x, 21) - int(y, 21), v // 20))

sp.sort(reverse = True) #сортирую по убыванию, чтобы первая пара с начала списка имела НАИБОЛЬШЕЕ x - y
print(sp[:5])
#[(20, 17394273143), (0, 17394272702), (0, 17394263000), (0, 17394253298), (0, 17394243596)]


v = 2 * 2187 ** 2020 + 729 ** 2021 - 2 * 243 ** 2022  + 81 ** 2023 - 2 * 27 ** 2024 - 6561
count = 0

while v > 0:
    if v % 27 > 9:
        count += 1
    v //= 27

print(count)


for x in range(1, 3001):
    v = 9 ** 150 + 9 ** 30 - x
    count = 0
    while v > 0:
        if v % 9 == 0:
            count += 1
        v //= 9
    if count == 122:
        print(x)
        break


count = 0
start_number = max(int('1e0', 16), int('100002', 4))
finish_number = min(int('FEF', 16), int('333332', 4))

for x in range(start_number, finish_number + 1):
    if x % 4 == 2 and x // 16 % 16 == 14:
        count += 1
print(count)


import string 

s = string.printable[1:25]


st = {1} #множество - неупорядоченняа коллекция уникальных элементов (в множестве нет дубликатов)
for x in s:
    ch1 = int(f"8AF7{x}11", 25)
    ch2 = int(f"{x}DA87", 25)
    v = ch1 + ch2
    for y in range(1, 101):
        if v % y == 0:
            st.add(y)   #метод .add() - добавление в множество
print(len(st))

