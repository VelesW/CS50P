import sys

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if type(n) is not int:
            raise ValueError("size of cookies should be an integer")
        if self.size + n > self.capacity:
            raise ValueError("Too much Cookies to fit inside the jar")

        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Lack of cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0 or type(capacity) is not int:
            raise ValueError("Capacity can't be negative and should be an integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise ValueError("size of cookies should be an integer")
        if size > self.capacity:
            raise ValueError("Too much Cookies to fit inside the jar")
        self._size = size

def main():
    jar = Jar()
    jar.deposit(10)
    print(jar)

if __name__ == "__main__":
    main()