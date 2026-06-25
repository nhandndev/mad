# TÀI LIỆU BÁO CÁO CÁ NHÂN: SIU (COMMUNITY DETECTOR)

**Mục tiêu nhiệm vụ:**
Đóng vai trò là "bộ não" phân tích của dự án. File của mình nhận vào các đồ thị (đã bị khuyết) từ Trung, sau đó chạy thuật toán phân cụm để xem mạng lưới lúc này bị vỡ ra thành bao nhiêu nhóm, và tính điểm chất lượng chia nhóm (Modularity Q).

**Chi tiết thuật toán và mã nguồn đã triển khai:**
Trong file `community_detector.py`, mình triển khai 2 thuật toán Clustering kinh điển:

1. **Thuật toán Louvain (`detect_louvain`):**
   - Mình gọi hàm `nx.community.louvain_communities(G)`.
   - **Bản chất thuật toán:** Louvain hoạt động theo hướng "từ dưới lên" (bottom-up). Ban đầu nó coi mỗi node là 1 cộng đồng. Sau đó, nó thử ghép node này vào cộng đồng của hàng xóm, nếu việc ghép này làm tăng điểm Modularity Q thì nó giữ lại. Quá trình này lặp lại đến khi Modularity không thể tăng thêm.
   - Ưu điểm: Cực kỳ nhanh, phù hợp mạng lưới cực lớn.

2. **Thuật toán Girvan-Newman (`detect_girvan_newman`):**
   - Khác với Louvain, GN hoạt động "từ trên xuống" (top-down). Nó tính *Edge Betweenness* (Cạnh nằm trên nhiều đường đi nhất) rồi lần lượt cắt bỏ các cạnh đó. Mạng lưới sẽ từ từ đứt ra thành các cụm rời rạc.
   - Mã nguồn của GN trả về một dạng Generator (iterator), do đó mình dùng lệnh `next(comp)` để lấy cấu trúc chia cụm ở phân cấp (level) đầu tiên ngay khi mạng lưới vừa bị chẻ đôi.

3. **Tính Modularity (Q) và Đo thời gian:**
   - Với mọi đầu ra, mình đều đưa qua hàm `nx.community.modularity(G, communities)` để lấy điểm số Q. Q nằm trong khoảng [-0.5, 1]. Q càng cao nghĩa là các liên kết nội bộ trong cộng đồng rất đặc, còn liên kết ra ngoài cộng đồng rất thưa. 
   - Đồng thời, mình dùng thư viện `time` chèn `time.time()` vào đầu và cuối thuật toán để xuất ra `exec_time` (thời gian thực thi).

**Đóng góp cho hệ thống:**
Code của mình trả về chính xác 3 giá trị `(communities, modularity, exec_time)`. Đây chính là "trái tim" của số liệu, giúp tạo ra các con số biến thiên về Modularity để Nhân lưu vào file CSV.
