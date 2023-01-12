class SuperClass:
  def __init__(self):
    # Protected member
    self._num1 = 100
    # Private member
    self.__num2 = 200
  
  def display(self):
    print(self._num1)
    print(self.__num2)

class SubClass(SuperClass):
  def show(self):
    print(self._num1)
    print(self.__num2)

sup_obj = SuperClass()
sub_obj = SubClass()

sup_obj.display()
sub_obj.show()