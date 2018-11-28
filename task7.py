from random import randint

res = {0: 0, 1: 0, 2: 0, 3: 0}
total = pow(10, 4)
for i in range(total):
    res[randint(0, 1)*2 + randint(0, 1)] += 1

total -= res[3]
del res[3]

print('total=', res, sep='')
for k in res:
    print(k, '-', (res[k] * 100) / total, '%', sep='')
