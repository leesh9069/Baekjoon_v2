# import sys
# n = int(input())
# total = []
# for _ in range(n):
#     person = list(map(int, sys.stdin.readline().split()))
#     total.append(person)
#
# total2 = total.copy()
# total2.sort(key = lambda x: x[0], reverse=True)
#
# print(total)
# print(total2)
#
# rank_list = [1]
# cnt = 1
# for i in range(len(total)-1):
#     if total2[i][1] > total2[i+1][1]:
#         rank_list.append(rank_list[i]+cnt)
#     else:
#         rank_list.append(rank_list[i])
#         cnt += 1
#
# pair_list = []
# for pair in zip(total2, rank_list):
#     pair_list.append(pair)
#
# print(pair_list)
#
# for i in total:
#     for j in range(len(pair_list)):
#         if i == pair_list[j][0]:
#             print(pair_list[j][1], end=" ")

n = int(input())
person_list = []

for _ in range(n):
    w, h = map(int, input().split())
    person_list.append((w,h))

for i in person_list:
    rank = 1
    for j in person_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end = " ")