import os
import numpy as np
import csv
from ast import literal_eval
from Parameters import *
import Parameters

def simplest_type(s):
    try:
        return literal_eval(s)
    except:
        return s

def read_data(path):
    with open(path, "r") as f:
        reader = csv.reader(f, skipinitialspace = True)
        data = []
        for row in reader:
            row = list(map(simplest_type, row))
            data.append(row)

    header = data.pop(0)

    return header, data

# Calculates total average running times over all experiments
def total_avg_running_time(data):
    total_mod = 0
    total_map = 0
    count = 0

    for scenario in data:
        for experimentData in data[scenario]:
            total_mod += experimentData[7]
            total_map += experimentData[8]
            count += 1
    
    print("Total average modularity running time:", str(round(total_mod / count, 2)), "s")
    print("Total average map equation running time:", str(round(total_map / count, 2)), "s")

# Calculates the average difference in amount of communities found over all experiments
def total_avg_community_count_difference(data):
    total_mod = 0
    total_map = 0
    count = 0

    for scenario in data:
        for experimentData in data[scenario]:
            total_mod += experimentData[3] - experimentData[2]
            total_map += experimentData[4] - experimentData[2]
            count += 1
    
    print("Total average error finding the right amount of communities by modularity:", str(round(total_mod / count, 2)))
    print("Total average error finding the right amount of communities by the map equation:", str(round(total_map / count, 2)))

# Calculates the average difference in NMI score between modularity and the map equation
def total_avg_nmi_difference(data):
    total_mod = 0
    total_map = 0
    count = 0

    for scenario in data:
        for experimentData in data[scenario]:
            total_mod += experimentData[5]
            total_map += experimentData[6]
            count += 1
    
    print("Total average NMI score of modularity:", str(round(total_mod / count, 2)))
    print("Total average NMI score of the map equation:", str(round(total_map / count, 2)))

# Compares nmi scores between varying community size situations and without
def nmi_varying_vs_not(data):
    total_varying = 0
    total_not = 0
    count_varying = 0
    count_not = 0

    for scenario in data:
        for experimentData in data[scenario]:
            if scenario.endswith("varying"):
                total_varying += experimentData[6] - experimentData[5]
                count_varying += 1
            else:
                total_not += experimentData[6] - experimentData[5]
                count_not += 1
    
    print("Total average difference in NMI scores between the map equation and modularity when community sizes vary:", str(round(total_varying / count_varying, 2)))
    print("Total average difference in NMI scores between the map equation and modularity when community sizes do not vary:", str(round(total_not / count_not, 2)))

# Compares nmi scores between highly interconnected communities situations and without
def nmi_interconnected_vs_not(data):
    total_interconnected_mod = 0
    total_not_mod = 0
    total_interconnected_map = 0
    total_not_map = 0
    count_interconnected = 0
    count_not = 0

    for scenario in data:
        for experimentData in data[scenario]:
            if scenario.endswith("interconnected") or scenario == "random_interconnected":
                total_interconnected_mod += experimentData[5]
                total_interconnected_map += experimentData[6]
                count_interconnected += 1
            else:
                total_not_mod += experimentData[5]
                total_not_map += experimentData[6]
                count_not += 1
    
    print("Total average NMI score for modularity in highly interconnected scenarios:", str(round(total_interconnected_mod / count_interconnected, 2)))
    print("Total average NMI score for the map equation in highly interconnected scenarios:", str(round(total_interconnected_map / count_interconnected, 2)))
    print("Total average NMI score for modularity in other scenarios:", str(round(total_not_mod / count_not, 2)))
    print("Total average NMI score for the map equation in other scenarios:", str(round(total_not_map / count_not, 2)))


data = {}
for name, _ in Parameters.params.items():
    try:
        (headers, fileData) = read_data(os.path.join("Results", name + ".csv"))
    except:
        print("Error: '" + name + ".csv' is missing")
    
    data[name] = fileData

total_avg_running_time(data)
total_avg_community_count_difference(data)
total_avg_nmi_difference(data)
nmi_varying_vs_not(data)
nmi_interconnected_vs_not(data)