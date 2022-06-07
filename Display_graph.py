import networkx as nx
import matplotlib.pyplot as plt

path = "./Graphs/EU-email/email-Eu-core.txt"

G = nx.read_edgelist("LFR_1000.txt")
#G = nx.read_edgelist(path)

pos = nx.spring_layout(G, k=2)
nx.draw_networkx(G, pos=pos, node_size=0, edge_color="#333333", alpha=0.5, with_labels=False)
plt.show()
