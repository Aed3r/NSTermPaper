import os
import networkx as nx
import time

n = 500 # number of nodes
tau1 = 3 # Power law exponent for degree distribution (>1)
tau2 = 1.5 # Power law exponent for community size distribution (>1)
mu = 0.1 # Fraction of edges to other communities ([0,1])
average_degree = 5 # Average degree of nodes in the network ([0,n])
min_degree = None # Minimum degree of nodes in the network ([0,n])
max_degree = None # Maximum degree of nodes in the network
min_community = 20 # Minimum size of communities
max_community = 500 # Maximum size of communities
tol = 1e-07 # Tolerance when comparing floats
max_iters = 1000 # Maximum number of iterations for the random graph generator
seed = 10 # Random seed

#Start timer
start = time.time()

# Generate the graph
G = nx.LFR_benchmark_graph(n, tau1, tau2, mu, average_degree, min_degree,
                        max_degree, min_community, max_community, 
                        tol, max_iters, seed)

# Remove self loops
G.remove_edges_from(nx.selfloop_edges(G))

# End timer and display time
end = time.time()
print("Time taken:", round(end - start, 2), "s")

# Return total number of communities in G
communities = {frozenset(G.nodes[v]["community"]) for v in G}
print("Number of communities:", len(communities))

# Export graph to .txt file
nx.write_edgelist(G, "LFR_" + str(n) + ".txt")

# Automatically run tests
os.system("python3 Run_test.py LFR_" + str(n) + ".txt")