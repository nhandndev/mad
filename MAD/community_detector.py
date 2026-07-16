"""
/**
 * File: community_detector.py
 * Phụ trách: Siêu (Chuyên gia Tối ưu Thuật toán)
 * Mô tả:
 *   - Chứa các thuật toán AI phức tạp dùng để phát hiện cộng đồng trong mạng.
 *   - Triển khai 2 chiến lược đối nghịch: Louvain (Bottom-up, gom cụm) và Girvan-Newman (Top-down, phân rã).
 *   - Đo lường thời gian chạy cực kỳ chi tiết và chấm điểm chất lượng phân cụm Modularity.
 */
"""
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
    
    # Gọi thuật toán Louvain từ thư viện NetworkX để gom cụm cộng đồng.
    # GIẢI THÍCH THUẬT TOÁN LOUVAIN: Đây là thuật toán Heuristic tiếp cận từ dưới lên (Bottom-up).
    # Khởi đầu, nó coi mỗi node là 1 cộng đồng riêng lẻ. Sau đó, nó thử gộp các node láng giềng lại với nhau.
    # Nếu việc gộp này làm tăng điểm Modularity (Q), nó sẽ chốt sự gộp đó. Quá trình lặp lại liên tục 
    # cho đến khi không thể làm Modularity tăng thêm được nữa. Vì chỉ tính toán cục bộ nên nó chạy CỰC KỲ NHANH.
    communities = nx.community.louvain_communities(G)
    
    # Tính toán tổng thời gian đã trôi qua kể từ lúc bắt đầu
    exec_time = time.time() - start_time
    
    # Chấm điểm Modularity cho kết quả phân chia cộng đồng vừa tìm được.
    # GIẢI THÍCH ĐIỂM MODULARITY (Q): Thang điểm đánh giá độ tốt của việc chia nhóm (thường từ -0.5 đến 1.0).
    # Cơ chế chấm điểm: Q sẽ CAO khi các node TRONG CÙNG MỘT NHÓM có mật độ liên kết chằng chịt với nhau, 
    # và các liên kết CHÉO GIỮA CÁC NHÓM KHÁC NHAU cực kỳ thưa thớt. Nếu Q thấp nghĩa là thuật toán chia nhóm sai 
    # hoặc mạng lưới đã bị đứt gãy, vỡ nát hoàn toàn.
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
    
    # Chạy thuật toán Girvan-Newman. Thuật toán này trả về một generator các bước phân chia.
    # GIẢI THÍCH THUẬT TOÁN GIRVAN-NEWMAN: Đây là thuật toán tiếp cận từ trên xuống (Top-down).
    # Nó đi tìm tất cả các sợi dây (cạnh) đóng vai trò là "Cầu nối" (Edge Betweenness cao nhất).
    # Sau đó nó "chặt" đứt sợi dây đó đi, rồi lại tính lại từ đầu. Cứ chặt liên tục cho đến khi 
    # mạng lưới bị đứt làm đôi (thành 2 cộng đồng), đứt làm 3... Thuật toán này chạy RẤT CHẬM nhưng rất triệt để.
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
    
    # Chấm điểm Modularity để xem việc chia cắt này có tốt không.
    # Tương tự như trên, dùng hàm toán học để kiểm tra xem cấu trúc bị chặt ra bởi Girvan-Newman có chặt chẽ không.
    modularity = nx.community.modularity(G, communities)
    
    # Trả về kết quả
    return communities, modularity, exec_time
