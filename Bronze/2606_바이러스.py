n = int(input())
num = []

for _ in range(n):
    lst = list(map(int, input().split()))
    num.append(lst)

num = sorted(num, key=lambda x: (x[0], x[1]))

for i in num:
    print(i[0], i[1])