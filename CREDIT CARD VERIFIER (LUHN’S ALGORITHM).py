n = int(input())
for i in range(n):
    card = input().replace(" ", "")
    step_1 = [int(f) * 2 if int(f) * 2 < 10 else int(f) * 2 - 9 for f in card[-2::-2]]
    step_2 = sum(step_1)
    step_3 = sum(map(int, card[::-2]))
    step_4 = step_2 + step_3
    answer = "YES"
    if step_4 % 10:
        answer = "NO"
    print(answer)
