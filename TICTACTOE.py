grid = [list(input()), list(input()), list(input())]


def win(l):
    for i in range(3):
        if all(l[i][j] == "O" for j in range(3)) or all(
            l[j][i] == "O" for j in range(3)
        ):
            return True
    if all(l[i][i] == "O" for i in range(3)) or all(
        l[i][2 - i] == "O" for i in range(3)
    ):
        return True
    return False


for i in range(3):
    for j in range(3):
        if grid[i][j] != ".":
            continue
        l = [r.copy() for r in grid.copy()]
        l[i][j] = "O"
        if win(l):
            for row in l:
                print("".join(row))
            exit()
print("false")
