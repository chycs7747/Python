class A:
    def __init__(self):
        self.num = 100
    def print(self):
        print("Called A")

class B:
    def __init__(self):
        self.num = 200
    def print(self):
        print("called B")

a = A()
b = B()

a.print()
a = b 
a.print()