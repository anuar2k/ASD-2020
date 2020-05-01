import functools
import math

# self is always Infinity, other = unknown type

@functools.total_ordering
class Infinity:
    def __init__(self, positive=True):
        self.__positive = positive

    def is_positive(self):
        return self.__positive

    @staticmethod
    def nan_check(to_check):
        if isinstance(to_check, float):
            return math.isnan(to_check)
        return False

    def __repr__(self):
        return "+infinity" if self.is_positive() else "-infinity"

    def __str__(self):
        return self.__repr__()

    def __hash__(self):
        return hash(self.is_positive())

    # +self
    def __pos__(self):
        return Infinity(self.is_positive())

    # -self
    def __neg__(self):
        return Infinity(not self.is_positive())

    # abs(self)
    def __abs__(self):
        return Infinity()

    # self < other
    def __lt__(self, other):
        if Infinity.nan_check(other):
            return False
        elif isinstance(other, Infinity):
            return not self.is_positive() and other.is_positive()
        return not self.is_positive()

    # self == other
    def __eq__(self, other):
        if isinstance(other, Infinity):
            return self.is_positive() == other.is_positive()
        return False

    # self + other
    def __add__(self, other):
        if Infinity.nan_check(other):
            return math.nan
        elif isinstance(other, Infinity):
            if self.is_positive() == other.is_positive():
                return Infinity(self.is_positive())
            else:
                return math.nan
        return Infinity(self.is_positive())

    # other + self == self + other
    def __radd__(self, other):
        return self + other

    # self - other == self + (-other)
    def __sub__(self, other):
        if isinstance(other, Infinity):
            other = -other
        return self + other

    # other - self == (-self) + other
    def __rsub__(self, other):
        return -self + other

    # self * other
    def __mul__(self, other):
        if Infinity.nan_check(other) or other == 0:
            return math.nan
        elif isinstance(other, Infinity):
            return Infinity(self.is_positive() == other.is_positive())
        return Infinity(self.is_positive() == (other > 0))
            
    # other * self == self * other
    def __rmul__(self, other):
        return self * other

    # self / other
    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError()
        if isinstance(other, Infinity):
            return math.nan
        return self * other

    # other / self
    def __rtruediv__(self, other):
        if Infinity.nan_check(other):
            return math.nan
        return 0.0 if self.is_positive() == (other > 0) else -0.0

    # self // other
    def __floordiv__(self, other):
        return self / other

    # other // self
    def __rfloordiv__(self, other):
        if Infinity.nan_check(other):
            return math.nan
        return 0

    # self % other
    def __mod__(self, other):
        if other == 0:
            raise ZeroDivisionError()
        return math.nan

    # other % self
    def __rmod__(self, other):
        if Infinity.nan_check(other):
            return math.nan
        if other == 0 or (self.is_positive() == (other > 0)):
            return other
        else:
            return Infinity(self.is_positive())

    # divmod(self, other)
    def __divmod__(self, other):
        return (self // other, self % other)

    # divmod(other, self)
    def __rdivmod__(self, other):
        return (other // self, other % self)
