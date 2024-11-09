matrix = [
    [710, 4334, 3483, 5554, 93, 3776, 7272, 434, 8028, 7264],
    [7909, 4394, 2181, 595, 204, 5274, 9520, 931, 1074, 7914],
    [537, 2488, 221, 2982, 2077, 4088, 4948, 7703, 6901, 9055],
    [5559, 7666, 7520, 26, 7479, 3188, 3179, 9080, 2998, 1152],
    [1319, 565, 3659, 3863, 5273, 4287, 2816, 3573, 7305, 5651],
    [8688, 2991, 5008, 2218, 7331, 569, 930, 4206, 1547, 22],
    [2180, 7008, 3027, 597, 9550, 440, 6826, 9153, 7700, 2889],
    [4929, 5792, 8233, 2604, 3764, 7251, 7469, 9888, 3777, 3286],
    [4535, 5478, 4723, 872, 5162, 4547, 1570, 5542, 6809, 6064],
    [3936, 2606, 1269, 7249, 1156, 6134, 8334, 5816, 1425, 6467],
]

# validate it is a matrix
print(len(matrix), len(matrix[0]))

""" 
a) Realize uma soma de todos os numeros da ultima coluna

b) Realize uma soma de todos os numeros

c) Realize uma soma dos numeros do meio (A matriz tem 10 colunas)

d) Realize uma soma na diagonal 

e) Realize uma soma na diagonal (invertido)
"""


def exercise_a(matrix):
    return sum(row[-1] for row in matrix)


def exercise_b(matrix):
    return sum(sum(row) for row in matrix)


def exercise_c(matrix):
    total_sum = 0

    for row in matrix:
        row_size = len(row)
        mid = row_size // 2

        if row_size % 2 == 0:
            before_mid = mid - 1
            total_sum += row[mid] + row[before_mid]
        else:
            total_sum += row[mid]

    return total_sum


def exercise_c_comprehension(matrix):
    n = len(matrix)
    mid = n // 2
    before_mid = mid - 1
    return sum(row[mid] + row[before_mid] if n % 2 == 0 else row[mid] for row in matrix)


def exercise_d(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def exercise_e(matrix):
    n = len(matrix[0]) - 1

    total_sum = 0
    idx = 0
    while idx < len(matrix[0]):
        total_sum += matrix[idx][n - idx]

        idx += 1
    return total_sum


def exercise_e_comprehension(matrix):
    n = len(matrix[0]) - 1
    return sum(matrix[idx][n - idx] for idx in range(len(matrix[0])))
