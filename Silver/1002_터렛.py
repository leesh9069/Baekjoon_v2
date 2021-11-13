n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    r = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    lst = [r1, r2, r]
    if r == 0 and r1 == r2:
        print(-1)
    elif r == r1 + r2 or r == abs(r1 - r2):
        print(1)
    elif r > r1 + r2 or abs(r1-r2) > r:
        print(0)
    else:
        print(2)