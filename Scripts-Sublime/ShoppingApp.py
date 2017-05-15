import datetime
class ShopApp:
	userDetails = []
	messageDetails = []
	defmessage = 'Thanks you {} for purchasing things from XYZ store.Your total bill is {} purchased at {}'
	def adduser(self,name,cost):
		name = name[0].upper() + name[1:].lower()
		cost = 'Rs ' + str(cost)
		dict1 = {'name' : name,'cost':cost}
		dt = datetime.datetime.now()
		dtformat = dt.strftime('%d-%m-%y %H:%M:%S')
		dict1['date'] = dtformat
		ShopApp.userDetails.append(dict1)
	def getdetails(self):
		return self.userDetails
	def messageuser(self):
		for msg in self.getdetails():
			nm = msg['name']
			cs = msg['cost']
			tm = msg['date']
			new_message = self.defmessage.format(nm,cs,tm)
			self.messageDetails.append(new_message)
		return self.messageDetails
user1 = ShopApp()
user1.adduser('viswa', 1700)
user1.adduser('shiva', 2500)
print(user1.getdetails())
print(user1.userDetails)
print(user1.messageuser())
