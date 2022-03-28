# ABM_TeachingAndCCE

This repository contains the scripts to run simulations in

Nakata S, Takezawa M. (in prep.) Conditions under which faithful cultural transmission through teaching promotes cumulative cultural evolution.

Description of files:

* "Main_MultiNetwork.py" contains codes of simulation described in the Results section. To run the simulation, the script needs inputs of parameters as command-line arguments: Network name (give "MultiNetwork.csv"), Generation, Number of rounds, Rate of teaching phase, Chain ID. 

* "Main_SingleNetwork.py" contains codes of simulation described in the Section 2 in electronic supplementary material. To run the simulation, the script needs inputs of parameters as command-line arguments: Network name (give "SingleNetwork.csv"), Generation, Number of rounds, Rate of teaching phase, Chain ID. 

* "MultiNetwork.csv" and "SingleNetwork.csv" contain the adjacency matrix of the network. Each line shows the node numbers connected by edges.
