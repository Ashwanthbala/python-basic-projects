class PlayerCharcaters():
	#class object attribute
	membership = True
	def __init__(self,name="Anonymous",age=12):
		if age > 18:
			self.name = name
			self.age = age
	def run(self):
		print("run")

	
#instantiating the object
player1 = PlayerCharcaters("Harry Potter",22)
player2 = PlayerCharcaters("Hermoine",20)

print(player1.name)
print(player2.membership)
player2.run()