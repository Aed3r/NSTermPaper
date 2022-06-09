from sklearn.metrics.cluster import normalized_mutual_info_score

# `normalized_mutual_info_score` takes two arrays, each partitioning the same data
# and computes their normalized mutual information, independent of labels
example1 = normalized_mutual_info_score([0, 0, 1, 1], [0, 0, 1, 1])
example2 = normalized_mutual_info_score([0, 0, 1, 1], [1, 1, 0, 0])
example3 = normalized_mutual_info_score([1, 1, 0, 0], [1, 2, 3, 4])

# Takes a file path of a file containing
# lines with all the nodes in the same community
# and returns a dictionary storing the partition
def parse_partition(path):
    communities = []
    # Read all the lines of the file, each line is a community
    f = open(path, 'r')
    for line in f:
        ints = line.split()
        ints = list(map(int, ints))
        communities.append(ints)
    f.close()
    communities.sort(key = len)


    # Initialize a dictionary with a far greater number of nodes. This will be trimmed by compare_communities later.
    max_num_of_nodes = sum([len(x) for x in communities])
    partition = dict(zip(range(1,max_num_of_nodes), range(1,max_num_of_nodes)))


    # Iterate through the list backwards to start with the largest communities and end with the smallest
    # If a node is in multiple communities, it will only register the last (smallest) community.
    # If a node is not in a community, it gets its own node id as community label
    for i in range(len(communities)-1, -1, -1):
        for node in communities[i]:
            partition[node] = i + max_num_of_nodes

    return partition

# Takes a file path of a file containing
# pairs of a node label and which partition it belongs to
# and returns a dictionary storing the partition
def read_partition(path):
    items = []
    f = open(path, 'r')
    for line in f:
        ints = line.split()
        node   = int(ints[0])
        community = int(ints[1])
        items.append((node, community))

    partition = dict(items)

    return partition

# takes a dictionary and returns their values in a deterministic order
# determined by sorting the keys
def preprocess_partitions(ground_truth_partition, found_partition):
    # find which keys (nodes) are missing and give them each their own community
    missing_keys = set(ground_truth_partition.keys()) - set(found_partition.keys())
    missing_items = [(key, key + len(ground_truth_partition)) for key in missing_keys]
    found_partition.update(missing_items)

    # convert the partition to a list and sort by key
    sorted_ground_truth_partition = list(ground_truth_partition.items())
    sorted_ground_truth_partition.sort(key = lambda x : x[0])
    sorted_found_partition = list(found_partition.items())
    sorted_found_partition.sort(key = lambda x : x[0])
    # only keep the communities
    ground_truth_communities = [x[1] for x in sorted_ground_truth_partition]
    found_communities = [x[1] for x in sorted_found_partition]

    return ground_truth_communities, found_communities

# takes two dictionaries, where the nodes are keys
# and the values are the label of the partition they belong to,
# and returns their normalized mutual information, 0 < NMI < 1
def compare_communities(ground_truth_partition, found_partition):
    ground_truth_communities, found_communities = preprocess_partitions(ground_truth_partition, found_partition)
    return normalized_mutual_info_score(ground_truth_communities, found_communities)
