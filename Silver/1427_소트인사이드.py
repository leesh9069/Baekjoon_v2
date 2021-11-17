n = input()

lst = [i for i in n]
lst.sort(reverse=True)

result = ''
for j in lst:
    result += j

print(result)