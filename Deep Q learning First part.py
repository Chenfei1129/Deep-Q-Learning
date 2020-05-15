import numpy as np
import random

def e_greedy(actionSpace, greedyAction, e):
	actionNumber = len(actionSpace)
	probability = {action: e/actionNumber for action in actionSpace}
	probability[greedyAction] = 1 - e + e/actionNumber
	action = random.choices(actionSpace, list(probability.values()))[0]
	return action

class chooseAction():
	def __init__(self, actionSpace, Q, phi, e_greedy):
		self.actionSpace = actionSpace
		self.phi = phi
		self.Q = Q
		self.e_greedy = e_greedy
	def __call__(self, s, e):
		greedyAction = max(self.Q(self.phi(s), action) for action in actionSpace)
		action = self.e_greedy(self.actionSpace, greedyAction, e)
		return action



