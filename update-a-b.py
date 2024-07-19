class A:
    def __init__(self):
        self.value = 1
    def update(self):
        self.value += 1
class B(A):
    def update(self):
        self.value *= 2

a = A()
b = B()

a.update()
b.update()

a, b = b, a 
a.update()
b.update()

print(a.value, b.value)