# Computational model for Teaching and Cumulative cultural evolution

This repository contains the scripts to run simulations in

Nakata, S. & Takezawa, M. (2023). Conditions under which faithful cultural transmission through teaching promotes cumulative cultural evolution. Scientific Reports, 13, 20986. https://doi.org/10.1038/s41598-023-47018-7


Description of files:

* "Main_MultiNetwork.py" contains codes of simulation described in the Results section. To run the simulation, the script needs inputs of parameters as command-line arguments: Network name (give "MultiNetwork.csv"), Generation, Number of rounds, Rate of teaching phase, Chain ID. All parameter combinations reported in the paper.

* "Main_SingleNetwork.py" contains codes of simulation described in the Section 2 in electronic supplementary material. To run the simulation, the script needs inputs of parameters as command-line arguments: Network name (give "SingleNetwork.csv"), Generation, Number of rounds, Rate of teaching phase, Chain ID. 

* "MultiNetwork.csv" and "SingleNetwork.csv" contain the adjacency matrix of the network. Each line shows the node numbers connected by edges.
