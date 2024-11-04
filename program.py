from rectangle import Rectangle

rectangle_1= Rectangle(2.54,3.7)

rectangle_1._width= 2.54
rectangle_1._height= 3.7

rectangle_2= Rectangle(4.1,5.6)
rectangle_2._width= 4.1
rectangle_2._height= 5.6

rectangle_1.description()
rectangle_2.description()

sum_area= rectangle_1.getArea()+ rectangle_2.getArea()
print(f"sum of area of two rectangles are {sum_area}")