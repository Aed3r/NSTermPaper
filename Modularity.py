from community import community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

G = nx.read_edgelist("LFR_250.txt") # Load a saved graph

# compute the best partition
partition = community_louvain.best_partition(G)

# Output number of edges
print("Number of edges:", len(G.edges()))

# Output information about the partitioning
print("Modularity:", community_louvain.modularity(partition, G))

# Output number of communities
print("Number of communities:", len(set(partition.values())))

# Output the size of each community
print("Community sizes:")
for com in set(partition.values()):
    print(com, ":", len([nodes for nodes in partition.values() if nodes == com]))

# Output the average degree of the graph
print("Average degree:", sum([len(list(G.neighbors(node))) for node in partition.keys()]) / len(G.nodes()))

# Output the average clustering coefficient of the graph
print("Average clustering coefficient:", nx.average_clustering(G))

# Output the diameter of the graph
print("Diameter:", nx.diameter(G))

# Output the average shortest path length of the graph
print("Average shortest path length:", nx.average_shortest_path_length(G))

# Output the average path length of the graph
print("Average path length:", nx.average_shortest_path_length(G))

# draw the graph
pos = nx.spring_layout(G)

# color the nodes according to their partition
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                       cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()