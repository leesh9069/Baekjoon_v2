# n = int(input())-1
# a = n // 6
# if n == 0:
#     print(1)
# else:
#     cnt = 0
#     while True:
#         if ((cnt + 1) * cnt) / 2 >= a:
#             break
#         cnt += 1
#     print(cnt + 1)

N = int(input())
first = 1
plus = 6
room = 1
if N == 1:
    print(1)
else:
    while True:
        first = first + plus
        room += 1
        if N <= first:
            print(room)
            break
        plus += 6