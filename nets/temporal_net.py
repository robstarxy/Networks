import networkx_temporal as tx

TG = tx.temporal_graph() # TG = tx.TemporalMultiGraph()

TG.add_edge("a", "b", time=0)
TG.add_edge("c", "b", time=1)
TG.add_edge("d", "c", time=2)
TG.add_edge("d", "e", time=2)
TG.add_edge("a", "c", time=2)
TG.add_edge("f", "e", time=3)
TG.add_edge("f", "a", time=3)
TG.add_edge("f", "c", time=3)
TG.add_edge("f", "d", time=4)

TG = TG.slice(attr="time")

print(TG)

tx.draw(TG, layout="kamada_kawai", figsize=(8, 2))
