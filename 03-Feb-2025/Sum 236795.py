# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t = eval(input())

for _ in range(t):
    a, b , c = map(int , input().split(" "))
    if abs(a - b) == c or a + b == c:
        print("YES")
    else:
        print("NO")