import math


class Vec3:
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, Vec3):
            self.x = x.x
            self.y = x.y
            self.z = x.z
            return
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        """Adds two `Vec3`s
        >>> v1 = Vec3(x=1); v2 = Vec3(x=2); v1+v2
        Vec3(x=3, y=0, z=0)
        """
        return Vec3(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __sub__(self, other):
        """Adds two `Vec3`s
        >>> v1 = Vec3(x=1); v2 = Vec3(x=2); v1-v2
        Vec3(x=-1, y=0, z=0)
        """
        return Vec3(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other):
        """Multiplys two `Vec3`s
        >>> v1 = Vec3(x=1); v2 = Vec3(x=2); v1*v2
        Vec3(x=2, y=0, z=0)
        >>> v2 = Vec3(x=2); v2*2
        Vec3(x=4, y=0, z=0)
        """
        if isinstance(other, (int, float)):
            return Vec3(self.x*other, self.y*other, self.z*other)
        return Vec3(self.x*other.x, self.y*other.y, self.z*other.z)

    def __repr__(self):
        return f'Vec3(x={self.x}, y={self.y}, z={self.z})'

    def __floordiv__(self, other):
        """Divides a Vec3 by a constant
        >>> v2 = Vec3(x=2); v2/2
        Vec3(x=1.0, y=0.0, z=0.0)
        """
        if not isinstance(other, (float, int)):
            raise ValueError('Only divide by constants are allowed!')
        return Vec3(self.x/other, self.y/other, self.z/other)
    __truediv__ = __floordiv__
    
    def __rtruediv__(self, other):
        """Divides a Vec3 by a constant
        >>> v2 = Vec3(x=1.0, y=2., z=1.0); 2.0/v2
        Vec3(x=2.0, y=1.0, z=2.0)
        """
        return Vec3(other/self.x, other/self.y, other/self.z)
    __rfloordiv__ = __rtruediv__

    def __abs__(self):
        """Computes absolute value of a `Vec3`
        >>> v2 = Vec3(x=4, y=3); abs(v2)
        5.0
        """
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    
    def abs_sq(self):
        """Computes absolute^2 value of a `Vec3`
        >>> v2 = Vec3(x=4, y=3); v2.abs_sq()
        25.0
        """
        return float(self.x**2+self.y**2+self.z**2)
    
    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def cross(self, other):
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x)
    
    def unit_vec(self):
        """
        >>> v2 = Vec3(x=4, y=3); v2.unit_vec()
        Vec3(x=0.8, y=0.6, z=0.0)
        """
        return Vec3(self/abs(self))


class Color(Vec3):
    def __str__(self):
        return f'{int(min(self.x*256, 255))} {int(min(self.y*256, 255))} {int(min(self.z*256, 255))}'