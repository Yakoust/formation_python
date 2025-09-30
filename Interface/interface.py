from abc import ABC

class Interface(ABC):
    __methods__ = ()

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is Interface:
            return all(any(m in B.__dict__ for B in subclass.__mro__) for m in cls.__methods__)
        return NotImplemented


class Container(Interface):
    __methods__ = ("__contains__",)

class Sized(Interface):
    __methods__ = ("__len__",)

class SizedContainer(Container, Sized):
    __methods__ = ("__len__", "__contains__")

class Iterable(Interface):
    __methods__ = ("__iter__",)

class MaListe:
    def __init__(self, data):
        self.data = list(data)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return iter(self.data)

print(issubclass(MaListe, SizedContainer))
print(issubclass(MaListe, Iterable))
print(issubclass(MaListe, Container))
