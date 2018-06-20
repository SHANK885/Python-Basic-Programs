'''
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area. 
'''
class Circle(object):
	a = 0
	def __init__(self,r):
		self.radius = r
	def area(self):
		self.a = 3.14*self.radius**2
		return self.a

areaCircle = Circle(2)
print(areaCircle.area())
