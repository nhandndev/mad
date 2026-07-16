# BÁO CÁO NGHIÊN CỨU KHOA HỌC RBL
**Đề tài:** Graph Centrality Metrics for Social Network Community Detection
**Nhóm thực hiện:** Khoa, Chương, Trung, Siu, Huy, Nhân

---

#### CHƯƠNG 1: MỞ ĐẦU
Trong kỷ nguyên số, các mạng xã hội (Social Networks) phát triển mạnh mẽ và cấu trúc của chúng ngày càng trở nên phức tạp. Việc phát hiện các "cộng đồng" (Community Detection) bên trong mạng lưới giúp hiểu rõ cách thông tin lan truyền và sự hình thành các nhóm có cùng sở thích. Tuy nhiên, sự xuất hiện của các "Node VIP" (người dùng có ảnh hưởng lớn, Hubs) thường làm lu mờ ranh giới giữa các cộng đồng tự nhiên. Nghiên cứu này nhằm mục đích phân tích tác động của việc cắt bỏ các Node VIP (dựa trên các chỉ số Centrality khác nhau) đối với chất lượng phân hoạch cộng đồng, được đo lường bằng điểm Modularity Q.

#### CHƯƠNG 2: LÝ THUYẾT TOÁN HỌC
Để đánh giá tầm quan trọng của các Node trong đồ thị $G = (V, E)$, nhóm sử dụng ba chỉ số trung tâm (Centrality Metrics) sau:

1. **Degree Centrality ($C_D$):** Đo lường số lượng liên kết trực tiếp của một đỉnh.
   $$ C_D(v) = \frac{deg(v)}{|V| - 1} $$

2. **Closeness Centrality ($C_C$):** Đo lường khoảng cách trung bình ngắn nhất từ đỉnh $v$ đến tất cả các đỉnh khác. 
   $$ C_C(v) = \frac{|V| - 1}{\sum_{u \neq v} d(v, u)} $$
   (Trong đó $d(v,u)$ là đường đi ngắn nhất từ $v$ đến $u$).

3. **Betweenness Centrality ($C_B$):** Đo lường tần suất đỉnh $v$ nằm trên đường đi ngắn nhất giữa hai đỉnh bất kỳ khác.
   $$ C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}} $$
   ($\sigma_{st}$ là tổng số đường đi ngắn nhất, $\sigma_{st}(v)$ là số đường đi đi qua $v$).

Chất lượng của thuật toán phát hiện cộng đồng được đánh giá qua **Modularity (Q)**:
$$ Q = \frac{1}{2m} \sum_{i,j} \left[ A_{ij} - \frac{k_i k_j}{2m} \right] \delta(c_i, c_j) $$
Giá trị $Q$ càng tiệm cận 1, cấu trúc cộng đồng càng phân minh rõ nét.

#### CHƯƠNG 3: PHƯƠNG PHÁP THỰC NGHIỆM
- **Dữ liệu thực nghiệm:** Mạng Karate Club (34 đỉnh, 78 cạnh) và đồ thị Barabási-Albert giả lập.
- **Biến độc lập:** Tỷ lệ Node VIP bị loại bỏ ($0\% \rightarrow 20\%$) dựa trên xếp hạng của 3 loại Centrality.
- **Biến phụ thuộc:** Điểm Modularity Q, thời gian thực thi thuật toán (Louvain, Girvan-Newman).
- **Quy trình:**
  1. Tính các chỉ số Centrality cho toàn mạng.
  2. Ở mỗi vòng lặp, xóa $X\%$ số Node có điểm Centrality cao nhất.
  3. Áp dụng Louvain/Girvan-Newman trên đồ thị khuyết và tính lại điểm Q.
  4. Trực quan hóa và đánh giá so sánh.

#### CHƯƠNG 4: PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM
Sau quá trình chạy thực nghiệm tự động bằng hệ thống `main_pipeline.py`, nhóm thu được 2 biểu đồ trực quan (Biểu đồ mạng lưới *Karate_Club_Removed_10pct_Betweenness.png* và biểu đồ đường xu hướng *Modularity_Trend.png*) cùng bảng số liệu gốc.

**Phân tích biện luận sắc bén:**
1. **Xu hướng giảm chung của Modularity:** Khi tỷ lệ xóa node tăng lên, điểm Modularity Q nói chung có xu hướng giảm. Điều này cho thấy các Node VIP (dù chiếm thiểu số) đóng vai trò là "chất keo dính" cục bộ giúp định hình cấu trúc topology của mạng lưới.
2. **Sự sụt giảm mạnh nhất thuộc về Betweenness Centrality:** Dựa trên biểu đồ đường xu hướng, khi xóa đi 10-15% node có chỉ số *Betweenness* cao nhất, điểm Q sụt giảm thẳng đứng và cấu trúc đồ thị bị vỡ vụn. 
   - *Giải thích giải phẫu học mạng lưới:* Các node có Betweenness cao đóng vai trò là **"những cây cầu nối" (Bridges/Brokers)** giao lộ giữa nhiều cụm cộng đồng khác nhau, thay vì chỉ đơn thuần là người nổi tiếng cục bộ (như Degree Centrality). Khi ta cắt bỏ các cây cầu này, đồ thị mất đi tính kết nối liên thông toàn cục, phân rã thành các hòn đảo (isolated components) quá nhỏ lẻ. Lúc này, thuật toán Louvain và Girvan-Newman không còn tìm thấy ranh giới cộng đồng đủ dày đặc để tối ưu hóa hàm Modularity, dẫn đến điểm Q lao dốc cực mạnh.
3. **Sự kháng cự của Degree Centrality:** Ngược lại, việc cắt bỏ các node có Degree cao chỉ làm điểm Q giảm nhẹ. Lý do là trong mạng xã hội, các node có Degree cao thường tập trung thành các lõi (Core) đặc trong cùng một cộng đồng. Việc lấy đi 1 vài đỉnh lõi không phá vỡ liên kết của các đỉnh vệ tinh xung quanh (vì chúng có tính redundant - dư thừa liên kết cao), nên cấu trúc cộng đồng vẫn được bảo toàn hình dáng.

#### CHƯƠNG 5: KẾT LUẬN
Đề tài đã triển khai thành công một hệ thống pipeline hoàn chỉnh (Data Loader -> Centrality Filter -> Community Detector -> Visualizer) để nghiên cứu cấu trúc mạng xã hội. Kết quả chứng minh rằng các node mang giá trị **Betweenness Centrality cao** chính là nhược điểm chí mạng (vulnerability) về mặt cấu trúc cộng đồng. Xóa bỏ các node này phá hủy hoàn toàn dòng chảy thông tin và ranh giới cộng đồng tự nhiên. Nghiên cứu cung cấp cơ sở quan trọng cho các ứng dụng thực tế như: ngăn chặn sự lây lan tin giả (bằng cách vô hiệu hóa node Betweenness cao) hoặc thiết kế hệ thống mạng chống chịu lỗi (fault-tolerant systems).
