#%%
import networkx as nx
from matplotlib import pyplot as plt
from scipy import stats as spstats
import itertools
import typing

#%%
with open("Wiki-Vote.txt", "r") as f:
  [f.readline() for _ in range(4)]
  wiki = nx.DiGraph()
  for line in f:
    u, v = line.rstrip('\n').split('\t')
    wiki.add_edge(int(u), int(v))

#%%
edges = 0
for u, v in wiki.edges:
  if wiki.has_edge(v, u):
    edges += 1

edges //= 2
print(edges)

#%%
pagerank_score = nx.pagerank(wiki)
hits_score = nx.hits(wiki)[0]

def maksimalni(score: typing.Dict[int, float]):
  return max(score, key=lambda i: score[i])

max_pagerank = maksimalni(pagerank_score)
max_hits = maksimalni(hits_score)
print(max_pagerank, max_hits)

#%%
pagerank_top_10 = sorted(pagerank_score, key=lambda i: pagerank_score[i], reverse=True)[:10]
hits_top_10 = sorted(hits_score, key=lambda i: hits_score[i], reverse=True)[:10]
print(pagerank_top_10)
print(hits_top_10)

#%%
local_cent = {
  "indeg": list(nx.in_degree_centrality(wiki).values()),
  "outdeg": list(nx.out_degree_centrality(wiki).values()),
}
global_cent = {
  "pagerank": list(nx.pagerank(wiki).values()),
  "hits": list(nx.hits(wiki)[0].values()),
}
corrs = {}

for xkey, ykey in itertools.product(local_cent.keys(), global_cent.keys()):
  corrs[f"{xkey}-{ykey}"] = spstats.spearmanr(local_cent[xkey], global_cent[ykey]).statistic

print(corrs)

#%%
nontrivial_comps = [comp for comp in nx.strongly_connected_components(wiki) if len(comp) > 1]

def prosek_metrike(nodes: typing.Set[int], scores: typing.Dict[int, float]):
  score_set = {value for key, value in scores.items() if key in nodes}
  return sum(score_set) / len(score_set)

for i, comp in enumerate(nontrivial_comps):
  print(f"{i} -> pagerank: {prosek_metrike(comp, pagerank_score)}  hits: {prosek_metrike(comp, hits_score)}")
