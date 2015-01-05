from individual import *
import randoms
class Relationship:
	def __init__(self, person_one, person_two):
		self.p1 = person_one
		self.p2 = person_two
		self.p1.relationship = self
		self.p2.relationship = self
		self.children = []
	
	def breed(self):
		utility = self.get_utility()
		if (utility > 0):
			fertility = self.get_fertility()
			if randoms.binary_random_decision(fertility,True,False):
				child = Individual(self.get_child_parameters())
				self.children.append(child)
				return child
		return False

	def get_child_parameters(self):
		return self.p1.parameters

	def is_valid(self):
		return self.p1.alive and self.p2.alive

	def get_utility(self):
		return self.p1.child_utility() + self.p2.child_utility()
	
	def get_fertility(self):
		return self.p1.fertility + self.p2.fertility
