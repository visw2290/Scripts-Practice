
class EmaVer:
	email_list=[]
	def ema(self,email):
		self.email = email
		if '@' in self.email:
			if self.email not in EmaVer.email_list:
				EmaVer.email_list.append(email)
			else:
				return 'Email ID already exists'
		else:
			return 'Enter a valid email address'
em1 = EmaVer()
print(em1.ema('visw@gmail.com'))
print(em1.ema('visw@gmail.com'))
print(em1.ema('oiu@hjk.com'))
print(em1.ema('lkkll'))
print(em1.email_list)
em2 = EmaVer()
print(em2.ema('viswa@gmail.com'))
print(em2.ema('viswa@gmail.com'))
print(em2.ema('oiuk@hjk.com'))
print(em2.ema('lkkll'))
print(em2.email_list)
