class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self): # this method makes the class iterable. It uses yield to return a dictionary containing length first, and then width
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 5)
for dimension in rect:
    print(dimension)
