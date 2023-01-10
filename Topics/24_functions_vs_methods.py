# -- Functions vs Methods --

# A Function that lives insdie a class is called a Method.

# So, methods are functions, but not all functions are methods.

# -- Function --

def average(sequence):
  return sum(sequence) / len(sequence)


# -- Method --

class Student:
  def __init__(self):   # Method (magic method)
    self.name = "Rahul"
    self.grades = (79, 90, 95, 45)
    
  def average(self):    # Method
    return sum(self.grades) / len(self.grades)