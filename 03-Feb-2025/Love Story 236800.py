# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = eval(input())

for _ in range(t):
    word = "codeforces"
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] != word[i]: 
            count += 1

    print(count)