class EAO:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)
        
    def __iadd__ (self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return EAO(x, y, z)
    
obj1 = EAO(2, 3, 3)
obj1 += EAO(3, 5, 5)
print(obj1)
        
        

