# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import Counter

n , k = map(int , input().split())
lst = list(map(int , input().split()))


cont_frequency = Counter()

solution = [1, 1]

left = 0
for right in range(len(lst)):
    cont_frequency[lst[right]] += 1
    while len(cont_frequency) > k:
        cont_frequency[lst[left]] -= 1
        if cont_frequency[lst[left]] == 0:
            cont_frequency.pop(lst[left])
        left += 1
    if solution[1] - solution[0] < right - left: 
        solution[0], solution[1] = left  + 1, right + 1
print(solution[0], solution[1])
