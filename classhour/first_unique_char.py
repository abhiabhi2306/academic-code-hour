n = int(input())
flag = False

for i in range(n):
    b = int(input())
    w = input()
    ans = [b for b in w if w.count(b) == 1]
    if ans:
        print(ans[0])
    else:
        print("-1")
