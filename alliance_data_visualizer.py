import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import ListedColormap

import numpy as np
import xgi

def show_hypergraph(H, seed, k, title, is_weighted=False):
    labels = {node: str(int(node.removeprefix("player-0"))) for node in H.nodes}

    fig, ax = plt.subplots(figsize=(12, 8))
    fig.patch.set_facecolor("#E8E8E8")
    ax.set_facecolor("#E8E8E8")
    
    #pos = xgi.circular_layout(H)
    pos = xgi.barycenter_spring_layout(H, seed = seed, k = k)
    
    weights = H.edges.attrs("weight")
    
    if is_weighted:
        blues = plt.get_cmap("Blues")
        cmap = mcolors.LinearSegmentedColormap.from_list(
            "truncated_blues",
            blues(np.linspace(0.75, 1.0, 256))
        )
        
        xgi.draw(
            H,
            ax=ax,
            pos=pos,
            node_labels=labels,
            hyperedge_labels=False,
            node_size=20,
            hull=True,
            dyad_color=weights,
            dyad_color_cmap=cmap,
            edge_fc=weights,
            edge_fc_cmap=cmap
        )
    else:
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

def show_weighted_hypergraph(path, seed, k):
    H = xgi.read_hif(path)
    
    max_round = (int)(max(H.edges.attrs("created_round").asdict().values()))
    
    inverted_weights = {
        edge_id: (max_round - (int)(value) + 1) for edge_id, value in H.edges.attrs("created_round")
    }
    
    H.set_edge_attributes(inverted_weights, name="weight")
    
    show_hypergraph(H, seed, k, "Players:", is_weighted=True)
    
def show_weighted_tribe_hypergraph(path, seed, k, tribe):
    H = xgi.read_hif(path)
    tribe_nodes = [
        node
        for node in H.nodes
        if H.nodes[node]["tribe"] == tribe
    ]
    
    H = xgi.subhypergraph(H, tribe_nodes)
    
    max_round = (int)(max(H.edges.attrs("created_round").asdict().values()))
    
    inverted_weights = {
        edge_id: (max_round - (int)(value) + 1) for edge_id, value in H.edges.attrs("created_round")
    }
    
    H.set_edge_attributes(inverted_weights, name="weight")
        
    show_hypergraph(H, seed, k, f"{tribe}:", is_weighted=True)
    
    
if __name__ == "__main__":
    show_tribe_hypergraph("data/season_19/r4_alliances.json", 41, 0.35, "Black Mambas")
