import networkx as nx

def load_karate_club():
    """Nạp mạng lưới Karate Club có sẵn trong NetworkX."""
    print("[Chương] Đang nạp đồ thị Karate Club...")
    return nx.karate_club_graph()

def generate_facebook_network(n=300, m=3):
    """Giả lập mạng xã hội (VD: Facebook) bằng thuật toán Barabási-Albert."""
    print(f"[Chương] Đang tạo đồ thị Barabási-Albert (n={n}, m={m})...")
    # Sử dụng Barabási-Albert để mô phỏng tính chất "rich-get-richer" của mạng xã hội
    return nx.barabasi_albert_graph(n, m)

if __name__ == "__main__":
    # Test thử độc lập
    G_karate = load_karate_club()
    G_fb = generate_facebook_network()
    print(f"Karate: {G_karate.number_of_nodes()} nodes | Facebook: {G_fb.number_of_nodes()} nodes")
