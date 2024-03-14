#Task 1
class Soda():
    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Soda and {self.ingredient}')
        else:
            print('Soda, just soda')


soda = Soda(ingredient='limon')
soda.show_my_drink()

#Task 2
class TriangleChecker():
    def __init__(self, sizes):
        self.sizes = sizes

    def is_triangle(self):
        if all(isinstance(size, (int, float)) for size in self.sizes):
            if all(size > 0 for size in self.sizes):
                sorted_sizes = sorted(self.sizes)
                if sorted_sizes[0] + sorted_sizes[1] > sorted_sizes[2]:
                    return 'U can build triangle'
                return 'U cann`t build triangle('
            return 'С отриц ничего не получится'
        return 'U`re needed числа'


trian1 = TriangleChecker([2,3,4])
print(trian1.is_triangle())
print('-'*20)
trian2 = TriangleChecker([1,1,3])
print(trian2.is_triangle())
print('-'*20)
trian3 = TriangleChecker([1,-2,3])
print(trian3.is_triangle())
print('-'*20)
trian4 = TriangleChecker([1,'2',3])
print(trian4.is_triangle())
