import os
import matplotlib.pyplot as plt
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

def get_avg(data):
    tmp = {}
    for row in data:
        handle = row[0][:-2]

        if handle not in tmp:
            tmp[handle] = []

        tmp[handle].append(row[2:])
        tmp[handle][-1].insert(0, 0)
    
    for item in tmp:
        tmp[item] = np.mean(tmp[item], axis = 0)

    new_data = []
    for item in tmp:
        new_data.append([item] + tmp[item].tolist())

    return new_data

def plot_found_communities_bar(header, data, name):
    # Transpose the data
    data = list(map(list, zip(*data)))
    data_dict = {}
    for (key, row) in zip(header, data):
        data_dict[key] = row

    labels = data_dict["Graph"]

    true_communities = data_dict["# true communities"]
    mod_communities  = data_dict["# communities found by modularity"]
    info_communities = data_dict["# communities found by MapEquation"]

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, true_communities, width, label='True')
    rects2 = ax.bar(x        , mod_communities,  width, label='Modularity')
    rects3 = ax.bar(x + width, info_communities, width, label='MapEquation')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Amount of communities')
    ax.set_xticks(x, labels, rotation = "vertical")
    ax.legend()

    # Bar labels overlap unfortunately
    # ax.bar_label(rects1, padding=3)
    # ax.bar_label(rects2, padding=3)
    # ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    #plt.show()
    plt.savefig(os.path.join("Plots", name + "_com.png"))


def plot_scores_bar(header, data, name):
    # Transpose the data
    data = list(map(list, zip(*data)))
    data_dict = {}
    for (key, row) in zip(header, data):
        data_dict[key] = row

    labels = data_dict["Graph"]

    mod_score = data_dict["Modularity NMI"]
    info_score = data_dict["MapEquation NMI"]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x -width/2 , mod_score, width, label='Modularity')
    rects2 = ax.bar(x + width/2, info_score, width, label='MapEquation')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Normalized mutual information score')
    ax.set_xticks(x, labels, rotation = "vertical")
    ax.legend()

    # Bar labels overlap unfortunately
    #ax.bar_label(rects1, padding=3)
    #ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    #plt.show()
    plt.savefig(os.path.join("Plots", name + "_scoresBar.png"))

def plot_scores_line(header, data, name):
    # Transpose the data
    data = list(map(list, zip(*data)))
    data_dict = {}
    for (key, row) in zip(header, data):
        data_dict[key] = row

    labels = data_dict["Graph"]

    mod_score = data_dict["Modularity NMI"]
    info_score = data_dict["MapEquation NMI"]



    x = np.arange(len(labels))  # the label locations

    fig, ax = plt.subplots()
    rects1 = ax.plot(x, mod_score,  marker = "o", label='Modularity')
    rects2 = ax.plot(x, info_score, marker = "D", label='MapEquation')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Normalized mutual information score')
    ax.set_xticks(x, labels, rotation = "vertical")
    ax.legend()

    fig.tight_layout()

    #plt.show()
    plt.savefig(os.path.join("Plots", name + "_scoresLine.png"))

def plot_times_bar(header, data, name):
    # Transpose the data
    data = list(map(list, zip(*data)))
    data_dict = {}
    for (key, row) in zip(header, data):
        data_dict[key] = row

    labels = data_dict["Graph"]

    mod_score = data_dict["Modularity time (s)"]
    info_score = data_dict["MapEquation time (s)"]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x -width/2 , mod_score, width, label='Modularity')
    rects2 = ax.bar(x + width/2, info_score, width, label='MapEquation')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Time to execute')
    ax.set_xticks(x, labels, rotation = "vertical")
    ax.legend()

    # Bar labels overlap unfortunately
    #ax.bar_label(rects1, padding=3)
    #ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    #plt.show()
    plt.savefig(os.path.join("Plots", name + "_times.png"))

# Make sure destination folder exists
os.makedirs("Plots", exist_ok = True)

for name, _ in Parameters.params.items():
    (headers, data) = read_data(os.path.join("Results", name + ".csv"))

    data = get_avg(data)

    print(name)
    plot_found_communities_bar(headers, data, name)
    plot_scores_bar(headers, data, name)
    plot_scores_line(headers, data, name)
    plot_times_bar(headers, data, name)
