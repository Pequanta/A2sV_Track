# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

t = eval(input())

for _ in range(t):
    n = eval(input())
    s = input()

    cont_right = set()

    cont_left = set()

    left_pre = [0]
    right_pre = []

    for i in range(n):
        cont_left.add(s[i])

        left_pre.append(len(cont_left))
        
    for i in range(n - 1, -1, -1):
        cont_right.add(s[i])

        right_pre.append(len(cont_right))

    right_pre = right_pre[::-1]
    right_pre.append(0)
    max_num = float("-inf")

    for i in range(len(right_pre)):
        max_num = max(max_num, right_pre[i] + left_pre[i])
    print(max_num)