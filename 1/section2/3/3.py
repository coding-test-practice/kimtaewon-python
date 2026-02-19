import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))

data2 = []
for i in range(0, len(data)-2):
    a = data[i]
    for j in range(i+1, len(data)-1):
        b = data[j]
        for m in range(j+1, len(data)):
            c = data[m]
            data2.append(a+b+c)

print(list(sorted(set(data2), reverse=True))[K-1])