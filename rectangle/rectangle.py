class Rectangle:
    """ Definition d'un rectangle """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def perimeter(self) -> float:
        return 2 * self.width + self.height

    def area(self) -> float:
        return self.width * self.height

class Parallelepiped(Rectangle):
    """ Definition d'un parallélépipède """

    def __init__(self, width: float, height: float, depth: float):
        super().__init__(width, height)
        self.depth = depth

    def volume(self) -> float:
        return self.width * self.height * self.depth

    def perimeter(self) -> float:
        return 4 * (self.width + self.height + self.depth)

    def area(self) -> float:
        return 2*((self.width * self.height) + (self.width * self.depth) + (self.height * self.depth))


if __name__ == "__main__":
    rectangle = Rectangle(100, 60)
    print(f"Périmètre du rectangle: {rectangle.perimeter()}")
    print(f"Aire du rectangle: {rectangle.area()}")
    parellelepipede = Parallelepiped(100, 60, 30)

    print(f"Périmètre du parellelepipede: {parellelepipede.perimeter()}")
    print(f"Aire du parellelepipede: {parellelepipede.area()}")
    print(f"Volume du parellelepipede: {parellelepipede.volume()}")
