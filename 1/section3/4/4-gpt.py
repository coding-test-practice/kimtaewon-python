import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))

# 수정 1: Merge sort 활용
result = []

p1 = 0
p2 = 0

while p1 < N and p2 < M:
    if n_list[p1] <= m_list[p2]:
        result.append(n_list[p1])
        p1 += 1
    else:
        result.append(m_list[p2])
        p2 += 1

while p1 < N:
    result.append(n_list[p1])
    p1 += 1

while p2 < M:
    result.append(m_list[p2])
    p2 += 1


print(*result)
