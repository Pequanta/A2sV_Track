# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int , input().split())

lst = list(map(int,  input().split()))


total_sum = 0
answer = 0
left = 0

for right in range(len(lst)):
    total_sum += lst[right]
    while total_sum > s: 
        total_sum -= lst[left]
        left += 1
    answer = max(answer, right - left + 1)

print(answer)

