import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import xgi

def show_hypergraph(H, seed, k, title):
    labels = {node: str(int(node.removeprefix("player-0"))) for node in H.nodes}

    fig, ax = plt.subplots(figsize=(12, 8))
    #pos = xgi.circular_layout(H)
    pos = xgi.barycenter_spring_layout(H, seed = seed, k = k)
    xgi.draw(
        H,
        ax=ax,
        pos=pos,
        node_labels=labels,
        hyperedge_labels=False,
        node_size=20,
        hull=True
    )

    legend_items = [
        Line2D([], [], linestyle="none", label=f"{labels[node]}  {H.nodes[node]['name']}")
        for node in sorted(H.nodes, key=lambda node: int(node.split("-")[-1]))
    ]
    
    ax.legend(
        handles=legend_items,
        title=title,
        loc="upper right",
        bbox_to_anchor=(0, 1),
        frameon=False,
    )

    fig.tight_layout()
    plt.show()
    
def show_full_hypergraph(path, seed, k):
    H = xgi.read_hif(path)
    show_hypergraph(H, seed, k, "Players:")
    
def show_tribe_hypergraph(path, seed, k, tribe):
    H = xgi.read_hif(path)
    tribe_nodes = [
        node
        for node in H.nodes
        if H.nodes[node]["tribe"] == tribe
    ]
    
    H = xgi.subhypergraph(H, tribe_nodes)
        
    show_hypergraph(H, seed, k, f"{tribe}:")
    
    
if __name__ == "__main__":
    show_tribe_hypergraph("data/season_19/r3_alliances.json", 41, 0.35, "Black Mambas")
