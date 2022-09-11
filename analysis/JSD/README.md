Generalized (alpha-) Jensen-Shannon-divergence
Example script to calculate the JSD between two probability distributions.


## Background

The generalized Jensen-Shannon-divergence measures the distance between two probability distribution.
It is a generalization of the  ['normal' Jensen-Shannon-divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence) using the [generalized entropy of order alpha](https://en.wikipedia.org/wiki/Tsallis_entropy).

More background can be found here:

Martin Gerlach, Francesc Font-Clos, and Eduardo G. Altmann, 
*Similarity of Symbol Frequency Distributions with Heavy Tails*, Physical Review X **6** (2016) 021009
https://journals.aps.org/prx/abstract/10.1103/PhysRevX.6.021009



## Running
Simply run 

    python run_jsda.py

Arguments

    -f1: word-count file #1

    -f2: word-count file #2

    -a: set the alpha-exponent in the JSD (default:1 = normal JSD)

    -n: get the normalized version of the JSD (default: False)

    -w: whether the two distributions should be weights according to size (default: False)

    -s: calculate expected JSD from random null model from s random realizations (default: s=0 )



## Data

The data are the counts of words from two books of the Project Gutenberg corpus.
- data/PG299_counts.txt
- data/PG304_counts.txt

where each line corresponds to the number of times a word occurs in that book

    word \t count \n




## Requirements:
- python
- numpy
- jupyer/matplotlib for the example-notebook


