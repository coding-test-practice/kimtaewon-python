# 수정 1: 에라토스테네스 체 원리 사용
# 소수 여부를 저장하는 리스트를 만든 후, 2의 배수들부터 배수들 전부 제외
# 2 ~ 루트 N 까지만 찾으면 됨

import sys
input = sys.stdin.readline

N = int(input())

import time
start = time.perf_counter()

# 수정 2: 소수 여부 리스트 만들기
# N+1개의 0으로 리스트 초기화 (0번 인덱스는 무효)
isPrime = [0] * (N+1)

cnt = 0

# 수정 3: for문 돌리기
# 2에서 N까지 for(i)문 써서 카운트하는 건 같음
# 2가 소수인지, 3이 소수인지 .... 를 N까지 판단하기 위해 for(j) 문을 돌림
# 배수들 싹 제거
for i in range(2, N+1):
    if isPrime[i] == 0:
        cnt += 1
        for j in range(i, N+1, i):
            isPrime[j] = 1

print(cnt)

end = time.perf_counter()

print("걸린 시간:", end - start)

