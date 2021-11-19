"""
1월 : 1일이 월요일 / 7로 나눈 나머지 1 - 월요일
2월 : 1일이 목요일 /
3월 : 1일이 목요일
4월 : 1일이 일요일
5월 : 1일이 화요일
6월 : 1일이 금요일
7월 : 1일이 일요일
8월 : 1일이 수요일
9월 : 1일이 토요일
10월 : 1일이 월요일
11월 : 1일이 목요일
12월 : 1일이 토요일
"""

x, y = map(int, input().split())

sun = [4, 7]
mon = [1, 10]
tue = [5]
wed = [8]
thu = [2, 3, 11]
fri = [6]
sat = [9, 12]

day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

num_day = y % 7
if x in sun:
    print(day[num_day-1])
elif x in mon:
    print(day[num_day])
elif x in tue:
    print(day[num_day-6])
elif x in wed:
    print(day[num_day-5])
elif x in thu:
    print(day[num_day-4])
elif x in fri:
    print(day[num_day-3])
else:
    print(day[num_day-2])
