import networkx as nx
import matplotlib.pyplot as plt
import os
import sys

LOCATION = os.path.join("Graphs", "Real", "EU-email", "email-Eu-core.txt") # Location of the network to be displayed

def display_graph(location):
    G = nx.read_edgelist(location)

    pos = nx.spring_layout(G, k=2)
    nx.draw_networkx(G, pos=pos, node_size=0, edge_color="#333333", alpha=0.5, with_labels=False)
    plt.show()

if __name__ == "__main__":
    display_graph(LOCATION)
    sys.exit()