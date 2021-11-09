import sys

n = int(sys.stdin.readline())
nlst = set(map(int, sys.stdin.readline().split()))
m = int(input())
mlst = list(map(int, sys.stdin.readline().split()))

for i in mlst:
    if i in nlst:
        print(1)
    else:
        print(0)