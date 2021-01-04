class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
  
    def get_attributes(self):
        return self.x, self.y, self.width, self.height

    def display_info(self):
        print(f'Rectangle({self.x}, {self.y}, {self.width}, {self.height})')

rect = Rectangle(5, 10, 50, 100)
rect.display_info()
