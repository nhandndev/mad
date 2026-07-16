# KỊCH BẢN THUYẾT TRÌNH TOÀN BỘ DỰ ÁN (PRESENTATION SCRIPT)

Kịch bản này được thiết kế để nhóm 6 người trình bày một cách trơn tru, logic, nối tiếp nhau không bị vấp. Mỗi người chỉ cần nói đúng phần của mình.

---

### 1. MỞ ĐẦU (Nhân hoặc Khoa)
**Lời thoại:**
"Chào thầy và các bạn. Hôm nay, nhóm chúng em xin trình bày đề tài nghiên cứu: 'Graph Centrality Metrics for Social Network Community Detection'. Trong mạng xã hội, có những người dùng VIP (Hubs) có sức ảnh hưởng cực lớn. Câu hỏi đặt ra là: Nếu chúng ta 'xóa' hay 'chặn' những người dùng VIP này, thì cấu trúc cộng đồng của mạng xã hội sẽ bị phá vỡ ra sao? Nhóm chúng em đã thiết kế một pipeline thực nghiệm tự động để đo lường điều đó."

### 2. LÝ THUYẾT TOÁN HỌC (Khoa)
**Lời thoại:**
"Để giải quyết bài toán, trước tiên chúng ta phải định nghĩa thế nào là VIP. Nhóm em dùng 3 thước đo (Centrality):
1. **Degree Centrality:** VIP vì có nhiều bạn bè trực tiếp nhất.
2. **Closeness Centrality:** VIP vì có khoảng cách lan truyền thông tin tới người khác ngắn nhất.
3. **Betweenness Centrality:** VIP vì nắm giữ vị trí 'cầu nối' giao lộ thông tin giữa các nhóm khác nhau.
Và để đánh giá xem cộng đồng có bị phá vỡ hay không, nhóm em dùng điểm **Modularity Q**. Q càng cao (gần 1) thì cộng đồng càng chia rõ ràng; Q lao dốc nghĩa là cấu trúc mạng đã vỡ vụn."

### 3. NẠP DỮ LIỆU (Chương)
**Lời thoại:**
"Về mặt dữ liệu thực nghiệm, em phụ trách file `data_loader.py`. Nhóm không dùng file tĩnh mà gọi trực tiếp dataset Zachary's Karate Club (34 nodes) có sẵn trong NetworkX để làm baseline. Đồng thời, em dùng thuật toán Barabási-Albert để mô phỏng một mạng lưới 300 nodes mang đặc tính Scale-free của Facebook. Điều này giúp dữ liệu của nhóm luôn khách quan và chuẩn mực."

### 4. BỘ LỌC NODE VIP (Trung)
**Lời thoại:**
"Tiếp nối phần dữ liệu của Chương, em viết file `centrality_filter.py`. File của em sẽ quét toàn mạng, chấm điểm 3 chỉ số Centrality (Degree, Closeness, Betweenness) cho từng node. Sau đó, em viết hàm tự động sắp xếp các Node từ cao xuống thấp và cắt bỏ (remove) 0%, 5%, 10%, 15% và 20% các Node đứng top đầu. Đồ thị sau khi bị cắt tỉa sẽ được chuyển sang cho Siu xử lý."

### 5. THUẬT TOÁN PHÁT HIỆN CỘNG ĐỒNG (Siu)
**Lời thoại:**
"Với đồ thị đã bị 'thương tổn' từ Trung, file `community_detector.py` của em sẽ cho chạy 2 thuật toán là Louvain và Girvan-Newman. 
- **Louvain:** là thuật toán Heuristic, tốc độ rất nhanh, cố gắng tối ưu hóa hàm Modularity ở từng cụm cục bộ.
- **Girvan-Newman:** là thuật toán chặt đứt các cạnh có 'Edge Betweenness' cao nhất từ từ.
Sau khi phân cụm xong, em sẽ tính điểm Modularity Q hiện tại và ghi nhận thời gian chạy để làm data đánh giá."

### 6. QUẢN LÝ ĐƯỜNG ỐNG (Nhân)
**Lời thoại:**
"Để các file trên chạy được, em đóng vai trò điều phối bằng file `main_pipeline.py`. Em tạo ra các vòng lặp lồng nhau: duyệt qua 3 loại Centrality, duyệt qua 5 mức độ % loại bỏ, ném đồ thị vào cho Siu tính toán, thu thập toàn bộ dữ liệu (như thuật toán, điểm Q, thời gian) và xuất thành 1 file `experimental_results.csv` tự động."

### 7. TRỰC QUAN HÓA & KẾT LUẬN (Huy)
**Lời thoại:**
"Từ file CSV của Nhân, em dùng file `visualizer.py` để vẽ ra các biểu đồ bằng thư viện Seaborn và Matplotlib. Nhìn vào biểu đồ đường xu hướng (chỉ vào ảnh Modularity Trend), thầy/các bạn có thể thấy rõ:
Khi xóa các node có **Degree cao**, Modularity chỉ giảm nhẹ. 
Nhưng khi xóa khoảng 10-15% node có **Betweenness cao**, đồ thị đường thẳng đứng đâm chui xuống đáy. 
=> **Kết luận:** Những người có lượng bạn bè khủng (Degree cao) không quan trọng bằng những người nắm giữ vị trí cầu nối (Betweenness cao). Nếu đánh sập các 'cầu nối' này, mạng lưới sẽ phân rã thành vô số hòn đảo cô lập, cấu trúc cộng đồng hoàn toàn sụp đổ. Cảm ơn thầy và các bạn đã lắng nghe!"
