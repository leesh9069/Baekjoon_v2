# N : 나무의 수 / M : 가져가려고 하는 나무의 길이
import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start+end) // 2
    sum = 0
    for i in tree:
        if i >= mid:
            sum += i - mid

    if sum >= M :
        start = mid + 1
    else:
        end = mid - 1
print(end)
