import numpy as np
import pandas as pd
import seaborn
from matplotlib.colors import ListedColormap

class GridWorld:
	def __init__(self, gamma = 1.0, theta = 0.5):
		self.actions = ("U", "D", "L", "R") 
		self.states = np.arange(1, 15)
		self.transitions = pd.read_csv("gridworld.txt", header = None, sep = "\t").values
		self.gamma = gamma
		self.theta = theta
		
	def state_transition(self, state, action):
		next_state, reward = None, None
		for tr in self.transitions:
			if tr[0] == state and tr[1] == action:
				next_state = tr[2]
				reward = tr[3]
		return next_state, reward

	def show_environment(self):
		all_states = np.concatenate(([0], self.states, [0])).reshape(4,4)
		colors = []
		# colors = ["#ffffff"]
		for i in range(len(self.states) + 1):
			if i == 0:
				colors.append("#c4c4c4")
			else:
				colors.append("#ffffff")

		cmap = ListedColormap(seaborn.color_palette(colors).as_hex())
		ax = seaborn.heatmap(all_states, cmap = cmap, \
			annot = True, linecolor = "#282828", linewidths = 0.2, \
			cbar = False)