s = "Кто-то сказал: Python — лучший язык программирования!"

count = 0

for i in s:
    if i.lower() in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'):
        count += 1

print(count)

print(sum(1 for i in s if i.lower() in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')))

'''
== - эквиваленция (тройное равно)

a == b = F
0 == 0 = 1
1 == 0 = 0
0 == 1 = 0
1 == 1 = 1

<= - импликация (->)

a <= b = F
0 <= 0 = 1
1 <= 0 = 0
0 <= 1 = 1
1 <= 1 = 1

!= - исключающее или

a != b = F
0 != 0 = 0
1 != 0 = 1
0 != 1 = 1
1 != 1 = 0
'''

'''
==, !=, <=

not, and, or
'''

'''
Порядок логических операций

not() -> and -> xor (исключающее или) -> or -> импликация -> эквиваленция

Поскольку импликация и эквиваленция обозначаются через операции сравнения, то в подобной записи

not x <= y. сначала будет выполняться <= (импликация), а только потом not. ЭТО НЕПРАВИЛЬНО. Сначала должен быть not, а только потом - импликация, поэтому необходимо брать в скобки
операции not, or, and, если они стоят рядом с импликацией, эквиваленцией и исключающим или, чтобы сохранить правильный порядок логических операций.
'''

print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = (x or y) and not(y == z) and not w
                if F:
                    print(x, y, w, z)


print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = ((x or y) <= z) or (y == w) or z
                if not F:
                    print(x, y, w, z)

print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = (z <= (not(y <= x))) or w
                if not F:
                    print(x, y, w, z)


from turtle import *

#fd(number) - вперед
#bk(number) - назад
#lt(number) - поворот налево
#rt(number) - поворот направо
#dot(size, color) - поставить точку
#goto(xcor, ycor) - перемещение на соответствующую координату
#up() - поднять хвост
#down() - опустить хвост
#tracer(False) - ускоряет движение. tracer(0) - моментальная отрисовка
#screensize(width, heigth) - изменение размера холста
#done() - завершение/фиксация рисунка на холсте
#update() - обновление экрана черепахи
#pos() - позиция черепашки относительно начала координат
#xcor() - получение абсциссы координаты
#ycor() - получение ординаты координаты
#heading() - получение угла поворота относительно начала координат


from turtle import *

screensize(5000, 5000)
tracer(0)
lt(90)
m = 5
for _ in range(8):
    fd(22 * m)
    rt(90)
    fd(33 * m)
    rt(90)

up()
bk(8 * m)
rt(90)
fd(11 * m)
lt(90)
down()

for _ in range(8):
    fd(73 * m)
    rt(90)
    fd(62 * m)
    rt(90)

up()

""" for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')

done() """


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not(y <= (x == z))) and (w <= x)
                if f:
                    print(x, y, z, w)


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (z <= y) or ((w <= x) <= y)
                if not f:
                    print(x, y, z, w)


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x and (not y)) or (y == z) or w
                if not f:
                    print(x, y, z, w)


print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((a or b) <= ((not c) and a)) and d
                if f:
                    print(a, b, c, d)


print('a b c d')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not(x <= y)) or (z == w) or z
                if not f:
                    print(x, y, z, w)