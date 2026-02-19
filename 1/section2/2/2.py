import sys
input = sys.stdin.readline

T = int(input())
K = []
data = []

for i in range(T):
    N, s, e, k = map(int, input().split())
    data.append(list(map(int, input().split())))
    data[i] = data[i][s-1:e-1]
    data[i].sort()
    K.append(k)

for i in range(T):
    print(f"#{i+1} {data[i][K[i]-1]}")