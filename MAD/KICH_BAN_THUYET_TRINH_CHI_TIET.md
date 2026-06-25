# KỊCH BẢN THUYẾT TRÌNH BẢO VỆ RESEARCH (FULL TOÀN TẬP TỪ A-Z)

*Tài liệu này là vũ khí tối thượng giúp bạn lên đứng trước Hội đồng và tự tin giải thích TẤT CẢ MỌI THỨ: Từ thuật toán, đến chỉ số, đến cách đọc 2 cái biểu đồ tách biệt.*

---

## PHẦN 1: TỔNG QUAN ĐỀ TÀI & LÝ THUYẾT 3 CHỈ SỐ
**Bạn thuyết trình:**
> "Chào thầy cô. Đề tài của nhóm em nghiên cứu về sự sụp đổ của một mạng xã hội (cụ thể là mạng Karate Club) khi ta tiêu diệt các nhân vật VIP. Ở đây, tụi em chia VIP làm 3 loại dựa trên 3 chỉ số Centrality:
> 
> 1. **Degree (Kẻ đông bạn nhất):** Là người có nhiều mối quan hệ trực tiếp nhất. Giống như một KOL có hàng triệu follower.
> 2. **Closeness (Kẻ truyền tin nhanh nhất):** Là người nằm ở vị trí 'chính giữa' mạng lưới, khoảng cách từ người này tới bất kỳ ai khác là ngắn nhất.
> 3. **Betweenness (Kẻ làm cầu nối):** Là người bí mật đứng giữa, nối phe A và phe B lại với nhau. Nếu không có người này, phe A và B sẽ không bao giờ giao tiếp được.
>
> **Mục tiêu của nghiên cứu:** Tụi em viết code để tự động xóa dần (từ 0% đến 20%) những người VIP này, xem thử xóa loại người nào thì mạng lưới sẽ chết nhanh nhất."

---

## PHẦN 2: GIẢI THÍCH 2 THUẬT TOÁN (LOUVAIN VÀ GIRVAN-NEWMAN)
*(Thầy cô chắc chắn sẽ hỏi: "Ủa em dùng thuật toán gì để biết mạng lưới nó chia phe phái?")*
**Bạn trả lời:**
> "Dạ, để biết mạng lưới bị vỡ ra thành bao nhiêu nhóm, tụi em áp dụng cùng lúc 2 thuật toán kinh điển nhất trong AI để đối chiếu (Cân đo đong đếm chéo):
> 
> 1. **Thuật toán LOUVAIN (Xây từ dưới lên - Bottom-up):** 
>    - **Cách hoạt động:** Ban đầu nó coi mỗi người là 1 nhóm riêng. Sau đó nó đi gom từ từ 2 người lại với nhau, nếu thấy điểm chất lượng nhóm (Modularity) tăng lên thì nó giữ lại. Gom miết đến khi không tăng được nữa thì dừng.
>    - **Ưu điểm:** Tốc độ cực kỳ khủng khiếp (chạy chớp mắt là xong), rất phù hợp cho mạng lưới hàng triệu người.
> 
> 2. **Thuật toán GIRVAN-NEWMAN (Chặt từ trên xuống - Top-down):**
>    - **Cách hoạt động:** Nó làm ngược lại Louvain. Nó nhìn vào toàn bộ mạng lưới, tìm ra những cái 'cây cầu' (các cạnh nối có Edge-Betweenness cao nhất) rồi lấy dao CHẶT ĐỨT cây cầu đó đi. Chặt liên tục cho đến khi mạng lưới rã ra thành từng cục nhỏ.
>    - **Nhược điểm:** Thuật toán này chạy cực kỳ chậm vì mỗi lần chặt 1 nhát là nó phải quét lại toàn bộ mạng lưới (Độ phức tạp $O(V \times E^2)$). Nhưng kết quả chia cụm của nó thường rất triệt để."

---

## PHẦN 3: GIẢI THÍCH HÌNH ẢNH MẠNG LƯỚI KARATE CLUB
**Bạn nói:**
> "Dạ thưa thầy cô, tụi em dùng data mạng Karate Club (34 người) vì đây là data thật, đã có sẵn kết quả chia rẽ nội bộ ngoài đời thực, dùng làm sa bàn thí nghiệm là chuẩn nhất.
> - **Nhìn vào hình `Karate_Club_Original`:** Mạng lưới bám rất chặt, chia làm 2 phe rõ ràng, điểm kết nối rất cao.
> - **Nhìn vào hình `Karate_Club_Removed_10pct_Betweenness`:** Sau khi tụi em xóa 10% những người làm cầu nối, mạng lưới nổ tung, các phe bị đẩy ra xa nhau, ranh giới cộng đồng hoàn toàn bị sụp đổ."

---

## PHẦN 4: GIẢI THÍCH BIỂU ĐỒ TRÙM CUỐI (`Modularity_Trend.png`)
*(Bạn mở cái hình có 2 khung: 1 khung Louvain bên trái, 1 khung Girvan-Newman bên phải)*

**Bạn nói:** 
> "Đây là biểu đồ tổng kết Research của nhóm em. Trục ngang là % người bị xóa. Trục dọc là điểm Modularity Q (Điểm càng cao thì cộng đồng càng bền vững, điểm rớt xuống đáy là nát bét).
> 
> **Thứ nhất, giải thích 3 đường (Tại sao 3 chỉ số lại có kết cục khác nhau):**
> - **Đường DEGREE (Đi ngang):** Tại sao xóa người đông bạn mà mạng lưới không sập? Dạ vì những người đông bạn (KOL) thường tụ tập lại thành một cục cốt lõi (Core) trong cùng một phe. Em xóa mất 1-2 ông KOL, thì các thành viên khác trong phe đó vẫn quen biết chéo lẫn nhau (tính dư thừa liên kết cao). Nên cấu trúc phe phái chả sứt mẻ gì!
> - **Đường CLOSENESS (Giảm từ từ):** Những người lan truyền nhanh nằm ở trung tâm hình học. Xóa họ đi thì luồng thông tin đi chậm lại, làm ranh giới phe phái mờ đi một chút, nên đường này có rớt nhưng rớt thoai thoải.
> - **Đường BETWEENNESS (Cắm đầu xuống đất):** Tại sao nó lại là tử huyệt? Dạ vì những người Betweenness cao chính là những TRẠM TRUNG CHUYỂN duy nhất giữa phe A và phe B. Khi em xóa các trạm này, phe A và phe B mất hoàn toàn liên lạc, đứt lìa khỏi nhau. Lúc này cả 2 thuật toán không tìm được liên kết để tối ưu hóa Modularity nữa, nên biểu đồ cắm đầu gãy đứng!
> 
> **Thứ hai, so sánh (Cân đo đong đếm) giữa 2 khung LOUVAIN và GIRVAN-NEWMAN:**
> - Nhìn khung **Louvain (Bên trái):** Thầy cô thấy 3 đường nó mượt mà hơn, độ sụt giảm từ từ. Vì bản chất Louvain là 'gom cụm cục bộ', nó luôn cố gắng tìm cách vớt vát lại những liên kết còn sót lại để vá víu cộng đồng.
> - Nhìn khung **Girvan-Newman (Bên phải):** Thầy cô thấy các đường (nhất là Betweenness) nó rớt cực kỳ bạo lực và gấp khúc. Vì bản chất của GN là 'vác dao đi chặt'. Mạng lưới đã bị khuyết do xóa Node VIP, mà thuật toán GN lại còn đi chặt đứt các cạnh quan trọng nữa, khiến cho mạng lưới tan nát tàn bạo hơn rất nhiều so với Louvain.

---

## PHẦN 5: CHỐT LẠI KẾT LUẬN TOÀN RESEARCH
**Bạn nói:**
> "Dạ, từ tất cả code và dữ liệu trên, nhóm em rút ra 2 kết luận khoa học:
> 1. Trong an ninh mạng hoặc quân sự, nếu muốn tiêu diệt một tổ chức tội phạm, đừng đi bắt những thằng lính có nhiều bạn bè (Degree). Hãy bắt những thằng làm **Giao liên/Trung gian (Betweenness)**, mạng lưới sẽ tự động tê liệt!
> 2. Khi chạy hệ thống thực tế lớn, ta nên dùng **Louvain** vì nó cho góc nhìn vá víu cộng đồng tốt và chạy cực nhanh, còn **Girvan-Newman** chỉ dùng để phân tích sự phá hủy triệt để trên quy mô nhỏ. Em xin hết ạ!"
