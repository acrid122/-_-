'''
Списки (list) - упорядоченные, изменяемые коллекции данных в Python.
Они могут содержать элементы любого типа (числа, строки, другие списки, объекты) и поддерживают динамическое изменение размера.
'''
empty_list = [] #empty_list = list()
numbers = [1, 2, 3, 4]
mixed = [1, 'hello', 3.14, [5, 6], True]
repeats = [1, 2] * 10
add_list = [1, 2, 3] + [4, 5]
add_list += [3]

print(empty_list, numbers, mixed, repeats, add_list)

'''
Особенности:

Упорядоченные: элементы сохраняют порядок добавления.
Изменяемые: можно менять элементы, добавлять или удалять.
Поддерживают дубликаты: [1, 1, 2] — допустимый список.
Динамические: размер меняется автоматически.
'''

'''
Индексация (точно такая же, как в строках)
'''

#Можем обращаться к элементам строки по индексам.

#Индексация слева направо начинается с нуля. Индексация справа налево начинается с -1.

lst = ['apple', 'banana', 'cherry', 'lemon', 'melon']

print(lst[3])
print(lst[-2])
print(lst[1], lst[-4])

'''
Срезы (точно такие же, как в строках)
'''

#Срезы - выделить подстроку

'''
Срезы

s4[start:stop:step] работают по индексам

start - индекс начала среза (по умолчанию 0)
stop - индекс конца среза (по умолчанию конец строки). идет невключительно
step - шаг среза (по умолчанию 1)
'''

s5 = "hello, world!"

print(s5[2:5])
print(s5[:3]) #hel
print(s5[9:]) #rld!
print(s5[::4]) #hoo!
print(s5[::-5]) #!wl #когда шаг отрицательный, то, грубо говоря, позиции start и stop меняются местами
print(s5[-2:-7:-2]) #drw
print(s5[::-1]) #реверс строки

'''
Изменение
'''

#lst = ['apple', 'banana', 'cherry', 'lemon', 'melon']

lst[-1] = 'orange'
print(lst)

lst[-2:] = ['orange', 'pineapple']
print(lst)

a = [1, 2, 3]
b = a
b.append(4)
print(a)

'''
Методы списков
'''
#1. .append(x). Добавляет элемент x в конец списка

c = [1, 2, 3]
c.append(4)
print(c)

c.append([5, 6]) #добавляет в конец список [5, 6]
print(c)

#2. .extend(iterable). Добавляет все элементы из итерируемого объекта в конец списка

c.extend([7, 8])
print(c)

#3. .insert(ind, x). Вставляет элемент x по индексу ind

c.insert(1, 9) #c = c[:1] + [9] + c[2:]
#если индекс больше длины списка, то будет добавлять в конец
print(c)

#4. .remove(x). Удаляет первое вхождение элемента x (слева). Вызывает ValueError, если x нет.

c.remove(9)
print(c)

#5. .pop(ind = len(s) - 1). Удаляет и возвращает элемент по индексу i (по умолчанию удаляет последний элемент)

last = c.pop() 
print(c, last)
c.pop(4)
print(c)

#print(c.pop(10000000))
#IndexError: pop index out of range

#6. .clear(). Удаляет все элементы из списка. У нас останется пустой список.

d = [1, 2, 3]
d.clear()
print(d)

#Как удалить целиком объект из памяти
del d
#del d[0]
#NameError: name 'd' is not defined
#print(d)

#7. .index(x, start = 0, end = len(sp)). Возвращает индекс первого вхождения в диапазоне [start:end]. Вызывает ValueError, если x нет.
print(c.index(2))

#8. .count(x). Подсчитывает количество вхождений x
print(c.count(2))

#9. .sort(key = None, reverse = False). Сортирует список на месте. key - функция для кастомной сортировки. reverse - флажок для сортировок по убыванию/возрастанию (по умолчанию - по возрастанию)

c.insert(1, 9)
c.sort()
print(c)

c.sort(reverse = True)
print(c)

#['apple', 'banana', 'cherry', 'pumpkin', 'pineapple']

lst.sort(key = len)
print(lst)

lst.sort(key = len, reverse = True)
print(lst)

c = [1, 2, 3, 4]

c.sort(key = lambda x: x % 2 == 0)

#c = [False, True, False, True]
#c = [0, 1, 0, 1]
#c = [0, 0, 1, 1]
#c = [False, False, True, True]
print(c)

c = [1, 2, 3, 4]
new_c = list(map(lambda x: x + 2, c))

print(new_c)

def increase_2(x):
    return x + 2

new_c = list(map(increase_2, c))

print(new_c)

numbers = [[1, 2], [3, 4], [5, 6]]
numbers.sort(key = sum, reverse = True)
print(numbers)

numbers = [[1, 2, 4], [3, 4, 5, 6], [5, 6]]
numbers.sort(key = len, reverse = True)
print(numbers)

numbers = [[1, 2, 4], [3, 4, 5, 6], [5, 6]]
numbers.sort(key = max, reverse = True)            
print(numbers)

numbers = ['HH', '2D', '3F', '4I'] #20 СС
numbers.sort(key = lambda x: int(x, 20))
print(numbers)

numbers = [[1, 2], [3, 4], [5, 6], [1, -3], [0, 2]]
#[0, 2], [1, 2], [1, -3], [3, 4], [5, 6]
numbers.sort(key = lambda x: (x[0], -x[1]))

'''
[1, 2] -> (1, -2)
[3, 4] -> (3, -4)
[5, 6] -> (5, -6)
[1, -3] -> (1, 3)
[0, 2] -> (0, -2)

(0, -2), (1, -2), (1, 3), (3, -4), (5, -6)

[0, 2], [1, 2], [1, -3], [3, 4], [5, 6]
'''

numbers = [
    [1, -1, 3],
    [1, 9, 2],
    [0, 15, 3],
    [4, 2, 5],
    [5, 6, 7]
]

numbers.sort(key = lambda x: (-x[2], x[1], -x[0]))
print(numbers)

#Списковые включения

'''
Списковые включения - компактный способ создания списков с использованием выражений.
'''
a = [1, 2, 3, 4]

#Создать список квадратов чисел
new_a = [x ** 2 for x in a] #при помощи цикла for прохожусь по всем элементам списка a
print(new_a)

new_a = [x ** 2 for x in a if x % 2 == 0]
print(new_a)

new_a = [x ** 2 if x % 2 == 0 else 0 for x in a]
print(new_a)

numbers = [i ** 2 for i in range(1, 20)]
numbers = [i ** 2 if i % 4 == 0 else i for i in range(1, 20)]
numbers1 = ['12', '13', '15']
numbers = [int(x) for x in numbers1 if int(x) % 3 == 0]


numbers = []
for x in numbers1:
    if int(x) % 3 == 0:
        numbers.append(int(x))
print(numbers)

#10. .reverse(). Переворачивает список на месте.

a = c[::-1] #срез для переворота списка, создает новый объект
print(a)
a.reverse()
print(a)

#11. .copy(). Возвращает копию списка
new_a = a.copy()
print(new_a)

a = [1, 2, 3, 4]
b = a.copy()
b.append(4)
print(a, b)

p = [[1, 2], [3, 4], [5, 6]]
b = p.copy()
b[0][0] = 10
print(b, p)

'''
copy() - поверхностная копия. создает новый составной объект, а затем вставляет в него ссылки на объекты, находящиеся в оригинале.

deepcopy() - глубокая копия. создает новый составной объект, а затем рекурсивно вставляет в него копии объектов внутри, находящиеся в оригинале.
'''

from copy import deepcopy

p = [[1, 2], [3, 4], [5, 6]]
b = deepcopy(p)
b[0][0] = 10
print(b, p)


#Преобразование типов

#Из строки в список

s = 'a b c'

print(s.split(), list(s)) #['a', 'b', 'c'] ['a', ' ', 'b', ' ', 'c']

#Из списка сделать строку
sp = ['a', 'b', 'c'] #если все элементы списка - строковые
print(','.join(sp))

#Другие итерируемые объекты
print(tuple(sp)) #кортеж - неизменяемый список 

#Встроенные функции для списков

#1. len(lst). Возвращает длину списка

lst = [1, 2, 3]
print(len(lst))

#2. sum(lst). Суммирует элементы (для чисел)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(sum(lst))

#3. min(lst), max(lst). Находит мниимальный/максимальный элемент. Должны быть объекты одного типы данных.
print(min(lst), max(lst))

new_lst = ['a', 'b', 'c', '0', '1', '00000000000000']

#у всех символов в компьютере есть специальные номера (code point). эти code point расписаны в таблице unicode.
print(ord('0'))
#....цифры ... Заглавные буквы ... строчные буквы
print(ord('A'))
print(ord('a'))

#сравнение строк лексикографическое (посимвольное)

print(chr(65))

#4. sorted(iterable, key, reverse). Создает новый объект (то есть старый неотсортированный сохраняется). Возвращает список.
p = sorted(lst, reverse = True) #причем в sorted() можно передавать любые итерируемые объекты (список, кортеж, строка, множество ...)
print(p)

#5. map(func, iterable*). Применяет функцию к каждому элементу итерируемого объекта. Возвращает итератор.
lst = ['13', '454', '656']
print(list(map(int, lst)))


#6. zip(*iterables). Объединяет элементы из нескольких итерируемых объектов в кортежи.

names = ['Alice', 'Bob']
scores = [90, 85]
address = ['Moscow', 'Ufa']

print(list(zip(scores, names, address)))
