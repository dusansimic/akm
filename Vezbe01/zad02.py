#%%
import networkx as nx
from matplotlib import pyplot as plt

#%%
mis = nx.les_miserables_graph()

print(nx.number_connected_components(mis))

# %%
gig_nodes = max(nx.connected_components(mis), key=len)
gig = nx.subgraph(mis, gig_nodes)

nx.draw(gig)
plt.show()
