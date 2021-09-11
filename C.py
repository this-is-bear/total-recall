import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
(a, b) = [int(s) for s in input().split()]
a = int(input())
b = int(input())
c = int(input())
if a <= 0 and a >= 23:
    print("YES")
elif b >= 0 and b <= 60:
    print("YES")
elif c >= 0 and c <= 60:
    print("YES")
else:
    print("NO")