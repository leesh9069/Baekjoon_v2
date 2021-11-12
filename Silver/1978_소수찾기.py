n = int(input())

num_list = list(map(int, input().split()))
cnt = 0

for i in num_list:
    not_cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                not_cnt += 1
        if not_cnt == 0:
            cnt += 1

print(cnt)