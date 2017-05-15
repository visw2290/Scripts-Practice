import shelve

shelveFile = shelve.open('c:\\BU Chats\\myshelve')
shelveFile['names'] = ('viswa', 'shiva', 'binchoo', 'pavan')
shelveFile.close()

shelveFile = shelve.open('c:\\Bu Chats\\myshelve')
print(list(shelveFile.keys()))
print(list(shelveFile.values()))

