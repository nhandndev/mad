import networkx as nx
import time

def detect_louvain(G):
    """Phát hiện cộng đồng bằng thuật toán Louvain và đo thời gian."""
    start_time = time.time()
    communities = nx.community.louvain_communities(G)
    exec_time = time.time() - start_time
    
    modularity = nx.community.modularity(G, communities)
    return communities, modularity, exec_time

def detect_girvan_newman(G):
    """Phát hiện cộng đồng bằng thuật toán Girvan-Newman (lấy phân cấp đầu tiên)."""
    if G.number_of_edges() == 0:
        return [], 0.0, 0.0
        
    start_time = time.time()
    comp = nx.community.girvan_newman(G)
    try:
        communities = tuple(sorted(c) for c in next(comp))
    except StopIteration:
        communities = [list(G.nodes())]
    exec_time = time.time() - start_time
    
    modularity = nx.community.modularity(G, communities)
    return communities, modularity, exec_time
