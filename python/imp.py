import numpy as np
import csv
import networkx as nx
import numpy as np


#cloness cetrarity(近接中心性)
G = nx.Graph()
edges = []
with open('assets\qiita.csv') as f:
    csvreader = csv.reader(f)
    flag = True
    for row in csvreader:
        if(flag):
            flag = False
            continue
        edges.append((row[0], row[1], row[2]))
G.add_weighted_edges_from(edges)

vp = [[], [], [], []]
print(vp)
cc = []
for k , v in nx.closeness_centrality(G).items():
    cc.append((k, v))
cc.sort(key= lambda x:x[1], reverse=True)
print(cc)

h = len(cc) // 4
print(h)
cnt = 0
p = 0
for i, j in cc:
    vp[p].append(int(i))
    print(i)
    cnt += 1
    if(cnt >= h):
        cnt = 0
        p += 1
print(vp)

size = int(len(cc)**(0.8))

IMP = []
for i in range(size):
    rand = np.random.rand()
    if(rand <= 0.7):
        IMP.append(vp[0][0])
    elif(rand <= 0.85):
        IMP.append(vp[1][0])
    elif(rand <= 0.95):
        IMP.append(vp[2][0])
    else:
        IMP.append(vp[3][0])
print(size)
print(IMP)