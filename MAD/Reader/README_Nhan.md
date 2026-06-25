# TÀI LIỆU BÁO CÁO CÁ NHÂN: NHÂN (MAIN PIPELINE)

**Mục tiêu nhiệm vụ:**
Kết nối tất cả các file mã nguồn độc lập của Chương, Trung, Siu, Huy thành một thể thống nhất. Điều phối luồng dữ liệu (Data Pipeline) từ khâu Input đến khâu Output một cách tự động, không cần sự can thiệp thủ công.

**Chi tiết thuật toán và mã nguồn đã triển khai:**
Trong file `main_pipeline.py`, mình xây dựng kiến trúc "Vòng lặp thực nghiệm đa chiều" (Grid Search Loop).

1. **Khởi tạo và Setup Baseline:**
   - Đầu tiên, gọi hàm từ Chương nạp `load_karate_club()`.
   - Lập tức truyền cho Siu và Huy vẽ tấm ảnh đồ thị gốc `Karate_Club_Original` làm hệ quy chiếu (baseline).
   - Khởi tạo mảng thông số cài đặt: 3 loại Metric (`degree`, `closeness`, `betweenness`) và mảng vòng lặp tỷ lệ cắt tỉa `[0.0, 0.05, 0.10, 0.15, 0.20]`.

2. **Logic vòng lặp thực nghiệm (Experiment Loop):**
   - Mình tạo 2 vòng `for` lồng nhau.
   - Ở mỗi bước lặp, gọi module của Trung `remove_top_vip_nodes` để "phá" đồ thị tương ứng với loại Centrality và % hiện tại.
   - **Xử lý ngoại lệ (Exception Handling):** Khi xóa quá nhiều Node, đồ thị có thể bị mất hết cạnh (`G_filtered.number_of_edges() == 0`). Mình cài đặt lệnh `continue` để chặn lỗi sập chương trình.
   - Lần lượt gọi 2 hàm `detect_louvain` và `detect_girvan_newman` của Siu. Tất cả thông số điểm Q, Tên thuật toán, Thời gian được mình đóng gói vào một bộ `dictionary` và nhét vào mảng `results`.

3. **Data Logging (Xuất dữ liệu CSV):**
   - Cuối chu trình, mảng `results` được chuyển hóa thành bảng dữ liệu 2 chiều `pandas DataFrame`.
   - Hàm `df.to_csv()` ghi toàn bộ log xuống ổ cứng dưới dạng file `experimental_results.csv`.
   - Ngay lập tức, đường dẫn file CSV được kích hoạt truyền sang cho hàm `plot_modularity_trend` của Huy để tự sinh hình ảnh phân tích.

**Đóng góp cho hệ thống:**
Sự có mặt của `main_pipeline.py` đảm bảo tính "Reproducibility" (khả năng tái lập kết quả) của dự án nghiên cứu. Bất kỳ thầy cô nào nhận được source code của nhóm, chỉ cần gõ 1 lệnh `python main_pipeline.py` duy nhất, hệ thống sẽ tự động chạy toàn bộ quy trình và sinh ra y hệt các con số và biểu đồ mà nhóm đã báo cáo.
