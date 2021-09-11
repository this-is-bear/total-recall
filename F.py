import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
N = int(input())
N = abs(N)
while abs(N) > 0:
    a = abs(N) // 10
    b = N % 10
    M = a * 10 + b
if N < 0:
    print("-" + M)
print(N)