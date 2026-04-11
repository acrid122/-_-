from statistics import *

with open('9.1.txt') as f:
    sp = [list(map(int, line.split())) for line in f]

summa = 0
for line in sp:
    povt = [i for i in line if line.count(i) == 3]
    nepovt = [i for i in line if line.count(i) == 1]
    if len(povt) == 3 and len(nepovt) == 4:
        if mean(nepovt) <= mean(povt): #mean - срзнач итерируемого объекта
            summa = sum(line)
print(summa)

with open('9.2_2.txt') as f:
    sp = [list(map(int, line.split())) for line in f]

count = 0

for line in sp:
    povt = [i for i in line if line.count(i) == 3]
    nepovt = [i for i in line if line.count(i) == 1]
    if len(povt) == 3 and len(nepovt) == 3:
        if max(line) ** 2 + min(line) ** 2 >= (sum(line) - max(line) - min(line)) ** 2:
            count += 1

print(count)  
