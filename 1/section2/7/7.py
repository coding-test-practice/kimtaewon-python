import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
for i in range(2, N+1):
    isPrime = False
    for j in range(2, i):
        if i%j == 0:
            isPrime = False