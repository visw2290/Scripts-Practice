import math
class Line:
	def __init__(self, coor1, coor2):
		self.coor1 = coor1
		self.coor2 = coor2
	def slope(self):
		# you should have use x1,y1 = self.coor1 
		return (self.coor1[1] - self.coor2[1])/(self.coor1[0] - self.coor2[0])
	def distance(self):
		return math.sqrt(((self.coor2[0]-self.coor1[0])**2) + ((self.coor2[1] - self.coor1[1])**2))
ln = Line((4,3), (8,4))
print(ln.slope())
print(ln.distance())