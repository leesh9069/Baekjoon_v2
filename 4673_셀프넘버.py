new_list = []
for i in range(1, 10001):
    num = i
    for j in str(num):
        num += int(j)
    new_list.append(num)

num_list = [k for k in range(1, 10001)]

result = set(num_list) - set(new_list)
result = sorted(result)

for i in result:
    print(i)
