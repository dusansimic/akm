#%%
import networkx as nx
from matplotlib import pyplot as plt

#%%
edges = [
  (0, 4),
  (0, 5),
  (1, 0),
  (1, 2),
  (1, 6),
  (2, 7),
  (3, 2),
  (3, 4),
  (3, 8),
  (4, 9),
  (5, 7),
  (6, 8),
  (7, 9),
  (8, 5),
  (9, 6)
]

dig = nx.DiGraph()

dig.add_edges_from(edges)

#%%
strong_gig_nodes = max(
  nx.strongly_connected_components(dig),
  key=len
)
strong_gig = nx.subgraph(dig, strong_gig_nodes)

#%%
nx.draw_circular(strong_gig)
plt.show()
