#%%
import networkx as nx
from matplotlib import pyplot as plt

#%%
f = open("CA-GrQc.txt")
for _ in range(4):
  f.readline()
  
g = nx.Graph()
for line in f:
  u, v = line.rstrip('\n').split('\t')
  g.add_edge(int(u), int(v))

#%%
degree_centrality = nx.degree_centrality(g)
degree_top_ten = sorted(enumerate(degree_centrality), key=lambda t: t[1])[-10:]
print([id for id, _ in degree_top_ten])

#%%
eigenvector_centrality = nx.eigenvector_centrality(g)
eigenvector_top_ten = sorted(eigenvector_centrality.items(), key=lambda t: t[1])[-10:]
print([id for id, _ in eigenvector_top_ten])

#%%
closeness_centrality = nx.closeness_centrality(g)
closeness_top_ten = sorted(closeness_centrality.items(), key=lambda t: t[1])[-10:]
print([id for id, _ in closeness_top_ten])

#%%
betweenness_centrality = nx.betweenness_centrality(g)
betweenness_top_ten = sorted(betweenness_centrality.items(), key=lambda t: t[1])[-10:]
print([id for id, _ in betweenness_top_ten])

#%%
g.remove_edges_from(nx.selfloop_edges(g))
max_shell_index = max(nx.core_number(g).values())
max_core_subgraph = nx.k_core(g, max_shell_index)

#%%
nx.draw(max_core_subgraph)
plt.show()

#%%
print(len(list(nx.connected_components(max_core_subgraph))))
