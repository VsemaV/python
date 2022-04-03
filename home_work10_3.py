class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return  self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Вычетание невозможно, т.к. ячеек в первой клетке <= чем во второй'

    def __mul__(self, other):
        return 'Multiply of cells is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Truediv of cell is ' + str(self.nums / other.nums)

cell_1 = Cell(10)
cell_2 = Cell(20)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_2 / cell_1)
print(cell_1.make_order(3))
