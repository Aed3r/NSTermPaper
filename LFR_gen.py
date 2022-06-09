import os
import networkx as nx
import time
import os
import Parameters

RUN_TESTS = False
NUM_SAMPLES = 3
seed = 2

def xorshift(seed):
    x = seed
    x ^= x << 13
    x ^= x >> 17
    x ^= x << 5
    return x


def generate_LFR(i, n, name, params, seed):

    for _ in range(i):
        # Update seed
        seed = xorshift(seed)

    print(i, n, name, seed)

    # Set the path and file name
    name = "LFR_" + name + "_" + str(n) + "_" + str(i)
    path = os.path.join("Graphs", "LFR", name)
    os.makedirs(path, exist_ok = True)

    #Start timer
    start = time.time()

    # Generate the graph
    G = nx.LFR_benchmark_graph(n, **params)

    # Remove self loops
    #G.remove_edges_from(nx.selfloop_edges(G))

    # End timer and display time
    end = time.time()
    print("Time taken:" + str(round(end - start, 2)) + "s")

    # Return total number of communities in G
    communities = list({frozenset(G.nodes[v]["community"]) for v in G})
    print("Number of communities:", len(communities))

    # Save the communities in a list as pairs of (node, community)
    community_labels = []
    for i in range(len(communities)):
        for v in communities[i]:
            community_labels.append((v,i))
    community_labels.sort() # might not be necessary but is nice for layout.

    # Export paramters and time
    with open(os.path.join(path, name + "_params.txt"), "w") as file:
        file.write("n: " + str(n) + "\n")
        for key, value in params.items():
            if key != "seed":
                file.write(key + str(value) + "\n")
        file.write("seed: " + str(seed) + "\n")
        file.write("Number of communities: " +  str(len(communities)) + "\n")
        file.write("Time taken: " + str(round(end - start, 2)) + "s")

    # Export graph to .txt file
    nx.write_edgelist(G, os.path.join(path, name + ".txt"), data = False)

    # Write the community labels to a file
    with open(os.path.join(path, name + "_labels.txt"), "w") as file:
        for v in community_labels:
            file.write(str(v[0]) + " " + str(v[1]) + "\n")

    # Write the communities to each line
    with open(os.path.join(path, name + "_cmty.txt"), "w") as file:
        for community in communities:
            for node in community:
                file.write(str(node) + " ")
            file.write("\n")

    # Automatically run tests
    if RUN_TESTS:
        os.system("python Run_test.py " + name)

    print()

sizes = [250]

for name, params in Parameters.params.items():
    for n in sizes:
        for i in range(NUM_SAMPLES):
            generate_LFR(i+1, n, name, params, seed)
