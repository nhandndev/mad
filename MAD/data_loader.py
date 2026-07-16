"""
/**
 * File: data_loader.py
 * Phụ trách: Chương (Kỹ sư Quản trị Dữ liệu)
 * Mô tả:
 *   - Chuyên nạp và sinh đồ thị mạng lưới.
 *   - Hàm load_karate_club() tải đồ thị thực tế (Karate Club).
 *   - Hàm generate_facebook_network() dùng thuật toán Barabási-Albert sinh mạng giả lập (Scale-free).
 */
"""
import networkx as nx

def load_karate_club():
    """
    Nạp mạng lưới Karate Club gốc có sẵn trong thư viện NetworkX.
    Mạng này gồm 34 thành viên và 78 mối quan hệ, đóng vai trò là mạng lưới thực tế chuẩn mực.
    
    Returns:
        networkx.Graph: Đồ thị vô hướng (undirected graph) của Karate Club.
    """
    # In ra thông báo cho biết đang nạp dữ liệu để theo dõi tiến trình
    print("[Chương] Đang nạp đồ thị Karate Club...")
    
    # Gọi hàm tích hợp của NetworkX để lấy bộ dữ liệu Karate Club
    return nx.karate_club_graph()

def generate_facebook_network(n=300, m=3):
    """
    Giả lập một mạng xã hội ảo (VD: Facebook) bằng thuật toán Barabási-Albert.
    Tạo ra một đồ thị dạng Scale-free theo nguyên tắc "Rich-get-richer" (người nhiều bạn dễ có thêm bạn).
    
    Args:
        n (int): Tổng số lượng node (người dùng) muốn tạo. Mặc định là 300.
        m (int): Số lượng cạnh (kết nối) mới mà mỗi node sẽ tạo ra khi được thêm vào. Mặc định là 3.
        
    Returns:
        networkx.Graph: Đồ thị Barabási-Albert đã được sinh ra.
    """
    # In ra thông báo đang tạo đồ thị mô phỏng kèm theo các tham số
    print(f"[Chương] Đang tạo đồ thị Barabási-Albert (n={n}, m={m})...")
    
    # Sử dụng Barabási-Albert để mô phỏng tính chất mạng xã hội
    return nx.barabasi_albert_graph(n, m)

if __name__ == "__main__":
    # Đoạn code này chỉ chạy khi thực thi trực tiếp file data_loader.py dùng để test thử độc lập
    
    # Nạp thử đồ thị Karate
    G_karate = load_karate_club()
    
    # Nạp thử đồ thị Facebook mô phỏng
    G_fb = generate_facebook_network()
    
    # In ra số lượng node của 2 đồ thị để kiểm tra xem hàm nạp/tạo có hoạt động đúng không
    print(f"Karate: {G_karate.number_of_nodes()} nodes | Facebook: {G_fb.number_of_nodes()} nodes")
