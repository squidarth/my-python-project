from bar.bar_utils import BarUtils

class FooUtils:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bar_utils = BarUtils(10)

    def sum(self):
        return self.x + self.y
    

    def product(self):
        return self.x * self.y