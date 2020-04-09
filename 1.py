class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        matrix = ''
        for i in range(len(self.lst)):
            for j in range(len(self.lst[i])):
                matrix += str(self.lst[i][j]) + ' '
            matrix += '\n'
        return matrix

    def __add__(self, other):
        def sum_lists(list_1, list_2):
            sum_l = []
            for i in range(len(list_2)):
                sum_l.append(list_1[i] + list_2[i])
            return sum_l

        new_lst = []
        if len(self.lst) == len(other.lst) or len(self.lst[0]) == len(other.lst[0]):
            for i in range(len(self.lst)):
                new_lst.append(sum_lists(self.lst[i], other.lst[i]))
            return Matrix(new_lst)
        else:
            raise Exception


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix_3 = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
print(matrix_1)
print(matrix_3)
print(matrix_1 + matrix_3)

try:
    print(matrix_1 + matrix_2)
except:
    print('Нельзя складывать матрицы разных размеров!')
