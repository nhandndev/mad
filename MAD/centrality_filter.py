import networkx as nx

def calculate_centralities(G):
    """
    Tính toán 3 chỉ số trung tâm (Centrality Metrics) cực kỳ quan trọng cho tất cả các node trong đồ thị.
    Bao gồm: Degree (Bậc), Closeness (Độ gần gũi), Betweenness (Độ trung gian).
    
    Args:
        G (networkx.Graph): Đồ thị cần tính các chỉ số.
        
    Returns:
        dict: Một dictionary chứa 3 dictionary con tương ứng với 3 chỉ số.
              Key là tên chỉ số ('degree', 'closeness', 'betweenness'), Value là dict {node: score}.
    """
    # In ra thông báo đang xử lý tính toán
    print("[Chung] Đang tính các chỉ số centrality...")
    
    # Tính Degree Centrality: Đo lường số lượng kết nối trực tiếp của mỗi node
    degree = nx.degree_centrality(G)
    
    # Tính Closeness Centrality: Đo lường khoảng cách ngắn nhất trung bình đến mọi node khác
    closeness = nx.closeness_centrality(G)
    
    # Tính Betweenness Centrality: Đo lường mức độ kiểm soát luồng thông tin (là 'cầu nối')
    betweenness = nx.betweenness_centrality(G)
    
    # Trả về một từ điển gộp cả 3 kết quả tính toán lại
    return {'degree': degree, 'closeness': closeness, 'betweenness': betweenness}

def remove_top_vip_nodes(G, centrality_dict, percentage=0.1):
    """
    Xóa bỏ một tỷ lệ X% các node "VIP" (có điểm cao nhất) dựa trên một loại chỉ số centrality.
    Mô phỏng lại cuộc tấn công hoặc sự cố đứt gãy mạng lưới.
    
    Args:
        G (networkx.Graph): Đồ thị gốc.
        centrality_dict (dict): Dictionary chứa điểm centrality của các node {node: score}.
        percentage (float): Tỷ lệ phần trăm node cần xóa (từ 0.0 đến 1.0). Mặc định 0.1 (10%).
        
    Returns:
        networkx.Graph: Một bản sao của đồ thị sau khi đã xóa các node VIP.
    """
    # Tạo một bản sao của đồ thị gốc để không làm hỏng dữ liệu mạng lưới ban đầu
    G_filtered = G.copy()
    
    # Tính toán chính xác số lượng node cần xóa bằng cách lấy tổng số node nhân với tỷ lệ
    num_to_remove = int(len(G) * percentage)
    
    # Nếu số lượng cần xóa là 0 (hoặc tỷ lệ = 0), trả về luôn đồ thị không đổi
    if num_to_remove == 0:
        return G_filtered
        
    # Sắp xếp dictionary centrality theo giá trị điểm số giảm dần (reverse=True) để đưa VIP lên đầu
    sorted_nodes = sorted(centrality_dict.items(), key=lambda item: item[1], reverse=True)
    
    # Trích xuất danh sách chỉ chứa ID của các node cần xóa (lấy từ đầu danh sách đến num_to_remove)
    nodes_to_remove = [node for node, val in sorted_nodes[:num_to_remove]]
    
    # Thực hiện lệnh xóa hàng loạt các node đó khỏi đồ thị bản sao
    G_filtered.remove_nodes_from(nodes_to_remove)
    
    # In ra thông báo đã xóa bao nhiêu node
    print(f"[Chung] Đã xóa {num_to_remove} node VIP ({percentage*100}%).")
    
    # Trả về đồ thị mới đã bị tổn thương
    return G_filtered
