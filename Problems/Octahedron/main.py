from math import sqrt

deck: int = int(input())

octa_area = 2 * sqrt(3) * deck ** 2
octa_vol = (1 / 3) * sqrt(2) * deck ** 3
print(round(octa_area, 2), round(octa_vol, 2))
