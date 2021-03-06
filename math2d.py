import math


class Vector2:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vector2(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    #print type(other)
    return Vector2(self.x - other.x, self.y - other.y)

  def __neg__(self):
    return Vector2(-self.x, -self.y)

  def rotate(self, a):
    return Vector2(
      math.cos(a)*self.x - math.sin(a)*self.y,
      math.sin(a)*self.x + math.cos(a)*self.y)

  def abs(self):
    return math.sqrt(self.x*self.x + self.y*self.y)

  def __mul__(self, other):
    if isinstance(other, Vector2):
      return self.x*other.x + self.y*other.y
    elif isinstance(other, (int, float, long)):
      return Vector2(self.x*other, self.y*other)
    else:
      return NotImplemented

  def __str__(self):
    return str(self.x) + " " + str(self.y)

class Pose2D:
  def __init__(self):
    self.translation = Vector2()
    self.rotation = 0
  def __init__(self,x,y,rotation):
    self.translation = Vector2(x,y)
    self.rotation = rotation

  def __mul__(self, other):
    return other.rotate(self.rotation) + self.translation

  def __invert__(self):
    p = Pose2D()
    p.rotation = -self.rotation
    p.translation = (Vector2() - self.translation).rotate(p.rotation)
    return p


class LineSegment:
  def __init__(self, point1X, point1Y, point2X, point2Y):
    self.point1X = point1X
    self.point1Y = point1Y
    self.point2X = point2X
    self.point2Y = point2Y
