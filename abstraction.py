from abc import ABCMeta, abstractmethod
import collections
from abc import ABC


class IStream(metaclass=ABCMeta):
    """
    error: a = IStream()  # TypeError: Can't instantiate abstract class
                          # IStream with abstract methods read, write


    """

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print(maxbytes)
        pass

    def write(self, data):
        pass


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


if __name__ == '__main__':
    # method two
    import io

    # Register the built-in I/O classes as supporting our interface
    # IStream 作为原类创建的类具有 register
    IStream.register(io.IOBase)

    # Open a normal file and type check
    f = open('foo.txt')
    print(isinstance(f, IStream))
