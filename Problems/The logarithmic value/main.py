from math import log


raekwan = float(input())
ghost = float(input())

if ghost <= 1.0:
    print(round(log(raekwan), 2))
else:
    print(round(log(raekwan, ghost), 2))