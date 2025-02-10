class Square :
  def __init__(self):
    self.__side = 10

  def area(self) :
    print("Side :", self.__side)
    print("My area is :", self.__side**2)

obj = Square()

obj.__side = 15
obj.area()