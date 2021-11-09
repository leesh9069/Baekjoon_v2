n = int(input())

lst = list(map(int, input().split()))
max_num = max(lst)

new_lst = []
for i in lst:
    new_lst.append((i/max_num)*100)
print(new_lst)
print(sum(new_lst)/len(new_lst))