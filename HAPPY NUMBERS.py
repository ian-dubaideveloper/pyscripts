n = int(input())
for i in range(n):
    s = x = int(input())
    k = 0
    smile = ":)"
    while x != 1 and k < 1000:
        x = sum(map(lambda a: int(a) ** 2, str(x)))
        k += 1
    if k >= 100:
        smile = ":("
    print(s, smile)
