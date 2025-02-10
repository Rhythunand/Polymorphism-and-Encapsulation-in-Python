class square :
  def __init__(self,side):
    self.side = side

  def area(self) :
    print("My area is :", self.side**2)

class circle :
  def __init__(self,radius):
    self.radius = radius

  def area(self) :
    print("My area is :", 3.4*self.radius*self.radius)

ocircle = circle(5)
osquare = square(5)

for shape in (osquare, ocircle) :
  shape.area()