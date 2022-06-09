import os
import time

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

import Modularity.community_louvain as modularity
from infomap import Infomap

import Scoring

PRINT_INFO = True
DRAW_GRAPH = False
FILES = [ "LFR_" + str(n) for n in [250,1000,5000,10000,50000,75000,100000]]
MEASURE = "ALL" # "MODULARITY" / "MAPEQUATION" / "SIGCLUST" / "ALL"
SAVE_RESULTS = True
RESULTS_FILE = "./Results.csv"

# if len(sys.argv) > 1:
#     FILE = sys.argv[1]
#     LOCATION = os.path.join("Graphs", "LFR", FILE)
#     MEASURE = "ALL"

for FILE in FILES:
    LOCATION = os.path.join("Graphs", "LFR", FILE)

    G = nx.read_edgelist(path = os.path.join(LOCATION, FILE + ".txt"), nodetype = int) # Load the saved graph

    SAVEPATH = os.path.join("Results", FILE + "_" + time.strftime("%d_%H-%M-%S"))
    os.makedirs(SAVEPATH, exist_ok = True)

    # compute the best partition

    if MEASURE == "MODULARITY" or MEASURE == "ALL":
        start = time.time()
        mod_partition = modularity.best_partition(G)
        end = time.time()
        # Running time
        mod_time = round(end - start, 2)
        print("Modularity running time:", mod_time, "s")

        # Write results to file
        with open(os.path.join(SAVEPATH, FILE + "_mod.txt"), "a") as f:
            for node, com in mod_partition.items():
                f.write(str(node) + " " + str(com) + "\n")

        # Compare community labels
        groundTruth = Scoring.read_partition(os.path.join(LOCATION, FILE + "labels.txt"))
        mod_partition = Scoring.read_partition(os.path.join(SAVEPATH, FILE + "_mod.txt"))
        #partition = Scoring.preprocess_partitions(partition)

        mod_res = Scoring.compare_communities(groundTruth, mod_partition)
        print("Modularity NMI: ", mod_res)


    if MEASURE == "MAPEQUATION" or MEASURE == "ALL":
        start = time.time()

        im = Infomap("--silent")
        for edge in G.edges():
            im.add_link(int(edge[0]), int(edge[1]))
        im.run()

        end = time.time()
        # Running time
        info_time = round(end - start, 2)
        print("MAPEQUATION running time:", info_time, "s")
        print(f"Found {im.num_top_modules} modules with codelength: {im.codelength}")

        # Write results to file
        with open(os.path.join(SAVEPATH, FILE + "_map.txt"), "a") as f:
            for node in im.tree:
                if node.is_leaf:
                    f.write(str(node.node_id) + " " + str(node.module_id) + "\n")

        # Compare community labels
        info_partition = Scoring.read_partition(os.path.join(SAVEPATH, FILE + "_map.txt"))
        #partition = Scoring.preprocess_partitions(partition)

        info_res = Scoring.compare_communities(groundTruth, info_partition)
        print("MapEquation NMI: ", info_res)

    if SAVE_RESULTS and MEASURE == "ALL":
        with open(RESULTS_FILE, "a") as f:
            f.write(FILE + ", ")
            f.write(time.strftime("%d_%H-%M-%S") + ", ")
            f.write(str(len(set(groundTruth.values()))) + ", " )
            f.write(str(len(set(mod_partition.values()))) + ", " )
            f.write(str(len(set(info_partition.values()))) + ", " )
            f.write(str(mod_res) + ", ")
            f.write(str(info_res) + ", ")
            f.write(str(mod_time) + ", ")
            f.write(str(info_time) + "\n")


    if PRINT_INFO:
        # Output number of edges
        print("Number of nodes:", len(G.nodes()))

        # Output number of edges
        print("Number of edges:", len(G.edges()))

        # Output information about the partitioning
        print("Modularity:", modularity.modularity(groundTruth, G))

        # Output number of communities
        print("Number of communities:", len(set(groundTruth.values())))

        # Output the size of each community
        print("Community sizes:\n[", end="")
        for com in set(groundTruth.values()):
            print(com, ":", len([nodes for nodes in groundTruth.values() if nodes == com]), end=", ")
        print("]")

        # Output the average degree of the graph
        print("Average degree:", sum([k[1] for k in G.degree]) / len(G.nodes()))

        # Output the average clustering coefficient of the graph
        print("Average clustering coefficient:", nx.average_clustering(G))

        # Output the diameter of the graph
        # try:
        #     print("Diameter:", nx.diameter(G))
        # except:
        #     print("Diameter:", "N/A")
        #
        # # Output the average shortest path length of the graph
        # try:
        #     print("Average shortest path length:", nx.average_shortest_path_length(G))
        # except:
        #     print("Average shortest path length:", "N/A")

        print()

    if DRAW_GRAPH:
        # draw the graph
        pos = nx.spring_layout(G)

        # color the nodes according to their partition
        cmap = cm.get_cmap('viridis', max(groundTruth.values()) + 1)
        nx.draw_networkx_nodes(G, pos, groundTruth.keys(), node_size=40,
                            cmap=cmap, node_color=list(groundTruth.values()))
        nx.draw_networkx_edges(G, pos, alpha=0.5)
        plt.show()
