# TÀI LIỆU MASTER: HƯỚNG DẪN BẢO VỆ ĐỀ TÀI & DEMO TOÀN TẬP
*Tài liệu này là "Kim chỉ nam" tổng hợp mọi thứ để nhóm tự tin 100% khi lên thuyết trình và trả lời chất vấn (Q&A).*

---

## 1. TỔNG QUAN ĐỀ TÀI (NHỮNG GÌ BẠN ĐANG LÀM?)
- **Mục tiêu:** Chứng minh rằng trong một mạng xã hội, những người làm **"Cầu nối" (Betweenness VIP)** quan trọng đối với cấu trúc cộng đồng hơn rất nhiều so với những người có **"Nhiều bạn bè" (Degree VIP)**. 
- **Cách thức chứng minh:** Ta sẽ sử dụng mạng lưới đồ thị tiêu chuẩn (như Karate Club 34 người hoặc mạng mô phỏng 300 người). Sau đó ta giả lập các cuộc tấn công bằng cách xóa dần 5%, 10%, 15%, 20% những người VIP nhất. Sau mỗi lần xóa, ta dùng thuật toán tìm cộng đồng (Louvain, Girvan-Newman) để đo lại xem mạng lưới còn nguyên vẹn hay đã vỡ nát (thông qua điểm Modularity Q).

---

## 2. CƠ CHẾ HOẠT ĐỘNG CỦA CODE (5 MODULES)
Thầy cô chắc chắn sẽ hỏi: *"Các em đã code như thế nào?"*. Bạn chỉ cần bật thư mục code lên và chỉ vào từng file:
1. **`data_loader.py` (Đọc dữ liệu):** Sử dụng các hàm tự động của NetworkX để nạp dataset chuẩn Zachary's Karate Club (không cần tải file ngoài cực nhọc) để làm Benchmark cực chuẩn xác.
2. **`centrality_filter.py` (Bộ lọc VIP):** Tính toán 3 loại điểm VIP cho toàn bộ người dùng trong mạng. Node nào điểm cao nhất sẽ đứng đầu danh sách. Cung cấp hàm "cắt tỉa" (xóa Node khỏi đồ thị gốc).
3. **`community_detector.py` (Phân cụm):** Đưa thuật toán AI (Louvain và Girvan-Newman) vào chạy. Nhận lại kết quả chia nhóm và đo chất lượng bằng điểm Modularity Q.
4. **`visualizer.py` (Vẽ biểu đồ):** Biến ma trận số liệu thành hình ảnh đồ thị phân màu và vẽ đường Lineplot cho báo cáo.
5. **`main_pipeline.py` (Đầu não):** Nối 4 file trên thành một dây chuyền tự động. Gõ lệnh 1 lần, code chạy từ A đến Z sinh ra bảng số liệu.

---

## 3. KỊCH BẢN DEMO THỰC TẾ TRÊN MÁY TÍNH
Khi lên bục bảo vệ, **Nhân** (hoặc người cầm chuột) hãy thực hiện theo đúng các bước sau để biểu diễn độ chuyên nghiệp:

* **Bước 1 (Xóa Data cũ):** Trực tiếp xóa 2 file ảnh `Karate_Club_Original.png`, `Karate_Club_Removed_10pct_Betweenness.png` và file `experimental_results.csv` trước mặt giáo viên để chứng minh code chạy thật, không phải lấy hình trên mạng.
* **Bước 2 (Chạy Code):** Mở Terminal (VSCode hoặc CMD), gõ lớn lệnh: `python main_pipeline.py`
* **Bước 3 (Thuyết minh lúc code chạy):** 
  *"Dạ thưa thầy/cô, hệ thống đang nạp mạng lưới Karate Club. Code đang chạy các vòng lặp từ 0% đến 20% để mô phỏng việc khóa tài khoản của các Node VIP... chạy cả 2 thuật toán Louvain và Girvan-Newman. Dạ code chạy xong rất nhanh ạ."*
* **Bước 4 (Mở hình ảnh và kết luận):** Click đúp mở các file ảnh vừa được sinh ra (Xem phần 4 để biết cách giải thích hình).

---

## 4. CÁCH ĐỌC VÀ BẢO VỆ CÁC HÌNH ẢNH (QUAN TRỌNG NHẤT)

### ẢNH 1: `Karate_Club_Original.png`
- **Hình dạng:** Một mạng lưới với các cụm màu sắc (thường là 2-3 cộng đồng).
- **Cách nói:** *"Đây là mạng lưới Karate Club ban đầu. Như thầy/cô thấy, nhờ thuật toán Layout lò xo (Spring Layout), các cộng đồng tự co cụm lại với nhau rất chặt chẽ, ranh giới 2 phe của Câu lạc bộ được thể hiện rõ ràng."*

### ẢNH 2: `Karate_Club_Removed_10pct_Betweenness.png`
- **Hình dạng:** Mạng lưới bị phân rã, cấu trúc bị đứt gãy.
- **Cách nói:** *"Hình ảnh này chụp lại khoảnh khắc chúng em ra lệnh XÓA ĐI khoảng 3-4 người dùng (10%) có chỉ số Betweenness cao nhất (những người làm Cầu nối - ví dụ như Võ sư Hi và ngài Chủ tịch). Thầy cô có thể thấy đồ thị gốc đã biến dạng hoàn toàn, mạng xã hội này đã vỡ vụn ra thành các hòn đảo."*

### ẢNH 3: `Modularity_Trend.png`
- **Hình dạng:** Biểu đồ đường (Lineplot). Trục ngang là % Xóa Node (0->20). Trục dọc là điểm Modularity. Có các đường nét đứt/liền đại diện cho 3 Centrality.
- **Cách nói:** 
  - *"Đường Degree (Nhiều bạn bè): Dù ta xóa đến 20% người có nhiều bạn bè nhất, Modularity chỉ giảm nhẹ. Có nghĩa là cộng đồng lõi không hề bị phá vỡ."*
  - *"Đường Betweenness (Cầu nối): Khi ta chỉ mới xóa đến 10%, đồ thị đã cắm đầu đi xuống cực mạnh. Khẳng định một lần nữa: Cắt đứt các 'Cầu nối' là cách phá hủy mạng lưới chí mạng nhất!"*

---

## 5. Q&A: NHỮNG CÂU HỎI PHẢN BIỆN THƯỜNG GẶP
**(Lưu ngay vào điện thoại để ứng phó)**

**Hỏi:** *Tại sao Modularity lại lao dốc khi xóa Betweenness cao?*
**Đáp:** Dạ vì người có Betweenness cao là điểm giao lộ của nhiều cộng đồng. Giống như cây cầu độc nhất bắc qua sông. Xóa họ đi thì cộng đồng bị chia cắt (Disconnected components), các thuật toán không còn tìm thấy ranh giới dày đặc để tối ưu hóa hàm Modularity.

**Hỏi:** *Sự khác biệt giữa thuật toán Louvain và Girvan-Newman là gì?*
**Đáp:** Dạ Girvan-Newman chạy theo hướng Top-down, từ từ chặt đứt các cạnh để chia nhỏ mạng lưới, nên nó cực kỳ chậm (độ phức tạp O(V*E^2)). Còn Louvain chạy Bottom-up theo hướng Heuristic tham lam, liên tục gom cụm lại, nên nó có tốc độ bàn thờ và thường chia thành các cộng đồng cục bộ tốt hơn.

**Hỏi:** *Data Karate Club này lấy ở đâu, có đáng tin không?*
**Đáp:** Dạ data này tụi em lấy trực tiếp từ benchmark tiêu chuẩn của NetworkX. Đây là dữ liệu có thật được thu thập bởi nhà xã hội học Wayne W. Zachary về một câu lạc bộ Karate ở đại học (1970-1972). Dùng dữ liệu thật này giúp nhóm có hệ quy chiếu chuẩn (ground truth) để chứng minh nghiên cứu là hoàn toàn chính xác.
