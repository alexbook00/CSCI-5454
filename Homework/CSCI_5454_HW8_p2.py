import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

# Part a
G = nx.Graph()

U = range(10)
V = range(10,20)
E = []

G.add_nodes_from(U, bipartite=0)
G.add_nodes_from(V, bipartite=1)

while not nx.is_connected(G):
	U_vertex = np.random.randint(0, 10)
	V_vertex = np.random.randint(10, 20)
	G.add_edge(U_vertex, V_vertex)

# Part b
counter_in_U = {}
for i in range(1, 21):
	counter_in_U[i] = 0

for walk in range(1000):
	if np.random.rand() < .25:
		start = np.random.randint(0, 10)
	else:
		start = np.random.randint(10, 20)

	curr = start
	for curr_step in range(1, 21):
		if curr in range(0, 10):
			counter_in_U[curr_step] += 1
		neighbors = [n for n in G.neighbors(curr)]
		curr = np.random.choice(neighbors)

plt.plot(range(1, 21), np.array(list(counter_in_U.values()))/1000, 'o-')
plt.xticks(range(1, 21))
plt.xlabel('Step number')
plt.ylabel('Fraction of walks with step in set U')
plt.show()

# Part c
counter_in_U = {}
for i in range(1, 21):
	counter_in_U[i] = 0

for walk in range(1000):
	if np.random.rand() < .25:
		start = np.random.randint(0, 10)
	else:
		start = np.random.randint(10, 20)

	curr = start
	for curr_step in range(1, 21):
		if curr in range(0, 10):
			counter_in_U[curr_step] += 1
		if np.random.rand() < .25:
			neighbors = [n for n in G.neighbors(curr)]
			curr = np.random.choice(neighbors)

plt.plot(range(1, 21), np.array(list(counter_in_U.values()))/1000, 'o-')
plt.xticks(range(1, 21))
plt.xlabel('Step number')
plt.ylabel('Fraction of walks with step in set U')
plt.show()

# Part d
for walk_length in [10, 20, 100]:
	counter_final = {}
	for i in range(0, 20):
		counter_final[i] = 0

	for walk in range(1000):
		if np.random.rand() < .25:
			start = np.random.randint(0, 10)
		else:
			start = np.random.randint(10, 20)

		curr = start
		for curr_step in range(1, walk_length+1):
			if np.random.rand() < .25:
				neighbors = [n for n in G.neighbors(curr)]
				curr = np.random.choice(neighbors)

		counter_final[curr] += 1

	plt.bar(range(20), np.array(list(counter_final.values()))/1000, align='center')
	plt.xticks(range(20))
	plt.title(f'Walk length {walk_length}')
	plt.xlabel('Vertices')
	plt.ylabel('Fraction of walks ending on each vertex')
	plt.show()
