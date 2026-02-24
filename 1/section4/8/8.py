# Todo: N, M // w(N개) 입력 받기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

weights = list(map(int, input().split()))
weights.sort(reverse=True)

# Todo: 구명보트 개수 극소화 필요
# M/2 될 때까지 무거운 사람 먼저 태우고, 남은 사람들 찡겨앉게 하기

ans = 0
boats = []

for i in range(N):
    if weights[i] > M/2:
        boats.append([weights[i]])
        print(boats)
    else:
        for j in range(len(boats)):
            print(boats)
            if sum(boats[j]) + weights[i] < M:
                boats[j].append(weights[i])



print(boats)