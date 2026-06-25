# TÀI LIỆU BÁO CÁO CÁ NHÂN: TRUNG (CENTRALITY FILTER)

**Mục tiêu nhiệm vụ:**
Chấm điểm tầm quan trọng (VIP) của từng Node trong mạng lưới dựa trên nền tảng toán học, và thực hiện việc giả lập "tấn công mạng" bằng cách xóa đi một tỷ lệ phần trăm các Node VIP này.

**Chi tiết thuật toán và mã nguồn đã triển khai:**
Trong file `centrality_filter.py`, mình đảm nhận 2 trọng trách:

1. **Hàm `calculate_centralities(G)`:**
   - Hàm này nhận đồ thị từ Chương, sau đó áp dụng 3 thuật toán tính Centrality của NetworkX lên toàn bộ Node.
   - **Degree Centrality:** Đo số kết nối trực tiếp. Node nào có nhiều cạnh nối nhất thì điểm cao nhất.
   - **Closeness Centrality:** Đo độ dài đường đi ngắn nhất trung bình từ Node đó đến tất cả Node khác. Node nào nằm ở "trung tâm hình học" của mạng lưới sẽ có điểm cao vì thông tin đi từ nó phát tán ra toàn mạng rất nhanh.
   - **Betweenness Centrality:** Đo xem Node đó nằm trên bao nhiêu đường đi ngắn nhất giữa các cặp Node khác. Node nào là "cây cầu duy nhất" nối 2 quần thể sẽ có Betweenness cực cao.
   - Kết quả trả về là một `dictionary` gộp chứa đầy đủ điểm số.

2. **Hàm `remove_top_vip_nodes(G, centrality_dict, percentage)`:**
   - Đây là lõi xử lý giả lập phá vỡ mạng.
   - Đầu tiên, mình **bắt buộc phải clone (copy)** đồ thị gốc bằng `G.copy()` để tránh tham chiếu bộ nhớ làm hỏng đồ thị ban đầu của các vòng lặp khác.
   - Mình tính số lượng Node cần xóa: `num_to_remove = int(len(G) * percentage)`. (Ví dụ đồ thị 34 node, cắt 10% tức là lấy 3 node đầu).
   - Sử dụng Python Dictionary Sorting `sorted(..., key=lambda x: x[1], reverse=True)` để xếp hạng giảm dần theo điểm Centrality.
   - Dùng lệnh `G_filtered.remove_nodes_from()` để chặt đứt các node này khỏi đồ thị.

**Đóng góp cho hệ thống:**
Nhờ module này, dự án mới tạo ra được dữ liệu đối chứng. Mình đã biến đồ thị nguyên vẹn thành các đồ thị bị khuyết ở những vị trí trọng yếu, cung cấp đúng nguyên liệu để Siu và Nhân test sự vỡ vụn của cộng đồng.
