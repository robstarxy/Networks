# Coding a many-to-many multilayer graph. Multiple realisations of one actor in multiple layer that are coupled with each other through interlayer edges. A network of networs.


import networkx as nx

class MultilayerGraphComplex:
    def __init__(self):
        self.graph = nx.MultiDiGraph()

    def add_edge(self, v, u, e, layer, c, weight=None):
        self.graph.add_edge(v, u, intralayer_edge=e, key=layer, coupling=c, weight=weight)

    def get_edges(self):
        return self.graph.edges(data=True)
    

    