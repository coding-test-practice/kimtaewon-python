# Todo: N / N개의 자연수 입력받기
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

# Todo: def reverse(x) 작성
def reverse(x):
    return int(str(x)[::-1])

# Todo: def isPrime(x) 작성
# x가 소수인가? -> 에라토스테네스 체 활용
# 리스트 p의 길이: data 최댓값
# 다 돌린 후 리스트에서 인덱스 검색하여 판단
def isPrime(x):
    p = [0] * (x + 1)  # 13 넣음=> 0~13
    for i in range(2, x):
        if p[i] == 0:
            for j in range(i, x+1, i):
                p[j] = 1
    return True if p[x] == 0 else False

# Todo: for문 (뒤집기 -> 소수 판별 -> 출력)
for d in data:
    d = reverse(d)
    if isPrime(d):
        print(d, end=' ')