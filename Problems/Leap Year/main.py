ret = int(input())
print("Leap" if ret % 4 == 0 and ret % 100 != 0 or ret % 400 == 0 else "Ordinary")
