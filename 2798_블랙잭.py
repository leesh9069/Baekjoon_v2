from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))

a = list(combinations(lst, 3))
print(a)
b = []
for i in range(len(a)):
    if sum(a[i]) <= m:
        b.append(sum(a[i]))

print(max(b))