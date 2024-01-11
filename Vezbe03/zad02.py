#%%
import networkx as nx
from matplotlib import pyplot as plt
import typing

#%%
with open("CA-GrQc.txt", "r") as f:
  [f.readline() for _ in range(4)]
  arxiv = nx.Graph()
  for line in f:
    u, v = line.rstrip('\n').split('\t')
    arxiv.add_edge(int(u), int(v))

#%%
centrality_metrics: typing.Dict[str, typing.Callable[[nx.Graph], dict]] = {
  "degree": nx.degree_centrality,
  "eigenvector": nx.eigenvector_centrality,
  "closeness": nx.closeness_centrality,
  "betweenness": nx.closeness_centrality,
}

for metric, function in centrality_metrics.items():
  print(f"metric: {metric}")
  ranks = function(arxiv)
  sorted_ranks = sorted(ranks, key=lambda i: ranks[i], reverse=True)
  top_nodes = [str(n) for n in sorted_ranks[:10]]
  print(f"top nodes: {' '.join(top_nodes)}")

#%%
arxiv.remove_edges_from(nx.selfloop_edges(arxiv))
cores = nx.core_number(arxiv)
max_core = max(cores.values())
arxiv_max_core = nx.k_core(arxiv, max_core, cores)


#%%
print(nx.number_connected_components(arxiv_max_core))
nx.draw(arxiv_max_core)
plt.show()
