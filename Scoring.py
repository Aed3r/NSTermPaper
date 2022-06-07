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
    items = []
    community = 0
    f = open(path, 'r')

    for line in f:
        ints = line.split()
        for i in ints:
            node = int(i)
            items.append((node, community))
        community += 1
    # if a node is in multiple communities, dict() will only register the last community.
    partition = dict(items)
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
def preprocess_partitions(partition):
    # convert the partition to a list and sort by key
    sorted_partition = list(partition.items())
    sorted_partition.sort(key = lambda x : x[0])
    # only keep the communities
    communities = [x[1] for x in sorted_partition]

    return communities

# takes two dictionaries, where the nodes are keys
# and the values are the label of the partition they belong to,
# and returns their normalized mutual information, 0 < NMI < 1
def compare_communities(partition1, partition2):
    communities1 = preprocess_partitions(partition1)
    communities2 = preprocess_partitions(partition2)
    return normalized_mutual_info_score(communities1, communities2)

examplePartition1 = { 0 : 0
                    , 1 : 0
                    , 2 : 0
                    , 3 : 0
                    , 4 : 1
                    , 9 : 1
                    , 6 : 1
                    , 7 : 1
                    }

examplePartition2 = { 0 : 0
                    , 1 : 1
                    , 2 : 2
                    , 3 : 3
                    , 4 : 4
                    , 9 : 2
                    , 6 : 2
                    , 7 : 2
                    }

name = "LFR_50000"
path = "./Graphs/Generated/" + name + "/"
partition = parse_partition(path + name + "cmty.txt")

print(compare_communities(partition, partition))
