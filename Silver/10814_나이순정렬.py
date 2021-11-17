import sys

n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)
    lst.append([a, b])

lst.sort(key= lambda x : x[0])

for i in lst:
    print(i[0], i[1])
