import os
import sys
import time

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

import Modularity.community_louvain as modularity
from infomap import Infomap

from Parameters import *
import Parameters
import Scoring

PRINT_INFO = False
DRAW_GRAPH = False
MEASURE = "ALL" # "MODULARITY" / "MAPEQUATION" / "SIGCLUST" / "ALL"
SAVE_RESULTS = True
VERBOSE = True
TESTLFR = False # LFR graphs get loaded according to the parameters in Parameters.py

# To set when testing separate networks
LOCATION = os.path.join("Graphs", "Real", "EU-email")
FILE = "email-Eu-core"
LABELSFILE = "email-Eu-corelabels.txt"

def run_tests(size, name, i):
    if TESTLFR:
        location = os.path.join("Graphs", "LFR", name)
        filename = "LFR_" + name + "_" + str(size) + "_" + str(i)
    else:
        location = LOCATION
        filename = FILE

    G = nx.read_edgelist(path = os.path.join(location, filename + ".txt"), nodetype = int) # Load the saved graph

    SAVEPATH = "Results"
    SAVEPATHCOMS = os.path.join("Found_communities", name)
    if SAVE_RESULTS:
        os.makedirs(SAVEPATH, exist_ok = True)
        os.makedirs(SAVEPATHCOMS, exist_ok = True)
        resultsFile = os.path.join(SAVEPATH, name + ".csv")
    
        # Verify if results file exists
        if not os.path.isfile(resultsFile):
            with open(resultsFile, "a") as f:
                f.write("Graph, Time, # true communities, # communities found by modularity, # communities found by MapEquation, Modularity NMI, MapEquation NMI, Modularity time (s), MapEquation time (s)\n")

    print ("File ", filename)

    # Get ground truth community labels
    if TESTLFR:
        groundTruth = Scoring.read_partition(os.path.join(location, filename + "_labels.txt"))
    else:
        groundTruth = Scoring.parse_partition(os.path.join(location, LABELSFILE))

    # compute the best partition

    if MEASURE == "MODULARITY" or MEASURE == "ALL":
        start = time.time()
        mod_partition = modularity.best_partition(G)
        end = time.time()
        # Running time
        mod_time = round(end - start, 2)
        if VERBOSE:
            print("Modularity running time:", mod_time, "s")

        # Write results to file
        if SAVE_RESULTS:
            with open(os.path.join(SAVEPATHCOMS, filename + "_mod.txt"), "a") as f:
                for node, com in mod_partition.items():
                    f.write(str(node) + " " + str(com) + "\n")

        items = []
        for node, com in mod_partition.items():
            items.append((node, com))
        mod_partition = dict(items)

        # Compare community labels
        #mod_partition = Scoring.read_partition(os.path.join(SAVEPATH, FILE + "_" + str(i) + "_mod.txt"))

        mod_res = Scoring.compare_communities(groundTruth, mod_partition)
        if VERBOSE:
            print("Modularity NMI: ", mod_res)


    if MEASURE == "MAPEQUATION" or MEASURE == "ALL":
        start = time.time()

        im = Infomap("--silent -2")
        for edge in G.edges():
            im.add_link(int(edge[0]), int(edge[1]))
        im.run()

        end = time.time()
        # Running time
        info_time = round(end - start, 2)
        if VERBOSE:
            print("MAPEQUATION running time:", info_time, "s")
            print(f"Found {im.num_top_modules} modules with codelength: {im.codelength}")

        # Write results to file
        if SAVE_RESULTS:
            with open(os.path.join(SAVEPATHCOMS, filename + "_map.txt"), "a") as f:
                for node in im.tree:
                    if node.is_leaf:
                        f.write(str(node.node_id) + " " + str(node.module_id) + "\n")

        items = []
        for node in im.tree:
            if node.is_leaf:
                items.append((node.node_id, node.module_id))
        info_partition = dict(items)

        info_res = Scoring.compare_communities(groundTruth, info_partition)
        if VERBOSE:
            print("MapEquation NMI: ", info_res)

    if SAVE_RESULTS and MEASURE == "ALL":
        with open(resultsFile, "a") as f:
            f.write("LFR_" + str(size) + "_" + str(i) + ", ")
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

if TESTLFR:
    for size in SIZES:
        for name, _ in Parameters.params.items():
            for i in range(1, NUM_SAMPLES+1):
                run_tests(size, name, i)
else:
    run_tests(None, FILE, None)