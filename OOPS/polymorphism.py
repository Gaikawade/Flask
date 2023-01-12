# Programs to demonstrate Polymorphism

# Method Overloading

class Overloading:
  # loading function with 2 arguments
  def loading(self, x=None, y=None):
    # this block will run if we call the loading function with no arguments
    if x==None and y==None:
      print("Am executed by calling loading method without arguments")
      return f"I have no friends"
    # this block will run if we call the loading function with 1 argument
    elif x!=None and y==None:
      print("Am executed by calling loading method with 1 argument")
      return f"I have a friend and his name is {x}"
    # this block will run if we call the loading function with 2 arguments
    else:
      print("Am executed by calling loading method with 2 arguments")
      return f"I have two friends and their names are {x} and {y}"

# Creating an instance of OverLoading Class
ol = Overloading()
# calling the loading function with 0 arguments
print(ol.loading())
# calling the loading function with 1 argument
print(ol.loading('Bob'))
# calling the loading function with 2 arguments
print(ol.loading('Bob', 'Rowlin'))


# Method Overriding

# Method overriding occurs when a subclass has a method with the same name as a method in its superclass

class A:
  def riding(self):
    print("Hello")

class B(A):
  def riding(self):
    print("Hi")
  def check(self):
    print("Bye")

# b = B()
# b.riding()
