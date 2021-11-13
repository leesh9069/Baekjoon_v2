"""sol1. 시간초과 발생"""
import sys
n = int(sys.stdin.readline())

lst = list(range(1, n+1))

while len(lst) >= 2:
    lst.pop(0)
    num = lst.pop(0)
    lst.append(num)

print(lst[0])
"""sol2. 라이브러리 풀이"""
from collections import deque

n = int(input())
deque = deque([i for i in range(1, n+1)])

while len(deque) >= 2:
    deque.popleft()
    num = deque.popleft()
    deque.append(num)

print(deque[0])