import numpy as np

class Vector3:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def Magnitude(self):
        return np.sqrt(self.i**2 + self.j**2 + self.k**2)
    
    def __add__(self, other: Vector3):
        return Vector3(self.i + other.i, self.j + other.j, self.k + other.k)
    
    def __sub__(self, other: Vector3):
        return Vector3(self.i - other.i, self.j - other.j, self.k - other.k) 
    
    def __mul__(self,other: float):
        return Vector3(self.i * other, self.j * other, self.k * other)
    
    def Unit(self):
        mag = Vector3.Magnitude(self)
        return Vector3(self.i / mag, self.j / mag, self.k / mag)
    
    def Dot(self, other: Vector3):
        return self.i * other.i + self.j * other.j + self.k * other.k
    
    def Cross(self, other: Vector3):
        i_comp = self.j * other.k - self.k * other.j
        j_comp = -(self.i * other.k - self.k * other.i)
        k_comp = (self.i * other.j - self.j * other.i)
        return Vector3(i_comp,j_comp,k_comp)
    
    def __div__(self, other: float):
        return Vector3(self.i / float, self.j / float, self.k / float)