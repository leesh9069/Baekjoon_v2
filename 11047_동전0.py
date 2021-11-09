N, K = map(int, input().split())

coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

while True:
    for i in coin_list:
        if i <= K: