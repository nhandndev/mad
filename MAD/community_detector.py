import networkx as nx
import time

def detect_louvain(G):
    """
    Phát hiện cộng đồng bằng thuật toán Louvain (Bottom-up) và đo lường thời gian thực thi.
    
    Args:
        G (networkx.Graph): Đồ thị mạng lưới cần phát hiện cộng đồng.
        
    Returns:
        tuple: Trả về một tuple gồm 3 phần tử:
            - communities (list of sets): Danh sách các tập hợp node, mỗi tập hợp là một cộng đồng.
            - modularity (float): Điểm chất lượng phân chia cộng đồng (Modularity Q).
            - exec_time (float): Thời gian thực thi thuật toán (tính bằng giây).
    """
    # Ghi nhận thời điểm bắt đầu để đo lường hiệu năng
    start_time = time.time()
    
    # Gọi thuật toán Louvain từ thư viện NetworkX để gom cụm cộng đồng
    communities = nx.community.louvain_communities(G)
    
    # Tính toán tổng thời gian đã trôi qua kể từ lúc bắt đầu
    exec_time = time.time() - start_time
    
    # Chấm điểm Modularity cho kết quả phân chia cộng đồng vừa tìm được
    modularity = nx.community.modularity(G, communities)
    
    # Trả về cụm cộng đồng, điểm Modularity và thời gian chạy
    return communities, modularity, exec_time

def detect_girvan_newman(G):
    """
    Phát hiện cộng đồng bằng thuật toán Girvan-Newman (Top-down) và lấy phân cấp đầu tiên.
    
    Args:
        G (networkx.Graph): Đồ thị mạng lưới cần phát hiện cộng đồng.
        
    Returns:
        tuple: Trả về một tuple gồm 3 phần tử:
            - communities (tuple of lists): Cấu trúc cộng đồng ở bước phân chia đầu tiên.
            - modularity (float): Điểm chất lượng phân chia cộng đồng (Modularity Q).
            - exec_time (float): Thời gian thực thi thuật toán (tính bằng giây).
    """
    # Nếu đồ thị trống (không có cạnh nào), trả về kết quả rỗng ngay lập tức để tránh lỗi
    if G.number_of_edges() == 0:
        return [], 0.0, 0.0
        
    # Ghi nhận thời điểm bắt đầu để đo thời gian chạy
    start_time = time.time()
    
    # Chạy thuật toán Girvan-Newman. Thuật toán này trả về một generator các bước phân chia
    comp = nx.community.girvan_newman(G)
    
    try:
        # Dùng next(comp) để lấy kết quả của bước phân chia cắt cạnh đầu tiên (level 1)
        # Sắp xếp các node trong mỗi cộng đồng và chuyển thành tuple
        communities = tuple(sorted(c) for c in next(comp))
    except StopIteration:
        # Nếu không thể phân chia được nữa, coi như toàn bộ đồ thị là 1 cộng đồng duy nhất
        communities = [list(G.nodes())]
        
    # Tính toán thời gian thực thi của thuật toán Girvan-Newman
    exec_time = time.time() - start_time
    
    # Chấm điểm Modularity để xem việc chia cắt này có tốt không
    modularity = nx.community.modularity(G, communities)
    
    # Trả về kết quả
    return communities, modularity, exec_time
