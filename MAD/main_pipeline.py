import sys
import codecs

# Đoạn code ép kiểu encoding stdout về UTF-8 để hiển thị tiếng Việt không bị lỗi trong Terminal Windows
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

import pandas as pd
from data_loader import load_karate_club
from centrality_filter import calculate_centralities, remove_top_vip_nodes
from community_detector import detect_louvain, detect_girvan_newman
from visualizer import plot_network_communities, plot_modularity_trend

def run_experiment():
    """
    Đường ống thực nghiệm (Pipeline) chính điều phối toàn bộ chương trình.
    Quy trình: 
      1. Nạp dữ liệu gốc.
      2. Tính toán điểm centrality cho toàn mạng lưới.
      3. Lần lượt xóa dần node VIP theo từng loại centrality với tỷ lệ từ 0% đến 20%.
      4. Ở mỗi bước cắt tỉa, chạy 2 thuật toán Louvain và Girvan-Newman để tìm cộng đồng.
      5. Ghi lại kết quả (Thời gian, điểm Modularity) ra file CSV.
      6. Xuất các đồ thị minh họa cho việc mạng lưới bị đứt gãy.
    """
    # Bắt đầu chạy hệ thống
    print("=== BẮT ĐẦU ĐƯỜNG ỐNG THỰC NGHIỆM TỰ ĐỘNG ===")
    
    # --- BƯỚC 1: NẠP DỮ LIỆU ---
    # Nạp mạng lưới Karate Club vào biến G
    G = load_karate_club()
    
    # Chạy thử Louvain trên mạng gốc chưa bị cắt tỉa
    init_comms, _, _ = detect_louvain(G)
    
    # Xuất ảnh mạng lưới gốc ở trạng thái nguyên bản
    plot_network_communities(G, init_comms, "Karate_Club_Original")
    
    # --- BƯỚC 2: TÍNH TOÁN CENTRALITY ---
    # Tính các chỉ số trung tâm (Degree, Closeness, Betweenness) cho đồ thị gốc
    centralities = calculate_centralities(G)
    
    # Định nghĩa danh sách các chỉ số cần test
    metrics = ['degree', 'closeness', 'betweenness']
    
    # Định nghĩa các tỷ lệ phần trăm xóa node (0%, 5%, 10%, 15%, 20%)
    removal_percentages = [0.0, 0.05, 0.10, 0.15, 0.20]
    
    # Khởi tạo danh sách rỗng để lưu trữ các số liệu đo lường ở mỗi vòng lặp
    results = []
    
    # --- BƯỚC 3: CHẠY THỰC NGHIỆM VÀ ĐO ĐẠC ---
    # Lặp qua từng loại chỉ số centrality
    for metric in metrics:
        
        # Với mỗi loại, lặp qua từng mức tỷ lệ phần trăm xóa
        for p in removal_percentages:
            
            # Xóa top p% node VIP dựa vào bảng xếp hạng của chỉ số 'metric' đang xét
            G_filtered = remove_top_vip_nodes(G, centralities[metric], p)
            
            # Nếu xóa xong đồ thị bị hỏng hoàn toàn (mất sạch cạnh nối), bỏ qua việc đo đạc
            if G_filtered.number_of_edges() == 0:
                continue
                
            # -- Thuật toán LOUVAIN --
            # Dò tìm cộng đồng trên mạng lưới đã bị sứt mẻ này bằng Louvain
            comms_l, mod_l, time_l = detect_louvain(G_filtered)
            
            # Lưu lại bộ thông số của Louvain vào list results (Dùng cho vẽ biểu đồ sau)
            results.append({
                'Centrality_Metric': metric.capitalize(), # Tên chỉ số (Viết hoa chữ đầu)
                'Removal_Percentage': p * 100,            # Đổi % ra số tròn (VD: 0.1 -> 10)
                'Algorithm': 'Louvain',                   # Tên thuật toán
                'Modularity': mod_l,                      # Điểm chất lượng
                'Execution_Time': time_l                  # Thời gian chạy
            })
            
            # -- Thuật toán GIRVAN-NEWMAN --
            # Dò tìm cộng đồng tương tự nhưng bằng Girvan-Newman
            comms_gn, mod_gn, time_gn = detect_girvan_newman(G_filtered)
            
            # Lưu lại bộ thông số của Girvan-Newman vào list
            results.append({
                'Centrality_Metric': metric.capitalize(),
                'Removal_Percentage': p * 100,
                'Algorithm': 'Girvan-Newman',
                'Modularity': mod_gn,
                'Execution_Time': time_gn
            })
            
            # -- TRỰC QUAN HÓA SỰ ĐỨT GÃY --
            # Đặc biệt lấy mốc xóa 10% (0.10) làm đại diện để vẽ ảnh đồ thị bị phá hỏng cho cả 3 chỉ số
            if p == 0.10:
                # Xuất ảnh mạng lưới bị cắt 10% (VD: Karate_Club_Removed_10pct_Degree.png)
                plot_network_communities(G_filtered, comms_l, f"Karate_Club_Removed_10pct_{metric.capitalize()}")
    
    # --- BƯỚC 4: LƯU KẾT QUẢ RA FILE ---
    # Chuyển đổi danh sách kết quả (list of dicts) sang định dạng DataFrame của Pandas
    df = pd.DataFrame(results)
    csv_filename = "experimental_results.csv"
    
    # Ghi dữ liệu DataFrame ra file CSV, bỏ đánh chỉ mục (index=False)
    df.to_csv(csv_filename, index=False)
    print(f"[Nhân] Đã lưu số liệu thực nghiệm vào {csv_filename}")
    
    # --- BƯỚC 5: VẼ BIỂU ĐỒ XU HƯỚNG ---
    # Gọi hàm của Huy bên module visualizer, đưa file CSV vào để vẽ 2 đường xu hướng
    plot_modularity_trend(csv_filename)
    
    # Kết thúc đường ống
    print("=== HOÀN THÀNH THỰC NGHIỆM ===")

# Đảm bảo hàm run_experiment() chỉ chạy khi file main_pipeline.py được thực thi trực tiếp 
if __name__ == "__main__":
    run_experiment()
