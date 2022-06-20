# Network Science term paper:
## Comparison between several measures of community structure

This repository contains all code related to our term paper.

The following python packages are required to run the experiments:
 - networkx
 - matplotlib
 - psutil
 - memory_profiler
 - sklearn
 - scipy
 - infomap

They can all be installed using pip: `pip install <package-name>`

To generate a new LFR benchmark, simply modify the parameters in `Parameters.py` and `LFR_gen.py` and run the latter. The resulting files should appear in `Graphs/LFR/...`.

The generated graphs can be previewed using `Display_graph.py`. The file can be set as a parameter atop the file. The graph drawing functionalities offered by NetworkX are not particularly strong, we recommend using external software such as Cytoscape (https://cytoscape.org/).

To run tests on saved networks, simply modify the parameters at the top of `Run_test.py` and run. The results should appear in the folders `Found_communities` and `Results`. The latter contains convenient CSV files.

The script `Plotting.py` can be used to plot the results from the generated CSV files.

The memory_profiler tool mprof.py can be used to measure memory usage: `python mprof.py run <file>.py`
And to plot the generated data: `python mprof.py plot`

The functions used to analyze the graphs from snap can be directly downloaded and unpacked into a directory of choice.
NB. Some graphs have overlapping communities.
