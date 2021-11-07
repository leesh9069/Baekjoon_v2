# cycle = int(input())
# lst = []
#
# for _ in range(cycle):
#     lst.append(int(input()))
#
# lst.sort()
# for i in lst:
#     print(i)

import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')