class disjointSet:
    def __init__(self, n):
        self.data = [i for i in range(n)]
        self.size = n
 
    def find(self, idx):
        return self.data[idx]
 
    def union(self, x, y):
        print("case: x=",x,"y=",y)
        x, y = self.find(x), self.find(y)
        if x == y:
            print("x:",x,"y:",y,"are same")
            return

        for i in range(len(self.data)):
            if self.data[i] == y:
                print("before self.data[i]:",self.data[i], "i:",i)
                self.data[i] = x
                print("after self.data[i]:",self.data[i], "i:",i)
                print(s.data)
        self.size -= 1
 
 
s = disjointSet(10)
s.union(0, 1)
s.union(2, 3)
s.union(1, 2)
s.union(0, 1)
s.union(4, 5)
s.union(5, 6)
s.union(7, 8)
s.union(7, 9)
 
print(s.data)
print(s.size)

tt = [-1 for _ in range(10)]
print(tt)