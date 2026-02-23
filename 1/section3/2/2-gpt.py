import sys
input = sys.stdin.readline

S = input()

# 수정 1: isdigit 사용, join 사용
temp = ''.join(c for c in S if c.isdigit())
value = int(temp)
print(value)

# 수정 2: 약수 세기 정석
cnt = 0
for i in range(1, int(value ** 0.5) + 1):
    if value%i == 0:
       if i == value%i:
           cnt += 1
       else:
           cnt += 2

print(cnt)