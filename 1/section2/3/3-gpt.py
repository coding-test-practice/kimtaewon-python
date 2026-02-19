import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))

# 개선 1: data2 리스트 만들지 말고 set 바로 활용
# 마이너: N을 받았으니 굳이 len(data)할 필요 X
data2 = set()
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for m in range(j+1, N):
            data2.add(data[i]+data[j]+data[m])

print(list(sorted(data2), reverse=True)[K-1])