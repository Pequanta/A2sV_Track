# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n , m = map(int , input().split())

lst1 = list(map(int , input().split()))
lst2 = list(map(int , input().split()))


pt_one = pt_two = 0


result = []
while pt_one < len(lst1) and pt_two < len(lst2):
    if lst1[pt_one] < lst2[pt_two]:
        result.append(lst1[pt_one])
        pt_one += 1
    else:
        result.append(lst2[pt_two])
        pt_two += 1

if pt_one < len(lst1):
    while pt_one < len(lst1):
        result.append(lst1[pt_one])
        pt_one += 1
elif pt_two < len(lst2):
    while pt_two < len(lst2):
        result.append(lst2[pt_two])
        pt_two += 1

for i in range(len(result)):
    print(result[i] , end=" ")