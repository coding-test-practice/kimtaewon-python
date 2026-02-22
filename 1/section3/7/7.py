# Todo: N 입력받기
import sys
input = sys.stdin.readline

N = int(input())

# Todo: for문 써서 더하기 (입력 -> 홀수개씩 더하기)
result = 0
lt = rt = N//2
for i in range(N):
    temp = list(map(int, input().split()))
    result += sum(temp[lt:rt+1])

    if i < N//2:
        lt -= 1
        rt +=1
    else:
        lt += 1
        rt -= 1

# Todo: 결과 출력
print(result)