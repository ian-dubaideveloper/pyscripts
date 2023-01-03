l = input().split("0")
res = 1
for i in range(len(l) - 1):
    res = max(res, len(l[i]) + len(l[i + 1]) + 1)
print(res)
