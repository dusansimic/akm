#%%
import networkx as nx
from matplotlib import pyplot as plt
import itertools
import random

#%%
def genER(N: int, p: float) -> nx.Graph:
  g = nx.Graph()
  for u in range(N):
    for v in range(u + 1, N):
      if random.random() <= p:
        g.add_edge(u, v)
  return g

plt.figure(1)
plt.subplot(311)
g001 = genER(1000, .001)
nx.draw(g001)
plt.subplot(312)
g01 = genER(1000, .01)
nx.draw(g01)
plt.subplot(313)
g0001 = genER(1000, .0001)
nx.draw(g0001)
plt.show()

#%%
g001_max_conn_comp = max(nx.connected_components(g001), key=len)
g01_max_conn_comp = max(nx.connected_components(g01), key=len)
g0001_max_conn_comp = max(nx.connected_components(g0001), key=len)

g001_max_conn_comp_size = len(g001_max_conn_comp)
g01_max_conn_comp_size = len(g01_max_conn_comp)
g0001_max_conn_comp_size = len(g0001_max_conn_comp)

max_conn_comp_sizes = [g001_max_conn_comp_size, g01_max_conn_comp_size, g0001_max_conn_comp_size]

print("      g001  g01 g0001")
for i, (size1, size2) in enumerate(itertools.product(max_conn_comp_sizes, max_conn_comp_sizes)):
  if (i + 1) % 3 == 1:
    if i // 3 == 0:
      print("g001 ", end='')
    elif i // 3 == 1:
      print("g01  ", end='')
    else:
      print("g0001", end='')
  print("{:5d}".format(size1 - size2), end='')
  if (i + 1) % 3 == 0:
    print()
