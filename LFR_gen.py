from networkx.generators.community import LFR_benchmark_graph
import networkx as nx
import time

n = 250 # number of nodes
tau1 = 3 # Power law exponent for degree distribution (>1)
tau2 = 1.5 # Power law exponent for community size distribution (>1)
mu = 0.1 # Fraction of edges to other communities ([0,1])
average_degree = 5 # Average degree of nodes in the network ([0,1])
min_degree = None # Minimum degree of nodes in the network ([0,n])
max_degree = None # Maximum degree of nodes in the network
min_community = 20 # Minimum size of communities
max_community = None # Maximum size of communities
tol = 1e-07 # Tolerance when comparing floats
max_iters = 500 # Maximum number of iterations for the random graph generator
seed = 10 # Random seed

start = time.time()
G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree, min_degree, 
                        max_degree, min_community, max_community, 
                        tol, max_iters, seed)
end = time.time()
print("Time taken:", round(end - start, 2), "s")

nx.write_edgelist(G, "LFR.txt")