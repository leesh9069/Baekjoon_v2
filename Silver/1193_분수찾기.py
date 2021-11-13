# import sys
# n = int(sys.stdin.readline())
#
# for i in range(1, n):
#     if int((i**2 - i +2)/2) <= n and int((i**2 + i +2)/2) > n :
#         group_num = i
#
# diff = int(n - ((group_num**2 - group_num + 2)/2))
#
# if group_num % 2 == 0:
#     upper = 1
#     print(upper+diff,'/',group_num+1-(upper+diff), sep='')
# else:
#     upper = group_num
#     print(upper-diff,'/',group_num+1-(upper-diff), sep='')


import sys
n = int(sys.stdin.readline())

num = 0
num_count = 0
while num_count < n:
    num += 1
    num_count += num

diff = n -(num_count - num + 1)

if num % 2 == 0:
    upper = 1 + diff
    lower = num + 1 -upper

else:
    upper = num - diff
    lower = num + 1 -upper

print(f"{upper}/{lower}")
