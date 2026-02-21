import sys
input = sys.stdin.readline

N = int(input())

def calc(s):
    s = s.lower()
    return s == s[::-1]

# 수정 2: 공백 제거
for i in range(1, N+1):
    data = input().strip()
    print(f"#{i} {"YES" if calc(data) else "NO"}")