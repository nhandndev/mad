import sys
import codecs
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

import pandas as pd
from data_loader import load_karate_club
from centrality_filter import calculate_centralities, remove_top_vip_nodes
from community_detector import detect_louvain, detect_girvan_newman
from visualizer import plot_network_communities, plot_modularity_trend

def run_experiment():
    print("=== BẮT ĐẦU ĐƯỜNG ỐNG THỰC NGHIỆM TỰ ĐỘNG ===")
    
    # 1. Nạp dữ liệu
    G = load_karate_club()
    
    # Vẽ mạng ban đầu (Louvain)
    init_comms, _, _ = detect_louvain(G)
    plot_network_communities(G, init_comms, "Karate_Club_Original")
    
    # 2. Tính Centrality
    centralities = calculate_centralities(G)
    metrics = ['degree', 'closeness', 'betweenness']
    removal_percentages = [0.0, 0.05, 0.10, 0.15, 0.20]
    
    results = []
    
    # 3. Chạy thực nghiệm cắt tỉa và đo đạc
    for metric in metrics:
        for p in removal_percentages:
            G_filtered = remove_top_vip_nodes(G, centralities[metric], p)
            
            # Nếu đồ thị bị xóa hết cạnh, bỏ qua tính toán
            if G_filtered.number_of_edges() == 0:
                continue
                
            # Louvain
            comms_l, mod_l, time_l = detect_louvain(G_filtered)
            results.append({
                'Centrality_Metric': metric.capitalize(),
                'Removal_Percentage': p * 100,
                'Algorithm': 'Louvain',
                'Modularity': mod_l,
                'Execution_Time': time_l
            })
            
            # Girvan-Newman
            comms_gn, mod_gn, time_gn = detect_girvan_newman(G_filtered)
            results.append({
                'Centrality_Metric': metric.capitalize(),
                'Removal_Percentage': p * 100,
                'Algorithm': 'Girvan-Newman',
                'Modularity': mod_gn,
                'Execution_Time': time_gn
            })
            
            # Xuất ảnh mạng lưới bị cắt tỉa 10% cho CẢ 3 CHỈ SỐ để so sánh bằng mắt thường
            if p == 0.10:
                plot_network_communities(G_filtered, comms_l, f"Karate_Club_Removed_10pct_{metric.capitalize()}")
    
    # 4. Lưu kết quả ra CSV
    df = pd.DataFrame(results)
    csv_filename = "experimental_results.csv"
    df.to_csv(csv_filename, index=False)
    print(f"[Nhân] Đã lưu số liệu thực nghiệm vào {csv_filename}")
    
    # 5. Gọi Huy vẽ hình xu hướng
    plot_modularity_trend(csv_filename)
    
    print("=== HOÀN THÀNH THỰC NGHIỆM ===")

if __name__ == "__main__":
    run_experiment()
