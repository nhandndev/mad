KHUNG CẤU TRÚC 12 SLIDE BẢO VỆ NGHIÊN CỨU & DỰ ÁN THỰC NGHIỆM
SLIDE 1: TIÊU ĐỀ & THÀNH VIÊN DỰ ÁN (TITLE & TEAM PROFILE)
Tiêu đề chính: Graph Centrality Metrics for Social Network Community Detection
Tiêu đề phụ: Quantifying the Impact of VIP Node Removal on Modularity and Computational Performance
Phân nhóm lĩnh vực: Graph Theory, Complex Network Analysis & Software Engineering
Người thuyết trình: Đoàn Ngọc Nhân (Leader / Quản lý Pipeline)
Đội ngũ thực hiện:
Đoàn Ngọc Nhân (Leader) — MSSV: QE210282 (Kiến trúc Sư Đường Ống)
Lê Đỗ Anh Khoa — MSSV: QE210269 (Chuyên Gia Toán Học Nghiên Cứu)
Nguyễn Thành Chương — MSSV: QE210081 (Kỹ Sư Quản Trị Dữ Liệu)
Đỗ Văn Trung (Chung) — MSSV: QE210224 (Kỹ Sư Tiền Xử Lý Hệ Thống)
Huỳnh Hoàng Siêu — MSSV: QE210005 (Chuyên Gia Tối Ưu Thuật Toán)
Lê Chấn Huy — MSSV: QE210078 (Kỹ Sư Trực Quan Hóa & Phân Tích)
Lớp: SE20D
Bằng chứng kết hợp [HYBRID PROOF]: Slide mở đầu giới thiệu rõ một đề tài khoa học có chiều sâu lý thuyết nhưng được vận hành bởi một đội ngũ kỹ sư phần mềm chuyên nghiệp, phân vai rõ ràng theo mô hình Agile (từ nạp dữ liệu, lọc cấu trúc, tối ưu thuật toán cho đến vẽ biểu đồ).
SLIDE 2: ĐẶT VẤN ĐỀ & CÂU HỎI NGHIÊN CỨU (PROBLEM STATEMENT & RESEARCH QUESTION)
Tiêu đề chính: Đặt Vấn Đề: Vai Trò Nút VIP và Sự Phân Rã Cộng Đồng
Tiêu đề phụ: Câu Hỏi Nghiên Cứu và Mục Tiêu Thực Nghiệm Định Lượng
Người thuyết trình: Đoàn Ngọc Nhân (Leader)
Nội dung cốt lõi:
Bối cảnh: Mạng xã hội không đồng nhất mà phân rã thành các cụm (communities) mật độ liên kết cao nội bộ. Các nút có độ trung tâm cao (VIP Nodes) đóng vai trò điều hướng hoặc kết nối liên cụm.
Câu hỏi nghiên cứu (Research Question - RQ):"Khi ta chủ động loại bỏ các node có độ trung tâm (Centrality) cao nhất theo các tiêu chí toán học khác nhau, cấu trúc cộng đồng tự nhiên của mạng xã hội sẽ bị phân rã hoàn toàn (Destroyed) hay lại được cô lập hóa rõ rệt hơn (Sharpened)?"
Nhiệm vụ thực nghiệm (Project Goal): Xây dựng một pipeline tự động để thực hiện kịch bản "tấn công cấu trúc" có chủ đích và đo đạc phản ứng của mạng lưới.
Bằng chứng nghiên cứu [RESEARCH PROOF]: Định nghĩa rõ ràng một bài toán khoa học (Research Problem) chưa có lời giải hiển nhiên. Xác định mục tiêu nghiên cứu là đo lường sự dịch chuyển của cấu trúc liên thông mạng dưới áp lực tấn công chọn lọc.
SLIDE 3: CƠ SỞ TOÁN HỌC & LÝ THUYẾT NỀN TẢNG (THEORETICAL FOUNDATIONS & LITERATURE)
Tiêu đề chính: Cơ Sở Toán Học: Các Chỉ Số Trung Tâm và Hàm Chất Lượng Modularity
Tiêu đề phụ: Kế Thừa Nền Tảng Văn Liệu Khoa Học Từ Các "Khổng Lồ"
Người thuyết trình: Lê Đỗ Anh Khoa (Chuyên gia Toán học)
Nội dung cốt lõi:
Định lượng Node VIP qua 3 độ đo Centrality:
Degree Centrality ():  (Độ nổi tiếng cục bộ)
Closeness Centrality ():  (Tốc độ truyền tin địa lý)
Betweenness Centrality ():  (Nút thắt cổ chai, cầu nối liên thông)
Hàm mục tiêu đánh giá chất lượng cộng đồng Modularity ():

Hệ thống Văn liệu kế thừa (Literature Map): Freeman (1977) về Centrality; Girvan-Newman (2002) về Phân hoạch; Blondel et al. (2008) về Louvain; Albert et al. (2000) về Tính chịu lỗi của đồ thị; Fortunato (2010) về Giới hạn phân giải Modularity.
Bằng chứng nghiên cứu [RESEARCH PROOF]: Chứng minh đề tài dựa trên các công thức toán học nghiêm túc và có sự kế thừa trực tiếp từ hệ thống nghiên cứu quốc tế (Citations), không phải là tự chế công thức.
SLIDE 4: THIẾT KẾ MA TRẬN THỰC NGHIỆM (EXPERIMENTAL MATRIX DESIGN)
Tiêu đề chính: Thiết Kế Nghiên Cứu: Ma Trận Thực Nghiệm Tự Động 30-Run
Tiêu đề phụ: Kiểm Chứng Baseline Trên Mạng Lưới Thực Tế Zachary's Karate Club
Người thuyết trình: Nguyễn Thành Chương (Kỹ sư Dữ liệu)
Nội dung cốt lõi:
Dataset duy nhất: Zachary's Karate Club ( nút,  cạnh). Đây là một mạng lưới thực tế kinh điển ghi nhận sự phân rã có thật ngoài đời, giúp loại bỏ hoàn toàn các sai số giả định từ đồ thị mô phỏng.
Ma trận thiết kế thực nghiệm thực tế ( kịch bản):
3 Biến độc lập (Centrality): 
5 Tỷ lệ cắt tỉa (): , , , , 
2 Thuật toán phân hoạch: Louvain (Gom cụm) và Girvan-Newman (Phân rã)
Bằng chứng nghiên cứu [RESEARCH PROOF]: Thể hiện phương pháp luận nghiên cứu thực nghiệm (Empirical Research Methodology) chuẩn quy: Có biến độc lập, biến phụ thuộc (Modularity, Time), có đối chứng (0% removal) và môi trường kiểm thử cô lập.
SLIDE 5: KIẾN TRÚC PIPELINE TỰ ĐỘNG & BẢN ĐỒ BIÊN PHÒNG CODE (CODE DEFENSE MAP)
Tiêu đề chính: Kiến Trúc Dự Án: Đường Ống Xử Lý Tự Động Hóa Khép Kín
Tiêu đề phụ: Bản Đồ Biên Phòng Code và Phân Nhiệm Kỹ Thuật
Người thuyết trình: Đoàn Ngọc Nhân (Leader) & Đỗ Văn Trung (Chung)
Nội dung cốt lõi:
Sơ đồ khối luồng dữ liệu (Data Pipeline Flow):
[data_loader.py] ➔ [centrality_filter.py] ➔ [community_detector.py] ➔ [visualizer.py]
                             ▲                       │
                             └────── [main_pipeline.py] ◄────── Ghi log CSV


Bản đồ Code Defense: Chứng minh tính module hóa của mã nguồn phần mềm, phân công trách nhiệm bảo vệ từng file code cụ thể cho từng kỹ sư trong nhóm (Nhân: main_pipeline.py, Chương: data_loader.py, Chung: centrality_filter.py, Siêu: community_detector.py, Huy: visualizer.py).
Bằng chứng dự án [PROJECT PROOF]: Chứng minh kỹ năng thiết kế kiến trúc phần mềm sạch (Clean Architecture). Dự án được tự động hóa 100% qua pipeline trung tâm, không làm thủ công, đảm bảo tính tái lặp (reproducibility) cao của phần mềm khoa học.
SLIDE 6: MODULE TIỀN XỬ LÝ & GIẢI PHẪU ĐỒ THỊ ĐỘNG (CENTRALITY FILTERING)
Tiêu đề chính: Kỹ Thuật Dự Án: Bộ Lọc Cắt Tỉa Node VIP Tự Động
Tiêu đề phụ: Giải Quyết Bài Toán Loại Bỏ Nút Không Gây Sập Chỉ Mục Đồ Thị
Người thuyết trình: Đỗ Văn Trung (Chung) (Kỹ sư Tiền xử lý)
Nội dung cốt lõi:
Logic kỹ thuật của centrality_filter.py:
Trích xuất và chuẩn hóa điểm số  về đoạn .
Sắp xếp giảm dần và cắt tỉa chính xác  nút có điểm cao nhất.
Thực hiện xóa nút và các cạnh liên đới thông qua cơ chế quản lý con trỏ bộ nhớ của thư viện NetworkX (G.remove_node()).
Giải pháp xử lý cô lập: Đảm bảo đồ thị sau khi cắt tỉa (subgraph) vẫn duy trì tính toàn vẹn của chỉ mục (Index Integrity) để chuyển giao sang cho thuật toán phát hiện cộng đồng mà không gây lỗi tham chiếu con trỏ.
Bằng chứng dự án [PROJECT PROOF]: Chứng minh năng lực giải quyết các bài toán lập trình hệ thống thực tế liên quan đến thao tác cấu trúc dữ liệu đồ thị động và tối ưu hóa bộ nhớ RAM khi biến đổi topology của đồ thị.
SLIDE 7: PHÂN TÍCH KỸ THUẬT THUẬT TOÁN ĐỐI NGHỊCH (COMMUNITY DETECTOR)
Tiêu đề chính: Kỹ Thuật Thuật Toán: Đối Sánh Triết Lý Gom Cụm và Phân Rã
Tiêu đề phụ: Phân Tích Độ Phức Tạp Thuật Toán Louvain vs. Girvan-Newman
Người thuyết trình: Huỳnh Hoàng Siêu (Chuyên gia Thuật toán)
Nội dung cốt lõi:
Bảng đối chuẩn hiệu năng kỹ thuật:
Louvain (Bottom-up Heuristic): Độ phức tạp thực tế . Gom cụm tham lam tối đa hóa Modularity cục bộ. Phù hợp xử lý dữ liệu lớn (Big Data).
Girvan-Newman (Top-down Divisive): Độ phức tạp cực lớn . Cắt tỉa tuần tự các cạnh có Edge Betweenness cao nhất và tính toán lại sau mỗi lần cắt.
Đóng gói module: File community_detector.py đóng gói cả hai thuật toán, sử dụng decorator đo thời gian thực thi bằng microsecond chính xác cho từng phiên chạy.
Bằng chứng dự án [PROJECT PROOF]: Thể hiện sự hiểu biết sâu sắc về cấu trúc thuật toán và độ phức tạp tính toán (Computational Complexity), giúp nhóm đưa ra quyết định tối ưu hóa tài nguyên phần cứng phù hợp.
SLIDE 8: CHỨNG MINH NGHIÊN CỨU I — BIẾN THIÊN MODULARITY PHẢN TRỰC QUAN
Tiêu đề chính: Kết Quả Nghiên Cứu I: Hiện Tượng Tăng Ngược Modularity Phản Trực Quan
Tiêu đề phụ: Biện Luận Toán Học Về Hành Vi Phân Rã Của Mạng Xã Hội
Người thuyết trình: Lê Chấn Huy (Chuyên gia Trực quan & Biện luận)
Nội dung cốt lõi:
Dữ liệu thực nghiệm (Table 2): Khi loại bỏ  node Degree và Closeness cao nhất, Modularity  tăng mạnh từ  (mức đỉnh điểm tại 15% Betweenness removal).
Lập giải khoa học:
Các node VIP là các "giao liên chéo" (cross-edges) nối chồng chéo giữa các phe phái. Khi bị loại bỏ, các ranh giới nhiễu biến mất, các cộng đồng còn lại trở nên cực kỳ thuần nhất và cô lập hoàn hảo  tăng vọt.
Xóa node có Betweenness cao làm sụp đổ cấu trúc mạng nhanh nhất ( rơi xuống đáy  tại mốc 20%), chứng minh Betweenness là tử huyệt liên thông đồ thị.
Bằng chứng nghiên cứu [RESEARCH PROOF]: Phát hiện ra quy luật phi tuyến tính (non-linear pattern) từ dữ liệu thực tế và đưa ra lập luận khoa học chặt chẽ để giải thích hiện tượng, thay vì chỉ đưa ra bảng số liệu thô.
SLIDE 9: CHỨNG MINH DỰ ÁN II — SỰ SỤP ĐỔ THỜI GIAN CHẠY CỦA GIRVAN-NEWMAN
Tiêu đề chính: Kết Quả Dự Án II: Hiện Tượng Sụp Đổ Thời Gian Chạy (Execution Time Collapse)
Tiêu đề phụ: Đo Lường Sự Tối Ưu Hóa Tài Nguyên Tính Toán Từ Cắt Tỉa Cấu Trúc
Người thuyết trình: Lê Chấn Huy & Huỳnh Hoàng Siêu
Nội dung cốt lõi:
Dữ liệu đo đạc thực tế:
Thời gian thực thi của Girvan-Newman sụt giảm ngoạn mục từ  xuống dưới  khi tăng tỷ lệ cắt tỉa lên .
Louvain giữ vững đồ thị phẳng ổn định ở mức cực thấp ().
Giải thích kỹ thuật:
Khi xóa các node VIP, đồ thị bị phân rã sớm thành các thành phần liên thông rời rạc siêu nhỏ. Số lượng cạnh còn lại cần tính toán lại Edge Betweenness giảm theo hàm lũy thừa  Thời gian chạy của Girvan-Newman giảm cực nhanh.
Bằng chứng dự án [PROJECT PROOF]: Chứng minh nhóm có thực hiện đo đạc hiệu năng thực tế (Performance Profiling) dưới góc độ kỹ sư hệ thống, tìm ra mối tương quan trực tiếp giữa sự thay đổi cấu trúc dữ liệu mạng lưới và hiệu năng của thuật toán.
SLIDE 10: THẢO LUẬN KHOA HỌC & CẢNH BÁO GIỚI HẠN PHÂN GIẢI (RESOLUTION LIMIT)
Tiêu đề chính: Thảo Luận: Giới Hạn Độ Phân Giải Modularity và Tính Chống Chịu Tấn Công
Tiêu đề phụ: Đào Sâu Bản Chất Vật Lý Của Đồ Thị Dưới Áp Lực Cắt Tỉa
Người thuyết trình: Lê Chấn Huy (hoặc Đoàn Ngọc Nhân điều phối)
Nội dung cốt lõi:
Cảnh báo ảo ảnh toán học (Resolution Limit): Ở mốc xóa , Modularity tăng nhẹ thực chất là do đồ thị bị vỡ vụn quá mức (Fortunato, 2010). Thuật toán Louvain bị giới hạn độ phân giải nên tự gom các mảnh vỡ này thành các cộng đồng ảo, thực tế cấu trúc mạng lúc này đã bị tê liệt hoàn toàn.
Đối chuẩn Robustness (Albert et al., 2000): Tái xác nhận lý thuyết: mạng xã hội cực kỳ bền vững trước sự biến mất của các Hub giao tiếp lớn (Degree) nhưng lại cực kỳ mong manh trước các đòn tấn công nhắm vào các "giao liên cầu nối" (Betweenness).
Bằng chứng nghiên cứu [RESEARCH PROOF]: Thể hiện tư duy phản biện khoa học (Critical Thinking). Nhóm không chỉ tin vào con số Modularity tăng một cách mù quáng mà chỉ ra được bản chất hạn chế toán học đứng sau con số đó.
SLIDE 11: KẾT LUẬN & ĐÓNG GÓP THỰC TIỄN CHO ĐỜI THỰC (APPLICATIONS & FUTURE WORK)
Tiêu đề chính: Kết Luận Đề Tài: Ứng Dụng Trong An Ninh Mạng và Kiến Trúc Pipeline
Tiêu đề phụ: Đóng Góp Thực Tiễn Của Nghiên Cứu Vào Đời Sống Số
Người thuyết trình: Đoàn Ngọc Nhân (Leader)
Nội dung cốt lõi:
Ứng dụng An ninh mạng (Chống tin giả/Tội phạm): Nếu muốn vô hiệu hóa một mạng lưới thông tin độc hại, đừng phí tài nguyên đi bắt các tài khoản KOL nhiều follow (Degree Centrality). Hãy nhắm trực tiếp vào các tài khoản trung gian, đóng vai trò giao liên kết nối giữa các hội nhóm kín (Betweenness Centrality) để bẻ gãy cấu trúc liên lạc của chúng một cách triệt để nhất.
Tối ưu hóa Pipeline kỹ thuật: Sử dụng đo lường Centrality làm bộ lọc tiền xử lý siêu nhẹ (Lightweight Pre-filtering) giúp giảm tải dữ liệu thô, biến các thuật toán phức tạp như Girvan-Newman trở nên khả thi trên các hệ thống đồ thị lớn.
Bằng chứng kết hợp [HYBRID PROOF]: Trả lời xuất sắc câu hỏi kinh điển của Hội đồng: "Nghiên cứu này chạy xong thì ứng dụng được gì cho xã hội và cho kỹ thuật?" bằng hai giải pháp cực kỳ thực tế và thuyết phục.
SLIDE 12: HỎI ĐÁP & CHUẨN BỊ PHẢN BIỆN (Q&A & DEFENSE READY)
Tiêu đề chính: Hỏi & Đáp (Q&A) - Nhóm 1 Sẵn Sàng Trình Bày
Tiêu đề phụ: Bản Đồ Phản Biện Chốt Chặn Cho 3 Câu Hỏi "Bẫy" Của Hội Đồng
Người thuyết trình: Cả 6 thành viên (Nhân điều phối câu hỏi cho Khoa, Siêu, Chương, Chung, Huy)
Nội dung cốt lõi:
Sẵn sàng giải trình cấu trúc code của 5 file: main_pipeline.py, data_loader.py, centrality_filter.py, community_detector.py, visualizer.py.
Sẵn sàng giải thích toán học đằng sau các chỉ số  và hiện tượng ảo ảnh Modularity ở mốc .
Bằng chứng dự án + nghiên cứu [HYBRID PROOF]: Slide kết thúc thể hiện phong thái tự tin, chuyên nghiệp, làm chủ hoàn toàn từ dòng code thực tế cho đến lý thuyết toán học hàn lâm.
