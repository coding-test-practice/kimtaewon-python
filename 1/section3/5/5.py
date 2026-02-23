# Todo: N, M / 배열 입력받기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

# Todo: merge sort? 개별 원소로 다 쪼갠 후 합쳐서 확인? 우선 보류
# Todo: brute force; 직접 더해가면서 세기. 1부터 for문 돌려서 세다가 M 도달하면 continue

cnt = 0
for i in range(N):
    sum = 0
    for j in range(i, N):
        sum += data[j]
        if sum == M:
            print(f"i: {i} j: {j} sum: {sum}")
            sum = 0
            cnt += 1
            break

# Todo: 결과 출력
print(cnt)