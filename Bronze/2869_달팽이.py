# A, B, V 올라간거리, 미끄러진 거리, 목표
import math

A, B, V = map(int, input().split())
# A + n(A-B) = V
# n = V - A / A - B  3/1   1 / 4
print(math.ceil((V-A)/(A-B))+1)