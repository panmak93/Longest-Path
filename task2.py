"""
Name: Cheuk Pan, Mak
Compsci 220
Assignment 3
"""

import networkx as nx
import collections

class Assignment3:
	
	
	def longest_path(G, v):
		stack = nx.topological_sort(G)
		visited = []
		dist = dict()
		for v in G.nodes():
			dist[v] = 0
			
		for v in stack:
			if (len(G.predecessors(v)) != 0) and (v != 0):
				max_dist_u = 0
				for u in G.predecessors(v):
					if dist[u] != 0:
						max_dist_u = max(dist[u], max_dist_u)
						dist[v] = max_dist_u + 1
			if 0 in G.predecessors(v):
				dist[v] = max(1, dist[v])
		
		maxdist = 0
		for key in dist:
			maxdist = max(maxdist, dist[key])
		return maxdist
			 

		
	output = ""
	while(True):
		line = input()
		if (line == "0") or (line == "\n") or (line == ""):
			break
		else:
			order = int(line)
			adj_dict = dict()
			counter = 0 
			while counter < order:
				adjacents = input()
				if ((adjacents == "\n") or (adjacents == "") or (adjacents == " ")):
					adj_dict[counter] = []
				else:
					adjacents.rstrip("\n")
					adjacent_list = adjacents.split()
					for adj in adjacent_list:
						adj = int(adj)
						if adj >= order:
							raise IndexError
						else:
							if counter in adj_dict:
								adj_dict[counter] += [adj]
							else:
								adj_dict[counter] = [adj]
				counter+=1
			G = nx.DiGraph(weight = 1)
			G.add_nodes_from(adj_dict.keys())
			for outgoing_v in adj_dict:
				for ingoing_v in adj_dict[outgoing_v]:
					G.add_edge(outgoing_v, ingoing_v)
			output = output + str(longest_path(G, 0)) + "\n"
		
	print(output.rstrip('\n'))
	
	
	