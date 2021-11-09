import sys
n = int(input())

check_list = [0] * 10001
lst = []

for i in range(n):
    num = int(sys.stdin.readline())
    check_list[num] += 1

for j in range(10001):
    if check_list[j] != 0:
        for k in range(check_list[j]):
            print(j)