import networkx as nx
import matplotlib.pyplot as plt

def build_graph(triples):
    if not triples:
        print("❌ No data to display in graph.")
        return

    G = nx.DiGraph()

    for subj, rel, obj in triples:
        if subj and rel and obj:
            G.add_node(subj)
            G.add_node(obj)
            G.add_edge(subj, obj, label=rel)

    # Layout setup
    pos = nx.spring_layout(G, k=1.1, seed=42)

    # Set aesthetics
    node_color = '#A2D5F2'        # Soft blue
    edge_color = '#555555'        # Dark grey
    font_color = '#333333'        # Darker font
    edge_label_color = '#FF6F61'  # Coral for relation labels
    bg_color = '#F7F9FC'          # Very light grey background

    plt.figure(figsize=(14, 10))
    ax = plt.gca()
    ax.set_facecolor(bg_color)  # Set graph background

    # Draw nodes and edges
    nx.draw_networkx_nodes(G, pos, node_color=node_color, edgecolors='black', node_size=3500)
    nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=2, arrows=True, arrowsize=25, arrowstyle='-|>')

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=14, font_color=font_color, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color=edge_label_color, font_weight='semibold')

    # Final touches
    plt.title("Knowledge Graph", fontsize=20, fontweight='bold', color='#2C3E50')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
