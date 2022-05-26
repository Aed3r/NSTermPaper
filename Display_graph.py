import networkx as nx
import matplotlib.pyplot as plt

path = "./Graphs/EU-email/email-Eu-core.txt"

#G1 = nx.read_edgelist("LFR.txt")
G2 = nx.read_edgelist(path)

nx.draw(G2)
plt.show()
