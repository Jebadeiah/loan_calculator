in_value = int(input())
out_value = int(input())
count = 0

while in_value >= out_value:
    in_value = in_value / 2
    count += 1

print(count * 12)
