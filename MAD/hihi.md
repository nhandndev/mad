Thành viên
Vai trò chính
File Code phụ trách
Nhiệm vụ chuẩn bị & Phản biện (Q&A)
Nhân (Leader)
Điều phối chung & Quản lý Đường ống
main_pipeline.py
- Thuyết trình phần Mở đầu & Quản lý đường ống.

- Hiểu cách kết nối các file đơn lẻ thành một vòng lặp thực nghiệm khép kín.

- Chủ động điều phối câu hỏi của Thầy/Cô cho các thành viên.
Khoa
Chuyên gia Toán học
Không có (Phụ trách Lý thuyết chính)
- Thuyết trình phần Cơ sở Toán học (3 chỉ số Centrality & Modularity ).

- Học thuộc lòng định nghĩa bản chất và công thức của từng chỉ số.

- Gánh các câu hỏi nặng về lý thuyết đồ thị từ Hội đồng.
Chương
Kỹ sư Dữ liệu
data_loader.py
- Thuyết trình phần Nạp dữ liệu thực nghiệm.

- Hiểu rõ bản chất mạng thực tế Karate Club và mạng mô phỏng Barabási-Albert (Scale-free).

- Giải thích lý do chọn hai tập dữ liệu này.
Chung
Kỹ sư Tiền xử lý
centrality_filter.py
- Thuyết trình phần Bộ lọc Node VIP.

- Giải thích thuật toán sắp xếp và cắt tỉa (remove)  các node có điểm trung tâm cao nhất.

- Trả lời câu hỏi về cách loại bỏ node mà không làm sập chỉ mục đồ thị.
Siêu
Chuyên gia Thuật toán
community_detector.py
- Thuyết trình phần Thuật toán Phát hiện Cộng đồng.

- So sánh triệt để hai cơ chế cực kỳ quan trọng: Louvain (Bottom-up) và Girvan-Newman (Top-down).

- Giải thích độ phức tạp thuật toán và cách đo thời gian thực thi.
Huy
Chuyên gia Trực quan & Biện luận
visualizer.py
- Thuyết trình phần Vẽ biểu đồ & Kết luận khoa học.

- Làm chủ cách giải thích 2 loại biểu đồ: Biểu đồ phân rã mạng lưới và Biểu đồ đường xu hướng Modularity.

- Đưa ra đề xuất thực tế ứng dụng nghiên cứu.

---

## 🎯 GIẢI THÍCH CODE CHI TIẾT DÀNH CHO TỪNG THÀNH VIÊN
*(Các bạn sử dụng phần này để vừa trình chiếu slide, vừa mở code lên giải thích cho thầy cô và các bạn trong lớp hiểu phần việc của mình)*

### 1. Nhân (Leader) - `main_pipeline.py`
**Đoạn code cần tập trung:** Hàm `run_experiment()`
- **Giải thích:** Đây là "trái tim" của toàn bộ dự án, nơi kết nối tất cả các module đơn lẻ lại với nhau thành một vòng lặp tự động.
  - **Bước 1:** Gọi `load_karate_club()` để nạp đồ thị mạng lưới.
  - **Bước 2:** Gọi `calculate_centralities(G)` để tính 3 chỉ số trung tâm (Degree, Closeness, Betweenness).
  - **Bước 3 (Quan trọng):** Chạy 2 vòng lặp `for` lồng nhau. Vòng ngoài duyệt qua từng loại Centrality, vòng trong duyệt qua các mức tỷ lệ xóa node (0%, 5%, 10%...). Tại mỗi bước, gọi `remove_top_vip_nodes` để tạo ra một mạng lưới đã bị "tấn công" (xóa node quan trọng).
  - **Bước 4:** Đưa đồ thị đã bị xóa node vào 2 thuật toán `detect_louvain` và `detect_girvan_newman` để gom cụm cộng đồng.
  - **Bước 5:** Lưu toàn bộ thông số (Thời gian, Modularity) vào biến `results`, xuất ra file `.csv` và gọi hàm vẽ biểu đồ của Huy.

### 2. Khoa (Chuyên gia Toán học)
*(Không phụ trách code)*
- **Nhiệm vụ khi thuyết trình:** Khoa không cần giải thích code cụ thể. Tuy nhiên, khi Nhân hoặc Chung mở code đến đoạn `calculate_centralities` (tính Degree, Closeness, Betweenness) hoặc lúc Siêu nhắc đến điểm `Modularity (Q)`, Khoa sẽ chịu trách nhiệm giải thích công thức toán học và bản chất lý thuyết đằng sau các hàm thư viện đó.

### 3. Chương (Kỹ sư Dữ liệu) - `data_loader.py`
**Đoạn code cần tập trung:** Hàm `load_karate_club()` và `generate_facebook_network()`
- **Giải thích:** 
  - `load_karate_club()`: Dùng thư viện NetworkX (`nx.karate_club_graph()`) để lấy bộ dataset chuẩn mực. Đây là mạng lưới thực tế của một câu lạc bộ võ thuật, dùng làm baseline.
  - `generate_facebook_network()`: Dùng hàm `nx.barabasi_albert_graph`. Chương cần giải thích rằng đây là thuật toán sinh đồ thị mô phỏng các mạng xã hội ngoài đời thực theo nguyên tắc "Rich-get-richer" (Nút nào càng có nhiều liên kết thì càng dễ thu hút liên kết mới trong tương lai), tạo ra đồ thị dạng Scale-free.

### 4. Chung (Kỹ sư Tiền xử lý) - `centrality_filter.py`
**Đoạn code cần tập trung:** Hàm `calculate_centralities()` và `remove_top_vip_nodes()`
- **Giải thích:** 
  - `calculate_centralities`: Gọi các hàm có sẵn của NetworkX (`degree_centrality`, `closeness_centrality`, `betweenness_centrality`) để chấm điểm "tầm quan trọng" cho tất cả các node.
  - `remove_top_vip_nodes`: Đầu tiên, tính số lượng node cần xóa dựa trên tham số `percentage`. Sau đó, dùng lệnh `sorted(..., reverse=True)` để sắp xếp các node theo điểm từ cao xuống thấp. Cuối cùng, dùng danh sách node VIP đó gọi lệnh `G_filtered.remove_nodes_from()` để loại bỏ chúng khỏi mạng lưới. Hành động này mô phỏng sự cố đứt gãy mạng hoặc việc các cá nhân có ảnh hưởng rời bỏ cộng đồng.

### 5. Siêu (Chuyên gia Thuật toán) - `community_detector.py`
**Đoạn code cần tập trung:** Hàm `detect_louvain()` và `detect_girvan_newman()`
- **Giải thích:** Cả hai hàm đều dùng để phát hiện cộng đồng và đo đạc thời gian (`time.time()`).
  - `detect_louvain`: Gọi `nx.community.louvain_communities(G)`. Siêu cần nhấn mạnh đây là thuật toán **Bottom-up** (từ dưới lên), gom cụm các node lân cận lại với nhau để tối ưu điểm Modularity. Thuật toán này chạy cực kỳ nhanh.
  - `detect_girvan_newman`: Gọi `nx.community.girvan_newman(G)`. Nhấn mạnh đây là thuật toán **Top-down** (từ trên xuống), liên tục tìm và chặt đứt các "cây cầu" (cạnh có Edge Betweenness cao nhất) để chia tách mạng lưới. Hàm này trả về một generator, ta dùng `next(comp)` để lấy kết quả phân tách ở bước đầu tiên. Thuật toán này chậm hơn Louvain rất nhiều.
  - Cuối cùng, cả hai hàm đều dùng `nx.community.modularity()` để tính điểm chất lượng cộng đồng.

### 6. Huy (Chuyên gia Trực quan) - `visualizer.py`
**Đoạn code cần tập trung:** Hàm `plot_network_communities()` và `plot_modularity_trend()`
- **Giải thích:** 
  - `plot_network_communities()`: Sử dụng Matplotlib và lệnh `nx.spring_layout` (giúp tự động dàn trải các node ra không gian sao cho không bị rối). Hàm lặp qua từng nhóm cộng đồng và tô cho mỗi nhóm một màu khác nhau bằng bảng màu `tab20`.
  - `plot_modularity_trend()`: Sử dụng thư viện Seaborn (`sns.lineplot`) để đọc file CSV kết quả, sau đó vẽ ra 2 biểu đồ đường song song (`subplots`). Trục X là phần trăm xóa node, trục Y là điểm Modularity, với các đường line có màu khác nhau đại diện cho từng loại Centrality. Biểu đồ này dùng để minh họa trực quan sự sụt giảm sức chịu đựng của mạng lưới.

---

## 🖼️ HƯỚNG DẪN THUYẾT TRÌNH CÁC FILE ẢNH KẾT QUẢ
*(Toàn bộ các file ảnh này sẽ do **Huy** thuyết trình chính, vì Huy giữ vai trò "Chuyên gia Trực quan & Biện luận". Tuy nhiên, **Chung** và **Siêu** có thể đứng cạnh hỗ trợ nếu hội đồng hỏi xoáy vào thuật toán)*

### 1. File `Karate_Club_Original.png` (Mạng lưới gốc)
- **Người thuyết trình:** Huy
- **Cách nói:** "Thưa thầy/cô, đây là trực quan hóa của mạng lưới Karate Club ở trạng thái nguyên bản gốc (chưa bị xóa node nào). Các chấm tròn là các thành viên, các đường nối là mối quan hệ. Thuật toán đã tự động gom cụm và tô các màu sắc khác nhau để thể hiện các nhóm (cộng đồng) tự nhiên có trong mạng lưới này."

### 2. Nhóm 3 file đồ thị bị tấn công/cắt tỉa 10%
*(Bao gồm: `Karate_Club_Removed_10pct_Degree.png`, `Karate_Club_Removed_10pct_Closeness.png`, `Karate_Club_Removed_10pct_Betweenness.png`)*
- **Người thuyết trình:** Huy (mời **Chung** hỗ trợ nếu cần)
- **Cách nói:** "Tiếp theo, nhóm tiến hành thực nghiệm 'tấn công' cấu trúc mạng bằng cách xóa đi 10% các node VIP nhất (những node quan trọng nhất). Thầy/cô có thể so sánh 3 hình ảnh này để thấy mức độ thiệt hại:
  - Khi xóa theo **Degree** (những người quen nhiều nhất), mạng lưới có đứt gãy nhưng vẫn còn giữ được hình thái.
  - Nhưng khi xóa theo **Betweenness** (những 'cây cầu' nối các nhóm với nhau), mạng lưới ngay lập tức bị vỡ vụn thành những cụm nhỏ lẻ tẻ, cô lập hoàn toàn. Điều này minh chứng trực quan rằng: phá hủy các 'cây cầu' Betweenness là cách làm sập một mạng lưới nhanh nhất."

### 3. File `Modularity_Trend.png` (Biểu đồ xu hướng tổng kết)
- **Người thuyết trình:** Huy (mời **Siêu** hỗ trợ phần giải thích điểm Modularity nếu cần)
- **Cách nói:** "Cuối cùng, để có cái nhìn khoa học bằng con số, đây là biểu đồ đường xu hướng tổng kết lại toàn bộ thực nghiệm. 
  - Trục ngang (X) là tỷ lệ phần trăm node bị xóa (từ 0 đến 20%). Trục dọc (Y) là điểm Modularity (điểm Q càng cao thì cộng đồng càng bền vững).
  - Có 2 biểu đồ so sánh giữa 2 thuật toán Louvain và Girvan-Newman.
  - Nhìn vào đồ thị, thầy/cô có thể thấy rõ đường dao động của chỉ số **Betweenness** (và/hoặc **Degree**) thường sụt giảm dốc nhất và nhanh nhất. 
  - **Kết luận rút ra:** Việc phát hiện và bảo vệ (hoặc tấn công) các node có chỉ số Betweenness Centrality cao mang ý nghĩa sống còn đối với độ bền vững của cấu trúc cộng đồng trong mạng xã hội."
