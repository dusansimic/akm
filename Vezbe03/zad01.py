#%%
import networkx as nx
from matplotlib import pyplot as plt

#%%
karate = nx.karate_club_graph()

#%%
k_degree_cent = nx.degree_centrality(karate)
k_degree_cent = [s * 1000 for s in k_degree_cent.values()]
nx.draw_networkx(karate, node_size=k_degree_cent)
plt.show()

#%%
k_eigenvector_cent = nx.eigenvector_centrality(karate)
k_eigenvector_cent = [s * 1000 for s in k_eigenvector_cent.values()]
nx.draw_networkx(karate, node_size=k_eigenvector_cent)
plt.show()

#%%
k_closeness_cent = nx.closeness_centrality(karate)
k_closeness_cent = [s * s * s * 2000 for s in k_closeness_cent.values()]
nx.draw_networkx(karate, node_size=k_closeness_cent)
plt.show()

#%%
k_betweenness_cent = nx.betweenness_centrality(karate)
k_betweenness_cent = [s * 1000 for s in k_betweenness_cent.values()]
nx.draw_networkx(karate, node_size=k_betweenness_cent)
