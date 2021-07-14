a = [[31, 37, 51], [22, 43, 86]]
b = [[3, 2, -1], [5, 4, 64]]

class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
            return '\n'.join(map(str, c)) 

matrx1 = Matrix(a)
matrx2 = Matrix(b)

print(matrx1, '\n')
print(matrx2, '\n')
print(matrx1 + matrx2)