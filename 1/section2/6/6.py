import sys
input = sys.stdin.readline

N = int(input())
data = list(input().split())

# Todo: 자릿수 더한 후 max 갱신
max_value = 0
max_num = 0
for d in data:
    temp = 0
    for i in d:
        temp += int(i)
    if temp > max_value:
        max_value = temp
        max_num = d

print(max_num)