n = int(input())

for _ in range(n):
    H, W, N = map(int, input().split()) # 층수, 방수, 몇번째 손님

    num1 = N % H
    num2 = (N//H) + 1

    if N % H == 0:
        print(H * 100 + (N//H))
    else:
        print(num1*100+num2)