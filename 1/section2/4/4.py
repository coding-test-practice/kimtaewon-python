import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

average = round(sum(data)/len(data), 1)

for i in range(N):
