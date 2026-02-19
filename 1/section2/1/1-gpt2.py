# 개선 1: sys.stdin.readline을 input에 재바인딩하기
import sys
input = sys.stdin.readline # 이렇게 쓰는 게 더 깔끔!
n, k = map(int, input().split())

# 개선 2: 정방향, 역방향용 배열 따로 만들기 (어차피 합치면 되니까)
forward = []
backward = []

i = 1
while i*i <= n:
    if n%i==0:
        forward.append(i)
        if n//i != i:
            backward.append(n//i)
    i = i + 1

# 개선 3: ===리스트 반전하기===
# [::-1] 인덱싱 활용
answer = forward + backward[::-1]

if k >= n:
    print(-1)
else:
    print(answer[k-1])