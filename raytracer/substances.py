import math


class Vec3:
    def __init__(self, x=0, y=0, z=0, t=0):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
    
    def __add__(self, other):
        """Adds two `Vec3`s
        >>> v1 = Vec3(x=1); v2 = Vec3(x=2); v1+v2
        Vec3(x=3, y=0, z=0, t=0)
        """
        return Vec3(self.x+other.x, self.y+other.y, self.z+other.z, self.t+other.t)
    
    def __sub__(self, other):
        """Adds two `Vec3`s
        >>> v1 = Vec3(x=1); v2 = Vec3(x=2); v1-v2
        Vec3(x=-1, y=0, z=0, t=0)
        """
        return Vec3(self.x-other.x, self.y-other.y, self.z-other.z, self.t-other.t)

    def __mul__(self, other):
        """Multiplys two `Vec3`s
        >>> v1 = Vec3(x=1); v2 = Vec3(x=2); v1*v2
        Vec3(x=2, y=0, z=0, t=0)
        """
        return Vec3(self.x*other.x, self.y*other.y, self.z*other.z, self.t*other.t)

    def __repr__(self):
        return f'Vec3(x={self.x}, y={self.y}, z={self.z}, t={self.t})'

    def __floordiv__(self, other):
        """Divides a Vec3 by a constant
        >>> v2 = Vec3(x=2); v2/2
        Vec3(x=1.0, y=0.0, z=0.0, t=0.0)
        """
        if not isinstance(other, (float, int)):
            raise ValueError('Only divide by constants are allowed!')
        return Vec3(self.x/other, self.y/other, self.z/other, self.t/other)
    
    def __truediv__(self, other):
        """Divides a Vec3 by a constant
        >>> v2 = Vec3(x=2); v2/2
        Vec3(x=1.0, y=0.0, z=0.0, t=0.0)
        """
        return self.__floordiv__(other)
    
    def __rtruediv__(self, other):
        """Divides a Vec3 by a constant
        >>> v2 = Vec3(x=2); v2/2
        Vec3(x=1.0, y=0.0, z=0.0, t=0.0)
        """
        return self.__floordiv__(other)
    
    def __rloordiv__(self, other):
        """Divides a Vec3 by a constant
        >>> v2 = Vec3(x=2); v2/2
        Vec3(x=1.0, y=0.0, z=0.0, t=0.0)
        """
        return self.__floordiv__(other)
    
    def __abs__(self):
        """Computes absolute value of a `Vec3`
        >>> v2 = Vec3(x=4, y=3); abs(v2)
        5.0
        """
        return math.sqrt(self.x**2+self.y**2+self.z**2+self.t**2)
    
    def abs_sq(self):
        """Computes absolute^2 value of a `Vec3`
        >>> v2 = Vec3(x=4, y=3); v2.abs_sq()
        25.0
        """
        return float(self.x**2+self.y**2+self.z**2+self.t**2)