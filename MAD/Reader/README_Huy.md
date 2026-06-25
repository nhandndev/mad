# TÀI LIỆU BÁO CÁO CÁ NHÂN: HUY (VISUALIZER)

**Mục tiêu nhiệm vụ:**
Biến những con số khô khan trong file CSV và các cấu trúc mảng đa chiều thành hình ảnh trực quan, sắc nét để nhóm chèn vào báo cáo khoa học.

**Chi tiết thuật toán và mã nguồn đã triển khai:**
Trong file `visualizer.py`, mình viết 2 hàm vẽ biểu đồ sử dụng thư viện `matplotlib` và `seaborn`:

1. **Hàm `plot_network_communities(G, communities)`:**
   - Dùng để vẽ bản đồ giải phẫu mạng lưới (Network Topology).
   - Mình sử dụng `nx.spring_layout(G, seed=42)`: Thuật toán mô phỏng lực đẩy lò xo (Force-directed graph drawing). Các node có liên kết với nhau sẽ hút nhau lại, các node không liên kết sẽ đẩy nhau ra xa. Trọng số `seed=42` giúp mỗi lần vẽ, các node sẽ nằm ở cùng một vị trí cố định trên màn hình, không bị xoay vòng lộn xộn.
   - Mình dùng bộ màu `plt.cm.get_cmap('tab20')` cung cấp 20 màu tương phản cao, tự động tô màu các node thuộc cùng 1 cộng đồng (cùng 1 set trong mảng `communities`) bằng chung 1 màu.
   - Hàm này xuất ra các ảnh `.png` để làm minh chứng xem sau khi xóa Node, đồ thị bị đứt gãy như thế nào.

2. **Hàm `plot_modularity_trend(csv_file)`:**
   - Mình sử dụng hàm `read_csv()` của Pandas để đọc cục data khổng lồ do Nhân xuất ra.
   - Sử dụng thư viện **Seaborn** (`sns.lineplot`), mình vẽ biểu đồ xu hướng.
   - Trục X: `Removal_Percentage` (Tỷ lệ bị xóa 0% -> 20%).
   - Trục Y: `Modularity` (Điểm chất lượng cộng đồng).
   - Tham số `hue='Centrality_Metric'` giúp hệ thống tự động tách ra 3 đường line đại diện cho Degree, Closeness, và Betweenness. Tham số `style='Algorithm'` đổi kiểu đường nét (nét đứt, nét liền) để phân biệt giữa thuật toán Louvain và Girvan-Newman.

**Đóng góp cho hệ thống:**
Sản phẩm của module này là linh hồn của phần Phân tích kết quả thực nghiệm. Không có biểu đồ đường Modularity_Trend, nhóm không thể có cơ sở biện luận tại sao Betweenness lại gây sụt giảm Q mạnh nhất. Ảnh độ phân giải cao được căn lề tự động bằng `plt.tight_layout()`.
