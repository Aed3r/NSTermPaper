import matplotlib.pyplot as plt
import numpy as np
import csv
from ast import literal_eval

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

def plot_found_communities_bar(header, data):
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

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    plt.show()


def plot_scores_bar(header, data):
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

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

def plot_scores_line(header, data):
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

    plt.show()

def plot_times_bar(header, data):
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

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()


data = read_data("./Results.csv")

plot_scores_line(*data)
