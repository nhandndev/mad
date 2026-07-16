"""
/**
 * File: visualizer.py
 * Phụ trách: Huy (Kỹ sư Trực quan hóa & Phân tích)
 * Mô tả:
 *   - Chịu trách nhiệm biến các ma trận số khô khan thành hình ảnh có ý nghĩa.
 *   - Hàm plot_network_communities() dàn trang các node ra không gian 2D và tô màu phân nhóm.
 *   - Hàm plot_modularity_trend() đọc file CSV để vẽ đồ thị đường (Lineplot) so sánh hiệu năng.
 */
"""
import os
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import seaborn as sns

def plot_network_communities(G, communities, title="Network Communities"):
    """
    Trực quan hóa đồ thị mạng lưới, tô màu các node khác nhau để phân biệt các cộng đồng.
    Xuất đồ thị ra file ảnh định dạng PNG.
    
    Args:
        G (networkx.Graph): Đồ thị cần vẽ.
        communities (list of sets): Cấu trúc cộng đồng đã được phân chia.
        title (str): Tiêu đề của biểu đồ và cũng là tên file ảnh lưu ra.
    """
    # Khởi tạo một hình vẽ với kích thước 10x8 inch
    plt.figure(figsize=(10, 8))
    
    # Tính toán vị trí các node trên mặt phẳng 2D dùng thuật toán lực đẩy (spring_layout) để mạng không bị rối
    pos = nx.spring_layout(G, seed=42)
    
    try:
        # Lấy bảng màu 'tab20' (có 20 màu khác biệt) cho các version matplotlib mới
        cmap = plt.colormaps['tab20']
    except AttributeError:
        # Tương thích ngược lấy bảng màu 'tab20' cho các version matplotlib cũ hơn
        cmap = plt.cm.get_cmap('tab20')
    
    # Lặp qua từng cộng đồng được phát hiện
    for i, comm in enumerate(communities):
        # Chọn màu sắc cho cộng đồng này dựa trên index i chia lấy dư cho 20
        color = cmap(i % 20)
        
        # Vẽ các node thuộc cộng đồng hiện tại, gán màu và đặt độ trong suốt alpha=0.8
        nx.draw_networkx_nodes(G, pos, nodelist=list(comm), node_color=[color], node_size=300, alpha=0.8)
    
    # Vẽ toàn bộ các cạnh (mối quan hệ) của đồ thị với độ trong suốt 0.5 để làm nền
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    
    # Vẽ nhãn (ID) cho từng node bằng chữ màu đen
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")
    
    # Đặt tiêu đề cho đồ thị
    plt.title(title)
    
    # Tắt hiển thị khung trục tọa độ (axis) để đồ thị đẹp hơn
    plt.axis('off')
    
    # Tự động căn chỉnh các thành phần cho vừa vặn với kích thước hình
    plt.tight_layout()
    
    # Lưu hình ảnh ra file, thay thế khoảng trắng trong tiêu đề bằng dấu gạch dưới và lưu vào folder result
    file_path = f"result/{title.replace(' ', '_')}.png"
    plt.savefig(file_path)
    
    # Đóng đồ thị để giải phóng bộ nhớ
    plt.close()
    
    # In thông báo xác nhận đã xuất ảnh
    print(f"[Huy] Đã xuất biểu đồ mạng lưới: {file_path}")

def plot_modularity_trend(csv_file):
    """
    Vẽ biểu đồ đường xu hướng thể hiện sự biến thiên điểm chất lượng cộng đồng (Modularity)
    khi tỷ lệ cắt tỉa các node VIP tăng dần. Đọc dữ liệu từ file CSV.
    
    Args:
        csv_file (str): Đường dẫn tới file CSV chứa kết quả thực nghiệm.
    """
    # Đọc dữ liệu từ file CSV vào một DataFrame của thư viện pandas
    df = pd.read_csv(csv_file)
    
    # Tạo ra một hình vẽ chứa 2 biểu đồ con (subplots) đặt ngang nhau, chung trục Y
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)
    
    # --- BIỂU ĐỒ 1: THUẬT TOÁN LOUVAIN ---
    # Lọc data của thuật toán Louvain, vẽ đường thẳng (lineplot) với trục X là % xóa, Y là Modularity
    # Đổi màu đường thẳng (hue) theo từng loại Centrality
    sns.lineplot(data=df[df['Algorithm'] == 'Louvain'], 
                 x='Removal_Percentage', y='Modularity', hue='Centrality_Metric', 
                 markers=True, dashes=False, ax=axes[0])
    
    # Đặt các cấu hình cho biểu đồ 1 (Tiêu đề, Nhãn trục X, Y và hiển thị lưới)
    axes[0].set_title('Thuật toán Louvain', fontsize=14)
    axes[0].set_xlabel('Tỷ lệ xóa Node VIP (%)')
    axes[0].set_ylabel('Điểm Modularity (Q)')
    axes[0].grid(True, linestyle='--', alpha=0.7)
    
    # --- BIỂU ĐỒ 2: THUẬT TOÁN GIRVAN-NEWMAN ---
    # Tương tự biểu đồ 1 nhưng lọc data của thuật toán Girvan-Newman để hiển thị ở khung bên phải
    sns.lineplot(data=df[df['Algorithm'] == 'Girvan-Newman'], 
                 x='Removal_Percentage', y='Modularity', hue='Centrality_Metric', 
                 markers=True, dashes=False, ax=axes[1])
    
    # Đặt cấu hình cho biểu đồ 2 (Tiêu đề, Nhãn trục X, bỏ nhãn trục Y vì chung với biểu đồ 1, lưới)
    axes[1].set_title('Thuật toán Girvan-Newman', fontsize=14)
    axes[1].set_xlabel('Tỷ lệ xóa Node VIP (%)')
    axes[1].set_ylabel('')
    axes[1].grid(True, linestyle='--', alpha=0.7)
    
    # Đặt tiêu đề lớn (suptile) cho toàn bộ bức hình chứa 2 biểu đồ con
    plt.suptitle('Xu hướng sụt giảm Modularity khi loại bỏ VIP Nodes', fontsize=16, fontweight='bold')
    
    # Căn chỉnh bố cục để không bị chữ đè lên nhau
    plt.tight_layout()
    
    # Xuất toàn bộ biểu đồ xu hướng ra file ảnh chung trong folder result
    file_path = "result/Modularity_Trend.png"
    plt.savefig(file_path)
    
    # Đóng đồ thị giải phóng tài nguyên
    plt.close()
    
    # In ra thông báo hoàn tất
    print(f"[Huy] Đã xuất biểu đồ xu hướng: {file_path} (đã tách 2 khung)")
