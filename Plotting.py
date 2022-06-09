import matplotlib.pyplot as plt
import numpy as np
import csv
from ast import literal_eval

def simplest_type(s):
    try:
        return literal_eval(s)
    except:
        return s

def plot(path):
    with open(path, "r") as f:
        reader = csv.reader(f, skipinitialspace = True)
        data = []
        for row in reader:
            row = list(map(simplest_type, row))
            print(row)
            data.append(row)

    header = data.pop(0)

    data = np.array(data)

    return header, data

print(plot("./Results.csv"))
