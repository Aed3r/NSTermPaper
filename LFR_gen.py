from networkx.generators.community import LFR_benchmark_graph
import networkx as nx
import time
import os

n = 50000 # number of nodes
tau1 = 3 # Power law exponent for degree distribution (>1)
tau2 = 1.5 # Power law exponent for community size distribution (>1)
mu = 0.1 # Fraction of edges to other communities ([0,1])
average_degree = 5 # Average degree of nodes in the network ([0,n])
min_degree = None # Minimum degree of nodes in the network ([0,n])
max_degree = None # Maximum degree of nodes in the network
min_community = 20 # Minimum size of communities
max_community = None # Maximum size of communities
tol = 1e-07 # Tolerance when comparing floats
max_iters = 500 # Maximum number of iterations for the random graph generator
seed = 10 # Random seed

# Set the path and file name
name = "LFR_" + str(n)
path = "./Graphs/Generated/" + name + "/"
os.makedirs(path, exist_ok = True)

#Start timer
start = time.time()

# Generate the graph
G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree, min_degree,
                        max_degree, min_community, max_community,
                        tol, max_iters, seed)

# Remove self loops
G.remove_edges_from(nx.selfloop_edges(G))

# Return total number of communities in G
communities = list({frozenset(G.nodes[v]["community"]) for v in G})
print("Number of communities:", len(communities))

# Save the communities in a list as pairs of (node, community)
community_labels = []
for i in range(len(communities)):
    for v in communities[i]:
        community_labels.append((v,i))
community_labels.sort() # might not be necessary but is nice for layout.

# End timer and display time
end = time.time()
print("Time taken:" + str(round(end - start, 2)) + "s")

# Export paramters and time
with open(path + name + "params.txt", "w") as file:
    file.write("n: " + str(n) + "\n")
    file.write("tau1: " + str(tau1) + "\n")
    file.write("tau2: " + str(tau2) + "\n")
    file.write("mu: " + str(mu) + "\n")
    file.write("average_degree: " + str(average_degree) + "\n")
    file.write("min_degree: " + str(min_degree) + "\n")
    file.write("max_degree: " + str(max_degree) + "\n")
    file.write("min_community: " + str(min_community) + "\n")
    file.write("max_community: " + str(max_community) + "\n")
    file.write("tol: " + str(tol) + "\n")
    file.write("max_iters: " + str(max_iters) + "\n")
    file.write("seed: " + str(seed) + "\n")
    file.write("Number of communities: " +  str(len(communities)) + "\n")
    file.write("Time taken: " + str(round(end - start, 2)) + "s")

# Export graph to .txt file
nx.write_edgelist(G, path + "LFR_" + str(n) + ".txt", data = False)

# Write the community labels to a file
with open(path + name + "cmty.txt", "w") as file:
    for v in community_labels:
        file.write(str(v[0]) + " " + str(v[1]) + "\n")
