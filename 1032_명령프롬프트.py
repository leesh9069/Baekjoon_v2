n = int(input())

total_lst = []
for _ in range(n):
    total_lst.append(input())

word = list(total_lst[0])

new_list = []
for i in range(n):
    for j in range(len(word)):
        if total_lst[i][j] == word[j]:
            continue
        else:
            word[j] = '?'

print("".join(word))