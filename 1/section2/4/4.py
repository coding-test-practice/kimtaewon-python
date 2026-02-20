import sys
input = sys.stdin.readline

# 1. 입력받기
N = int(input())
data = list(map(int, input().split()))

# 2. 평균 계산
average = round(sum(data)/len(data), 1)

# 3. 딕셔너리 활용
dict = {x: (data[x-1]-average)**2 for x in range (1, N+1)}

# 4. 최솟값 찾기
for i in range(N):
    print(dict.keys())
    print(min(dict.values()))
    print(dict.get(i+1))