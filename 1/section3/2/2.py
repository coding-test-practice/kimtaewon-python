# Todo: 문자열 입력 받기
import sys
input = sys.stdin.readline

S = input()

# Todo: 자연수 만들기 -> 결과 출력
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
temp = ""
for s in S:
    if s in num:
        temp += s
value = int(temp)
print(value)

# Todo: 약수 계산하기 -> 결과 출력
forward = []
backward = []
for i in range(1, int(value ** 0.5) + 1):
    if value%i == 0:
       forward.append(i)
backward = sorted(map(lambda x: value // x, forward), reverse=True)

print(len(set(forward + backward)))