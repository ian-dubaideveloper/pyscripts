n, m, c = [int(i) for i in input().split()]
l = [*map(int, input().split())]
used = []
R = 0
USAGE = 0
B = []
for i in input().split():
    mx = int(i)
    used += (mx,)
    if used.count(mx) % 2:
        USAGE += l[mx - 1]
    else:
        USAGE -= l[mx - 1]
    B += (USAGE,)
    if USAGE > c:
        R = 1

print(
    [
        "Fuse was blown.",
        f"Fuse was not blown.\nMaximal consumed current was {max(B)} A.",
    ][R == 0]
)
