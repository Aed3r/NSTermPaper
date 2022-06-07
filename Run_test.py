#import Community.community as louvain
#import Community.modularity
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx
import time
from time import sleep
import sys
import Modularity.community_louvain as modularity
from infomap import Infomap

PRINT_INFO = False
DRAW_GRAPH = False
FILE = "LFR_250.txt"
MEASURE = "MODULARITY" # "MODULARITY" / "MAPEQUATION" / "SIGCLUST" / "ALL"

if len(len(sys.argv)) > 1:
    FILE = sys.argv[1]
    MEASURE = "ALL"

G = nx.read_edgelist(FILE) # Load the saved graph

# compute the best partition

if MEASURE == "MODULARITY" or MEASURE == "ALL":
    start = time.time()
    partition = modularity.best_partition(G)
    end = time.time()
    # Running time
    print("Modularity running time:", round(end - start, 2), "s")

if MEASURE == "MAPEQUATION" or MEASURE == "ALL":
    start = time.time()
    
    im = Infomap("--two-level")
    for node in G.nodes():
        im.add_link(node[0], node[1])
    im.run()

    end = time.time()
    # Running time
    print("MAPEQUATION running time:", round(end - start, 2), "s")

if PRINT_INFO:
    # Output number of edges
    print("Number of edges:", len(G.edges()))

    # Output information about the partitioning
    print("Modularity:", modularity.modularity(partition, G))

    # Output number of communities
    print("Number of communities:", len(set(partition.values())))

    # Output the size of each community
    print("Community sizes:\n[", end="")
    for com in set(partition.values()):
        print(com, ":", len([nodes for nodes in partition.values() if nodes == com]), end=", ")

    # Output the average degree of the graph
    print("Average degree:", sum([len(list(G.neighbors(node))) for node in partition.keys()]) / len(G.nodes()))

    # Output the average clustering coefficient of the graph
    print("Average clustering coefficient:", nx.average_clustering(G))

    # Output the diameter of the graph
    try:
        print("Diameter:", nx.diameter(G))
    except:
        print("Diameter:", "N/A")

    # Output the average shortest path length of the graph
    try:
        print("Average shortest path length:", nx.average_shortest_path_length(G))
    except:
        print("Average shortest path length:", "N/A")

if DRAW_GRAPH:
    # draw the graph
    pos = nx.spring_layout(G)

    # color the nodes according to their partition
    cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                        cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()