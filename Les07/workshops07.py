workshops07.py
workshops07.rd
#--------------------------------- 1 -----------------------------------
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_list]))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)

a = Matrix([[15, 15], [15, 15], [15, 15]])
b = Matrix([[16, 7], [22, 28], [36, 71]])

print(a.__add__(b))

#-------------------------------- 2 -------------------------------------

from abc import ABC

class Clothes(ABC):
    def __init__(self, p):
        self.p = p

    @property
    def Consumption_full(self):
        full = round((self.p / 6.5) + 0.5 + float(2 * self.p) + 0.3)
        return f'total fabric consumption: {full} m.'

class Coat(Clothes):
    def Consumption(self):
        return f'coat fabric consumption: {round(self.p / 6.5 + 0.5)} m.'

class Suit(Clothes):
    def Consumption(self):
        return f'suit fabric consumption: {round(2 * self.p + 0.3)} m.'

# coat - size, suit - height
coat = Coat(48)
suit = Suit(172)

print(coat.Consumption())
print(suit.Consumption())
print(suit.Consumption_full)

#-------------------------------- 3 -------------------------------------
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
        print(self.quantity)

    def __add__(self, other):
        return f'Cell has grown: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Сells have shrunk: {sub}' if sub > 0 else 'the cell is gone'

    def __truediv__(self, other):
        return f'Cell divides: {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'the cell has grown: {self.quantity * other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(15)
cell_2 = Cell(3)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(4))