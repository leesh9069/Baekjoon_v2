N, K = map(int, input().split())

coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

a = 0
for i in coin_list:
    if i <= K:
        a += K // i
        K = K % i
        if K == 0:
            break
        continue
print(a)