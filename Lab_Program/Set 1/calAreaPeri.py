def Area(length, breadth):
    return length * breadth
def Perimeter(length, breadth):
    return 2 * (length + breadth)
length = float(input("Enter the Length of rectangle: "))
breadth = float(input("Enter the Breadth of rectangle: "))

area = Area(length,breadth)
perimeter = Perimeter(length,breadth)
print(f"{area} is area of rectangle ")
print(f"{perimeter} is perimeter of rectangle ")