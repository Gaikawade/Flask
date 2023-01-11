''' 
 A Python program to demonstrate inheritance
 Cube class inherits the Square class
 Performing the square and cube operation
'''

  # Square calss is used to calculate the square of the number
class Square:
  # Constructor
  def __init__(self, num):
    self.num = num
  
  # Function to calculate the square
  def getSquare(self):
    # returning the square value
    return self.num ** 2

# Cube class which is a subclass of Square Class
class Cube(Square):
  # Constructor
  def __init__(self, num):
    # Calling constructor of Square Class
    # Instead of super(), we can use the Class name as well
    Square.__init__(self, num)
  
  def getCube(self):
    # Multiplying the sqrt value from self with the num to get the cube value
    return Square.getSquare(self) * self.num


number = int(input("Enter a number: "))
# Creating an instance of Cube Class object
obj = Cube(number)
# Printing the cube value by calling getCube() method
print(f"The Cube of {number} is {obj.getCube()}")
# Printing the square value by calling getSquare() method
print(f"The Square of {number} is {obj.getSquare()}")
