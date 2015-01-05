import randoms
class Individual:
	def __init__(self,PARAMETERS):
		#Assumptions:
		#Binary sex model (in this case, 0 and 1)
		#Refer to some form of sexual reproductive capacity
		#Penis/testicle havers versus womb havers, for instance.
		
		self.parameters = PARAMETERS
		self.age = 0
		self.fertile = False
		self.alive = True
		self.sex = randoms.random_int(0,1)

		self.fertile_age = randoms.random_int(PARAMETERS["fertility-age-min"],PARAMETERS["fertility-age-max"])
		self.fertility = randoms.random_int(PARAMETERS["fertility-min"],PARAMETERS["fertility-max"])
		self.fertility_decline = PARAMETERS["fertility-decline"]
		self.utility_child = {}
		for c in [0,1,2,3,4,"extra"]:
			self.utility_child[c] = randoms.random_int(PARAMETERS["utility-child"][c]["min"],PARAMETERS["utility-child"][c]["max"])
		self.life_expectancy = PARAMETERS["life-expectancy"]

		self.relationship = None

	def grow(self):
		#Growth/development assumptions:
		#Fertility starts off at its highest young,
		#Then decreases constantly until hitting zero.
		#Everyone dies at the same age.
		self.age += 1
		if (self.fertile == False):
			if (self.fertile_age <= self.age):
				self.fertile = True
		elif ((self.fertile == True) and (self.fertility > 0)):
			self.fertility -= self.fertility_decline
		
		if (self.age >= self.life_expectancy):
			return self.die()
		return True

	def die(self):
		self.alive = False
		return False

	def child_utility(self):
		#Assumptions related to decision to have children:
		#A person's decision to have another child is based
		#Only on how many children they've had before.
		#And not any other factors (age, economic circumstance..)
		n_children = len(self.relationship.children)
		if (n_children <= 4):
			return self.utility_child[n_children]
		else:
			return self.utility_child[4] + (n_children - 4) * self.utility_child["extra"]
