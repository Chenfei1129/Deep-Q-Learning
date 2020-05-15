import numpy as np
import random

def e_greedy(actionSpace, greedyAction, e):
	actionNumber = len(actionSpace)
	probability = {action: e/actionNumber for action in actionSpace}
	probability[greedyAction] = 1 - e + e/actionNumber
	action = random.choices(actionSpace, list(probability.values()))[0]
	return action

class ChooseAction():
	def __init__(self, actionSpace, Q, phi, e_greedy):
		self.actionSpace = actionSpace
		self.phi = phi
		self.Q = Q
		self.e_greedy = e_greedy
	def __call__(self, s, e):
		Q_value = {action: self.Q(self.phi(s), action) for action in actionSpace}
		greedyAction = max(Q_value, key = Q_value.get)
		action = self.e_greedy(self.actionSpace, greedyAction, e)
		return action
'''
Gradient Descend
input: y,Q,phi,a,theta
output: new theta
Take the derivative of (y-Q(phi, a, theta))^2 with respect to theta, which is the E(r+gamma*max(Q(s', a', newTheta))
-Q(s, a, theta)*gradientQ)
'''
'''
Question: How to initialize and store information in the buffer?
          Include theta as a parameter when we need Q?
          How to take the gradient?
'''

