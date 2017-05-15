class Error(Exception):
	pass
class CheckError(Error):
	pass
if __name__ == '__main__':
	i = 10
	try:
		if i < 11:
			raise CheckError
	except CheckError:
		print('This is the user-defined check error i created')