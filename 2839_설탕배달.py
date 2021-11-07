n = int(input()) #18

num1 = n // 5 #3
lst = []
for i in range(0, num1+1):  #0123
    num2 = n - (5*i) #18 13 8 3
    if num2 % 3 == 0:
        num3 = num2 // 3
        lst.append(int(num3+i))

if len(lst) == 0:
    print(-1)
else:
    print(min(lst))