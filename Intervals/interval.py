class IntervalError(Exception):
    def __init__(self, *args: object):
        super().__init__("Erreur : Bornes invalides !", *args)

class Interval:
    def __init__(self, start, end):
        if (
                start is None
                or end is None
                or not isinstance(start, int)
                or not isinstance(end, int)
                or start < 0
                or start > end
        ):
            raise IntervalError()

        self.start = start
        self.end = end

    def __str__(self):
        return f"Interval : {self.start} : {self.end}"

    def __contains__(self, item) -> bool:
        return self.start <= item <= self.end

    def __add__(self, other):
        return Interval(self.start + other.start, self.end + other.end)

    def __sub__(self, other):
        return Interval(self.start - other.start, self.end - other.end)

    def __mul__(self, other):
        return Interval(self.start * other.start, self.end * other.end)

    def __and__(self, other):
        new_start = max(self.start, other.start)
        new_end = min(self.end, other.end)
        if new_start <= new_end:
            return Interval(new_start, new_end)
        else:
            return None

try:
    interval = Interval(-1, 2)
except IntervalError as ex:
    print(ex)

try:
    interval = Interval(4, 2)
except IntervalError as ex:
    print(ex)

try:
    interval = Interval(None, 2)
except IntervalError as ex:
    print(ex)

try:
    interval = Interval(1, 2)
except IntervalError as ex:
    print(ex)


int1 = Interval(1, 2)
print(int1)
int2 = Interval(1, 2)
print("===contains===")
print(2 in int2)
print(3 in int2)
int3 = Interval(2, 5)
int4 = Interval(3, 4)
print("===add===")
print(int3 + int4)
print("===sub===")
print(int4 - int1)
print("===mul===")
print(int3 * int4)
print("===and===")
print(int3 & int4)