from usererror import CheckError
class Errort(CheckError):
	i = 20
	try:
		if i < 30:
			raise CheckError
	except CheckError:
		print('Your test has passed')