import sys

n = int(sys.stdin.readline())

total_lst = []

for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    total_lst.append(lst)

total_lst.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end_time = total_lst[0][1]
for i in range(1, n):
    if total_lst[i][0] >= end_time:
        end_time = total_lst[i][1]
        cnt += 1
print(cnt)