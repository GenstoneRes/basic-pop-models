from population import *

import statistics
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


PARAMETERS = { 
	"individuals" : {
		"fertility-age-min" : 16,
		"fertility-age-max" : 18,
		"fertility-min" : 0,
		"fertility-max" : 1023,
		"fertility-decline" : 30,
		"utility-child" : {
			0 : {
				"min" : -1,
				"max" : 35,
			},
			1 : {
				"min" : -2,
				"max" : 35,
			},
			2 : {
				"min" : -15,
				"max" : 15,
			},
			3 : {
				"min" : -20,
				"max" : 5,
			},
			4 : {
				"min" : -35,
				"max" : 10,
			},
			"extra" : {
				"min" : -10,
				"max" : 5,
			}
		},
		"life-expectancy" : 80,
	},
	"society" : {
		"starting-population" : 100,
		"starting-age-min" : 18,
		"starting-age-max" : 18,
	}
}

n_gens = 300
n_games = 100

outcomes = [0,0,0]
for g in range(0,n_games):
	print("Running game {}".format(g))
	pop = Population(PARAMETERS)

	pop_values = []
	for i in range(0,n_gens):
		val = pop.one_year()
		pop_values.append(val)
		if (val == 0):
			outcomes[1] += 1
			break
		elif (val > 1000):
			outcomes[2] += 1
			break
		if (i + 1 == n_gens):
			print(pop_values)
			outcomes[0] += 1

print("N_gens: {}. Attempts: {}".format(n_gens,sum(outcomes)))
print("Success: {}. Collapse: {}. Expansion: {}.".format(outcomes[0],outcomes[1],outcomes[2]))

#print(pop_values)

#bar = plt.bar([a for a in range(0,len(pop_values))],pop_values,1,color="blue")
#plt.show()
