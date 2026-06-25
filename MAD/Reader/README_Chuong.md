# TÀI LIỆU BÁO CÁO CÁ NHÂN: CHƯƠNG (DATA LOADER)

**Mục tiêu nhiệm vụ:**
Cung cấp dữ liệu chuẩn và đa dạng để toàn bộ nhóm có thể chạy thuật toán phân tích mạng lưới mà không gặp lỗi file rác hay lỗi đường dẫn.

**Chi tiết thuật toán và mã nguồn đã triển khai:**
Trong file `data_loader.py`, mình chịu trách nhiệm viết 2 hàm chính:

1. **Hàm `load_karate_club()`:**
   - Mình sử dụng trực tiếp hàm `nx.karate_club_graph()` của thư viện NetworkX.
   - Đây là bộ dữ liệu thực tế do Wayne W. Zachary thu thập từ một câu lạc bộ Karate tại trường đại học (từ 1970-1972).
   - Đồ thị này có 34 nodes (đại diện cho 34 thành viên) và 78 edges (đại diện cho mối quan hệ tương tác ngoài lớp học).
   - Lý do chọn: Đây là "Hello World" của Data Science mạng lưới. Cộng đồng mạng này đã bị phân làm 2 nửa ngoài đời thực do mâu thuẫn giữa Võ sư (Mr. Hi) và Chủ tịch CLB (Officer), nên rất hoàn hảo để kiểm thử thuật toán Community Detection.

2. **Hàm `generate_facebook_network(n, m)`:**
   - Để mở rộng quy mô, mình không tải file dữ liệu Facebook hàng GB về máy gây nặng nề, mà dùng thuật toán giả lập **Barabási-Albert**.
   - Thuật toán này sinh ra đồ thị tuân theo quy luật "Preferential Attachment" (Cơ chế gắn kết ưu tiên). Tức là trong mạng xã hội, một người dùng mới tham gia (node mới) sẽ có xu hướng kết bạn với những người đã có sẵn nhiều bạn bè (rich-get-richer).
   - Mình set mặc định $n=300$ (số lượng node) và $m=3$ (số cạnh mỗi node mới sẽ tạo ra). Đồ thị sinh ra hoàn toàn có cấu trúc Scale-free giống Facebook hay Twitter thực tế.

**Đóng góp cho hệ thống:** 
File của mình đảm bảo module của Trung và Siu ở phía sau luôn luôn nhận được đầu vào là một object đồ thị `nx.Graph` hoàn toàn sạch, chuẩn hóa, không chứa node mồ côi hay edge đứt gãy.
