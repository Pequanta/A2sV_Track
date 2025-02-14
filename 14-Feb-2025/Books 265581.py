# Problem: Books - https://codeforces.com/contest/279/problem/B

n , t = map(int , input().split())

lst = list(map(int , input().split()))

total_minutes = 0

left = 0

max_books = float("-inf")

for right in range(len(lst)):
    total_minutes += lst[right]
    while total_minutes > t:
        total_minutes -= lst[left]
        left += 1
    max_books = max(max_books, right - left + 1)
print(max_books)
    