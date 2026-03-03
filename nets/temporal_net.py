# import networkx_temporal as tx

# TG = tx.temporal_graph() # TG = tx.TemporalMultiGraph()

# TG.add_edge("a", "b", time=0)
# TG.add_edge("c", "b", time=1)
# TG.add_edge("d", "c", time=2)
# TG.add_edge("d", "e", time=2)
# TG.add_edge("a", "c", time=2)
# TG.add_edge("f", "e", time=3)
# TG.add_edge("f", "a", time=3)
# TG.add_edge("f", "c", time=3)
# TG.add_edge("f", "d", time=4)

# TG = TG.slice(attr="time")

# print(TG)

# tx.draw(TG, layout="kamada_kawai", figsize=(8, 2))


#%load_ext autoreload
# %autoreload 2

import tnetwork as tn
import networkx as nx
import seaborn as sns


my_d_graph = tn.DynGraphIG()


my_d_graph.add_node_presence("a",(1,5)) #add node a during interval [1,5[
my_d_graph.add_nodes_presence_from(["a","b","c"],(2,3)) # add ndoes a,b,c from 2 to 3
my_d_graph.add_nodes_presence_from("d",(2,6)) #add node from 2 to 6

my_d_graph.add_interaction("a","b",(2,3)) # link nodes a and b from 2 to 3
my_d_graph.add_interactions_from(("b","d"),(2,5)) # link nodes b and d from 2 to 5

plot = tn.plot_longitudinal(my_d_graph,width=400,height=200)