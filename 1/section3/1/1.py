# Todo: N 입력받기
import sys
input = sys.stdin.readline

N = int(input())

# Todo: 회문 문자열 여부 판단 함수
def calc(s):
    s = s.lower()
    print(f"s: {s} s[::-1]: {s[::-1]}")
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")

# Todo: for문 돌리기
for i in range(N):
    data = input()
    data = data[0:-1]
    calc(data)