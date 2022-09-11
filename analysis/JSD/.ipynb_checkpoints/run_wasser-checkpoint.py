# +
import os
from collections import Counter
_data_path = "./data/ngrams"
from matplotlib import pyplot as plt
corpus2dist = {}
import sys
src = sys.argv[1]
tgt=  sys.argv[2]
print(src,tgt)
p = src
corpus2dist[p] = [list(range(500)),[0] * 500]
with open(p,"r") as f:
    data = f.readlines()
l2c = [0] * 500
for d in data:
    l,c = [int(x) for x in d.strip().split()]
    if l < 50000:
        try:
            l2c[l] = c
        except:
            l2c += [0] * (l-len(l2c)+1)
            l2c[l] = c

#plt.bar(range(len(l2c)),l2c)
#corpus2dist[p][0] = range(len(l2c))
#corpus2dist[p][1] = l2c
#plt.title(p)
#plt.show()
#plt.clf()
#print(corpus2dist)
# -

p = tgt
corpus2dist[p] = [list(range(500)),[0] * 500]
with open(p,"r") as f:
    data = f.readlines()
l2c2 = [0] * 500
for d in data:
    l,c = [int(x) for x in d.strip().split()]
    if l < 50000:
        try:
            l2c2[l] = c
        except:
            l2c2 += [0] * (l-len(l2c2)+1)
            l2c2[l] = c
#plt.bar(range(len(l2c)),l2c)
#corpus2dist[p][0] = range(len(l2c2))
#corpus2dist[p][1] = ll2c22c

from scipy.stats import wasserstein_distance as wsd
val = wsd(range(len(l2c)),range(len(l2c2)),l2c,l2c2)
print(val)


