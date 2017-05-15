class StackOverflowUser:

    def __init__(self, name, userid, rep): 
        self.name = name
        self.userid = userid
        self.rep = rep

    @classmethod
    def from_input(cls):
        return cls(
            input('Name: '),
            int(input('User ID: ')), 
            int(input('Reputation: ')),
        )
users = {}
for i in range(2):  # create 10 users
    user = StackOverflowUser.from_input()  # from user input
    users[user.userid] = user  # and store them in the dictionary
print(users.items())