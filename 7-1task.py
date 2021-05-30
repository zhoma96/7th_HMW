a = [[3, 2, 2, 9], [6, 7, 1, 1], [3, 2, 1, 6]]
b = [[2, 2, 5, 8], [6, 3, 4, 6], [6, 7, 4, 1]]

class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self,):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.lists)):
            sum_matrix.append([])
            for j in range(len(self.lists[0])):
                sum_matrix[i].append(self.lists[i][j] + other.lists[i][j])
            return '\n'.join(map(str, sum_matrix))

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)

print(matrix_1, '\n')
print(matrix_2, '\n')
print((matrix_1 + matrix_2))