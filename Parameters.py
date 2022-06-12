# File containing parameters for the different graph types and general parameters

NUM_SAMPLES = 5
SIZES = [250,1000,5000,10000,25000,50000,100000,250000,500000,1000000]

# Dense network with varying communities
dense_varying = {
"tau1" : 2.8, # Power law exponent for degree distribution ([2,3])
"tau2" : 1.8, # Power law exponent for community size distribution ([1,2])
"mu" : 0.15, # Fraction of edges to other communities ([0,1])
"average_degree" : 5, # Average degree of nodes in the network ([0,n])
"min_degree" : None, # Minimum degree of nodes in the network ([0,n])
"max_degree" : None, # Maximum degree of nodes in the network
"min_community" : 25, # Minimum size of communities
"max_community" : None, # Maximum size of communities
"tol" : 1e-07, # Tolerance when comparing floats
"max_iters" : 500 # Maximum number of iterations for the random graph generator
}

# Dense network with large communities
dense_large = {
"tau1" : 2.8, # Power law exponent for degree distribution (>1)
"tau2" : 1.2, # Power law exponent for community size distribution (>1)
"mu" : 0.15, # Fraction of edges to other communities ([0,1])
"average_degree" : 5, # Average degree of nodes in the network ([0,n])
"min_degree" : None, # Minimum degree of nodes in the network ([0,n])
"max_degree" : None, # Maximum degree of nodes in the network
"min_community" : 20, # Minimum size of communities
"max_community" : None, # Maximum size of communities
"tol" : 1e-07, # Tolerance when comparing floats
"max_iters" : 500, # Maximum number of iterations for the random graph generator
}

# Dense network with varying communities, with interconnected communities
dense_interconnected = {
"tau1" : 2.8, # Power law exponent for degree distribution (>1)
"tau2" : 1.8, # Power law exponent for community size distribution (>1)
"mu" : 0.4, # Fraction of edges to other communities ([0,1])
"average_degree" : 6, # Average degree of nodes in the network ([0,n])
"min_degree" : None, # Minimum degree of nodes in the network ([0,n])
"max_degree" : None, # Maximum degree of nodes in the network
"min_community" : 20, # Minimum size of communities
"max_community" : None, # Maximum size of communities
"tol" : 1e-07, # Tolerance when comparing floats
"max_iters" : 500 # Maximum number of iterations for the random graph generator
}

# Dense network with varying communities, with disconnected communities
dense_disconnected = {
"tau1" : 2.8, # Power law exponent for degree distribution (>1)
"tau2" : 1.8, # Power law exponent for community size distribution (>1)
"mu" : 0.05, # Fraction of edges to other communities ([0,1])
"average_degree" : 6, # Average degree of nodes in the network ([0,n])
"min_degree" : None, # Minimum degree of nodes in the network ([0,n])
"max_degree" : None, # Maximum degree of nodes in the network
"min_community" : 20, # Minimum size of communities
"max_community" : None, # Maximum size of communities
"tol" : 1e-07, # Tolerance when comparing floats
"max_iters" : 500 # Maximum number of iterations for the random graph generator
}

# Sparse network with small communities
sparse_small = {
"tau1" : 2.8, # Power law exponent for degree distribution (>1)
"tau2" : 1.9, # Power law exponent for community size distribution (>1)
"mu" : 0.15, # Fraction of edges to other communities ([0,1])
"average_degree" : 3.5, # Average degree of nodes in the network ([0,n])
"min_degree" : None, # Minimum degree of nodes in the network ([0,n])
"max_degree" : None, # Maximum degree of nodes in the network
"min_community" : 20, # Minimum size of communities
"max_community" : None, # Maximum size of communities
"tol" : 1e-07, # Tolerance when comparing floats
"max_iters" : 500 # Maximum number of iterations for the random graph generator
}

# Sparse network with varying communities
sparse_varying = {
"tau1" : 2.8, # Power law exponent for degree distribution (>1)
"tau2" : 1.7, # Power law exponent for community size distribution (>1)
"mu" : 0.15, # Fraction of edges to other communities ([0,1])
"average_degree" : 3.5, # Average degree of nodes in the network ([0,n])
"min_degree" : None, # Minimum degree of nodes in the network ([0,n])
"max_degree" : None, # Maximum degree of nodes in the network
"min_community" : 20, # Minimum size of communities
"max_community" : None, # Maximum size of communities
"tol" : 1e-07, # Tolerance when comparing floats
"max_iters" : 500 # Maximum number of iterations for the random graph generator
}

random_varying = {
"tau1" : 3.5, # Power law exponent for degree distribution (>1)
"tau2" : 2, # Power law exponent for community size distribution (>1)
"mu" : 0.5, # Fraction of edges to other communities ([0,1])
"average_degree" : 5, # Average degree of nodes in the network ([0,n])
"min_degree" : None, # Minimum degree of nodes in the network ([0,n])
"max_degree" : None, # Maximum degree of nodes in the network
"min_community" : 3, # Minimum size of communities
"max_community" : None, # Maximum size of communities
"tol" : 1e-07, # Tolerance when comparing floats
"max_iters" : 500 # Maximum number of iterations for the random graph generator
}

params = {
"dense_varying" : dense_varying,
"dense_large" : dense_large,
"dense_interconnected" : dense_interconnected,
"dense_disconnected" : dense_disconnected,
"sparse_small" : sparse_small,
"sparse_varying" : sparse_varying,
"random_varying" : random_varying,
}
