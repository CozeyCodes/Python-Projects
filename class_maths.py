

class polygon:

    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height


class square(polygon):

    def perimeter_square(self):
        return 4*(self.length)
    
    def area_square(self):
        return (self.length)*(self.length)

class rectangle(polygon):

    def perimeter_rectangle(self):
        return 2*((self.length)+(self.breadth))

    def area_rectangle(self):
        return ((self.length)*(self.breadth))

class cube(polygon):

    def volume_cube(self):
        return (self.length)**3

x = square(2,3,5)
y = rectangle(2,3,5)
z = cube(2,3,5)

print(f"The Perimeter of Square is {x.perimeter_square()}.")
print(f"The Area of Square is {x.area_square()}.")

print(f"The Perimeter of Rectangle is {y.perimeter_rectangle()}.")
print(f"The Area of Rectangle is {y.area_rectangle()}.")

print(f"The Perimeter of Square is {z.volume_cube()}.")
