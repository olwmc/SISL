class Thing:
	def __init__(self, name, age, fav_thing):
		self.name = name
		self.age = age
		self.fav_thing = fav_thing
	
	def getName(self):
		return self.name
		
	def getAge(self):
		return self.age

	def getFav(self):
		return self.fav_thing

thing = Thing("Name", 13, "sports")

# Testing thing.getName()
if (thing.getName() == 'Name'):
	print("PASS")
else:
	print("FAIL thing.getName() !== 'Name'")
	exit(0)

# Testing thing.getAge()
if (thing.getAge() >= 13):
	print("PASS")
else:
	print("FAIL thing.getAge() !>= 13")
	exit(0)

# Testing thing.getFav()
if (thing.getFav() == 'Sports'):
	print("PASS")
else:
	print("FAIL thing.getFav() !== 'Sports'")
	exit(0)

