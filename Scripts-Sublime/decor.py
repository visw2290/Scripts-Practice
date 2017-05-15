def deco(funn):
	def wrapp():
		print('You are checking decorator')
		funn()
		print('Decorator is checked')
	return wrapp()
#@deco
def oldo():
	print('This is a test for decorator')
oldo = deco(oldo)
oldo