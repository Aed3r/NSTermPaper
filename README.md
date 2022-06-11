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

The memory_profiler tool mprof.py can be used to measure memory usage: `python mprof.py run <file>.py`
And to plot the generated data: `python mprof.py plot`

The functions used to analyze the graphs from snap can be directly downloaded and unpacked into a directory of choice.
NB. Some graphs have overlapping communities.
