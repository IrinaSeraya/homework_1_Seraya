# Пользователь вводит матрицу (список списков). Напишите функцию, которая транспонирует матрицу, не изменяя входную матрицу. 
# Транспонирование матрицы - операция над матрицей, когда ее строки становятся столбцами с теми же номерами.
i = int(input('Введите количество строк '))
matrix = []
for a in range(i):
    matrix.append(list(map(int, input().split())))
print(matrix)
def transp_matrix(matrix):
    transp_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transp_matrix
print(transp_matrix(matrix))