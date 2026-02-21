import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

def reverse(x):
    return int(str(x)[::-1])

# 수정 1: 1 예외처리, 효율 고려
def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1): # range에 실수 들어가면 TypeError 뜸
        if x % i == 0:
            return False
    return True

for d in data:
    d = reverse(d)
    if isPrime(d):
        print(d, end=' ')