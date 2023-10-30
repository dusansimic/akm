#%%
import networkx as nx
from matplotlib import pyplot as plt

#%%
flo = nx.florentine_families_graph()

print(nx.nodes(flo))
print(nx.edges(flo))

#%%
flodir = nx.to_directed(flo)

nx.draw(flodir)
plt.show()

# %%
