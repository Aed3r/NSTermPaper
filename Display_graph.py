import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("LFR.txt")

nx.draw(G)
plt.show()