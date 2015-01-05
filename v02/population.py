from individual import *
from relationship import *
import copy

class Population:
	def __init__(self,PARAMETERS):
		self.population = []
		for i in range(0,PARAMETERS["society"]["starting-population"]):
			new_individual = Individual(PARAMETERS["individuals"])
			self.population.append(new_individual)
		self.year = 0

	def one_year(self):
		self.year += 1
		self.population = self.grow_all(self.population)
		relationships = self.partner_all(self.population)
		self.breed_all(relationships)
		return len(self.population)

	def grow_all(self,population):
		pop = copy.copy(population)
		for ind in pop:
			still_alive = ind.grow()
			if (not still_alive):
				population.remove(ind)
		return population

	def partner_all(self,population):
		relationships = []
		to_partner = []
		pop = copy.copy(population)
		for ind in pop:
			if (ind.relationship is None):
				if (ind.fertile):
					to_partner.append(ind)
			elif (ind.relationship.is_valid()):
				if (relationships.count(ind.relationship) == 0):
					relationships.append(ind.relationship)

		return relationships + self.new_partners(to_partner)

	def new_partners(self,to_partner):
		new_relationships = []
		sorted(to_partner, key=lambda p: p.age)
		while len(to_partner) >= 2:
			mm1 = to_partner[0]
			for mm2 in to_partner:
				if ((mm1 != mm2) and ((mm1.sex + mm2.sex) == 1)):
					new = Relationship(mm1,mm2)
					new_relationships.append(new)
					to_partner.remove(mm2)
					break
			to_partner.remove(mm1)
		return new_relationships
		

	def breed_all(self,relationships):
		for r in relationships:
			child = r.breed()
			if child:
				self.population.append(child)
