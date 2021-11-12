# a, b = map(int, input().split())
#
# def primelist(n):
#     onehot = [True] * n
#     sqr = int(n**0.5)
#     for i in range(2, sqr+1):
#         if onehot[i]:
#             for j in range(2*i, n, i):
#                 onehot[j] = False
#
#     lst = []
#     for i in range(2, n):
#         if onehot[i]:
#             lst.append(i)
#     return set(lst)
#
# set_a = primelist(a)
# set_b = primelist(b)
#
# if set_a == set_b:
#     print(set_a)
# else:
#     result = list(set_b - set_a)
#     for i in result:
#         print(i)

m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1:
        continue

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)
