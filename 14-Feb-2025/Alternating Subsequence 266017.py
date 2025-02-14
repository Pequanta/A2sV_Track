# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = eval(input())

for _ in range(t):
    n = eval(input())
    lst = list(map(int , input().split()))


    max_negative = float("-inf")
    max_positive = float("-inf")

    total_sum = 0
    if len(lst) == 1:
        print(lst[0])
    else:
        if lst[0] < 0:
            prev_sign = False
            max_negative = lst[0]
        else:
            prev_sign = True
            max_positive = lst[0]
        stack = []
        for i in range(1, len(lst)):
            if i == len(lst) - 1:
                if lst[i] > 0 and prev_sign:
                    max_positive = max(max_positive, lst[i])
                    total_sum += max_positive
                elif lst[i] > 0 and not prev_sign:
                    total_sum += max_negative
                    total_sum += lst[i]
                elif lst[i] < 0 and not prev_sign:
                    max_negative = max(max_negative, lst[i])
                    total_sum += max_negative
                elif lst[i] < 0 and prev_sign:
                    total_sum += max_positive
                    total_sum += lst[i]
    
            else:
                if lst[i] > 0 and prev_sign:
                    max_positive = max(max_positive, lst[i])
                    prev_sign = True
                elif lst[i] > 0 and not prev_sign:
                    max_positive = lst[i]
                    total_sum += max_negative
                    max_negative = float("-inf")
                    prev_sign = True
                elif lst[i] < 0 and not prev_sign:
                    max_negative = max(max_negative, lst[i])
                    prev_sign = False
                elif lst[i] < 0 and prev_sign:
                    max_negative = lst[i]
                    total_sum += max_positive
                    max_positive = float("-inf")
                    prev_sign = False

        print(total_sum)

    