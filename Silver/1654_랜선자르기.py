# K, N = map(int, input().split())
#
# lst = []
# for _ in range(K):
#     lst.append(int(input()))
#
# minimum = min(lst)
#
# num = 0
# result = [0 for _ in range(minimum)]
# lst2 = []
# for i in range(1, minimum):
#     for j in range(K):
#         result[i-1] += lst[j] // i
#
#     if result[i-1] == N:
#         lst2.append(i)
#
# print(max(lst2))

K, N = map(int, input().split())

lst = []
for _ in range(K):
    lst.append(int(input()))

start, end = 1, max(lst)

while start <= end:
    mid = (start+end) // 2
    sum = 0
    for i in lst:
        sum += i // mid

    if sum >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)