import math


class Polygons:

    def __init__(self, num_sides, side_length):
        """
        A class that represents a regular polygon.

        attributes:
            - num_sides: the number of sides of the polygon
            - side_length: the length of each side of the polygon
            - radius: the radius of the circumscribed circle of the polygon
            - area: the area of the polygon
        """

        # TODO 1: Create an attribute called num_sides and set it to the num_sides given in the constructor
        pass  # Replace this line with your code
    
        num_sides = num_sides
        #Change
        
        

        # TODO 2: Create an attribute called side_length and set it to the side_length given in the constructor
        pass  # Replace this line with your code
    
        side_length = side_length

        # TODO 3: Create an attribute called radius and set it equal to the result of the following formula:
        # - side_length / (2 * sin(pi / num_sides))
        # - use the math library to get the value of pi and the sin() function
        pass  # Replace this line with your code
    
        radius = side_length / (2 * math.sin(math.pi / num_sides))

        # TODO 4: Create an attribute called area and set it equal to the result of the polygon_area() method
        pass  # Replace this line with your code
    
        area = self.polygon_area()

    def polygon_area(self):
        """
        Method that calculates the area of the polygon from the number of sides and side length.
        returns:
            - the area of the polygon
        """
        return self.num_sides * self.side_length ** 2 / (4 * math.tan(math.pi / self.num_sides))
