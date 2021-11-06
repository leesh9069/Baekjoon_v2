N = int(input())

for i in range(N):
    ox = list(input())
    ans = 0
    sum = 0
    for j in ox:
        if j == 'O':
            ans += 1
            sum += ans
        else:
            ans = 0
    print(sum)