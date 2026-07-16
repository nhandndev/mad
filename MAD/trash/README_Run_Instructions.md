# HƯỚNG DẪN CÀI ĐẶT, CHẠY CHƯƠNG TRÌNH VÀ LẤY DỮ LIỆU

Tài liệu này hướng dẫn chi tiết cách để nhóm bạn khởi chạy dự án nghiên cứu và hiểu rõ nguồn gốc dữ liệu.

## 1. Cài đặt Môi trường (Dependencies)
Dự án sử dụng Python. Trước khi chạy, bạn cần cài đặt các thư viện lõi phục vụ cho phân tích mạng lưới và trực quan hóa dữ liệu.
Mở Terminal (hoặc Command Prompt/PowerShell) và chạy lệnh sau:
```bash
pip install networkx matplotlib pandas seaborn scipy
```
*Lưu ý: Bạn nên sử dụng `networkx` phiên bản từ 2.7 trở lên để có sẵn thuật toán Louvain tích hợp.*

## 2. Nguồn gốc Dữ liệu (Data Source)
Dự án không yêu cầu tải file dữ liệu rời từ bên ngoài (như `.csv` hay `.txt`), mà sử dụng trực tiếp các bộ dữ liệu và trình tạo dữ liệu có sẵn của `networkx` để đảm bảo tính chuẩn xác và dễ tái lập thực nghiệm:

- **Mạng lưới Karate Club của Zachary:** Đây là bộ dữ liệu kinh điển trong Network Science (Khoa học mạng lưới). Nó mô phỏng mối quan hệ của 34 thành viên trong một câu lạc bộ Karate. Dữ liệu được nạp tự động qua hàm `nx.karate_club_graph()`.
- **Mạng xã hội giả lập (Barabási-Albert):** Để mô phỏng một mạng xã hội thực tế (như Facebook) với tính chất "Scale-free" (người giàu càng giàu thêm - những người có nhiều bạn sẽ càng dễ có thêm bạn mới), chúng ta dùng hàm `nx.barabasi_albert_graph(n=300, m=3)`. Đồ thị này sẽ sinh ra ngẫu nhiên nhưng bám sát phân phối bậc của mạng xã hội thực.

## 3. Cách chạy chương trình
Toàn bộ dự án được kết nối tự động. Bạn **không cần** chạy lẻ tẻ từng file của Chương, Trung, Siu hay Huy. 

Bạn chỉ cần chạy duy nhất file `main_pipeline.py` của Nhân:
```bash
python main_pipeline.py
```

## 4. Kết quả đầu ra (Output)
Sau khi script chạy xong, trong thư mục dự án sẽ tự động xuất hiện các file sau:
1. `Karate_Club_Original.png`: Hình ảnh mạng lưới ban đầu chưa bị cắt tỉa.
2. `Karate_Club_Removed_10pct_Betweenness.png`: Hình ảnh mạng lưới sau khi thử nghiệm cắt bỏ 10% số Node VIP (dựa trên Betweenness).
3. `experimental_results.csv`: File Excel (CSV) chứa bảng số liệu điểm Modularity và thời gian chạy cho mọi trường hợp.
4. `Modularity_Trend.png`: Biểu đồ đường (Lineplot) cực kỳ quan trọng thể hiện sự sụt giảm Modularity khi cắt tỉa các Node VIP. Bạn sẽ dùng ảnh này để phân tích trong báo cáo.
