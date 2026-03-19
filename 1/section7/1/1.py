N = int(input())

def div(n):
    if n > 0:
        r = n%2
        n //= 2
        div(n)
        print(r, end="")


div(N)