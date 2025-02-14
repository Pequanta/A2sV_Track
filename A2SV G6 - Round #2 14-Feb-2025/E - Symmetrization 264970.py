# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t = eval(input())

for _ in range(t):
    n = eval(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int , input())))
    def rotate_mat(mat):
        return [list(x) for x in zip(*mat[::-1])]
        
    first_rotation = rotate_mat(matrix)
    second_rotation = rotate_mat(first_rotation)
    third_rotation = rotate_mat(second_rotation)


    result = 0
    for i in range(len(first_rotation)):
        for j in range(len(first_rotation[0])):
            temp_sum = first_rotation[i][j] + second_rotation[i][j] + third_rotation[i][j] + matrix[i][j]
            if temp_sum == 3 or temp_sum == 1:
                result += 1
            elif temp_sum == 2:
                result += 2
    print(result // 4)
