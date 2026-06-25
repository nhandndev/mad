import networkx as nx

def calculate_centralities(G):
    """Tính 3 chỉ số trung tâm: Degree, Closeness, Betweenness."""
    print("[Trung] Đang tính các chỉ số centrality...")
    degree = nx.degree_centrality(G)
    closeness = nx.closeness_centrality(G)
    betweenness = nx.betweenness_centrality(G)
    return {'degree': degree, 'closeness': closeness, 'betweenness': betweenness}

def remove_top_vip_nodes(G, centrality_dict, percentage=0.1):
    """Xóa X% node VIP nhất dựa trên một loại centrality cụ thể."""
    G_filtered = G.copy()
    num_to_remove = int(len(G) * percentage)
    
    if num_to_remove == 0:
        return G_filtered
        
    sorted_nodes = sorted(centrality_dict.items(), key=lambda item: item[1], reverse=True)
    nodes_to_remove = [node for node, val in sorted_nodes[:num_to_remove]]
    
    G_filtered.remove_nodes_from(nodes_to_remove)
    print(f"[Trung] Đã xóa {num_to_remove} node VIP ({percentage*100}%).")
    return G_filtered
