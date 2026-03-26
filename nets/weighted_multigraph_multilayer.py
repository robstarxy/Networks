import networkx as nx
import matplotlib as plt

class WeightedMultigraphMultilayer:
    def __init__(self):
        self.graph = nx.MultiGraph()

    def add_edge(self, u, v, layer, weight):
        self.graph.add_edge(u, v, key=layer, weight=weight)

    def get_edges(self):
        return self.graph.edges(data=True)
    
#create a weighted multigraph multilayer
wmm = WeightedMultigraphMultilayer()                
wmm.add_edge('a', 'b', 'layer1', 3)
wmm.add_edge('a', 'b', 'layer2', 5)
wmm.add_edge('b', 'c', 'layer1', 1)
wmm.add_edge('b', 'c', 'layer2', 3)     
print(wmm.get_edges())
    


#def Edge as tuple (u, v, l, w):
#    return (u, v, l, w)

#def spreading process on a weighted multigraph multilayer:


#SIS: Susceptible-Infected-Susceptible model

#UAU: Unaware-Aware-Unaware model