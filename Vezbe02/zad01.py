#%%
import networkx as nx
from matplotlib import pyplot as plt

#%%
karate = nx.karate_club_graph()

#%%
nx.draw(karate)
plt.show()

#%%
degree_centrality = nx.degree_centrality(karate)
degree_node_sizes = [c * 20 for c in degree_centrality]
nx.draw_networkx(karate, node_size=degree_node_sizes)

#%%
eigenvector_centrality = nx.eigenvector_centrality(karate)
eigenvector_node_sizes = [c * 1000 for c in list(eigenvector_centrality.values())]
nx.draw_networkx(karate, node_size=eigenvector_node_sizes)

#%%
closeness_centrality = nx.closeness_centrality(karate)
closeness_node_sizes = [c * 1000 for c in list(closeness_centrality.values())]
nx.draw_networkx(karate, node_size=closeness_node_sizes)

#%%
betweenness_centrality = nx.betweenness_centrality(karate)
betweenness_node_sizes = [c * 2000 for c in list(betweenness_centrality.values())]
nx.draw_networkx(karate, node_size=betweenness_node_sizes)
