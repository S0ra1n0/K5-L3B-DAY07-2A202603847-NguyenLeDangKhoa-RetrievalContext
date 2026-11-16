# Hậu kiểm bộ đọc citation · dev (KHÔNG dùng để thay kết quả chính thức)

Lỗi được phát hiện khi đọc câu trả lời của test: model cite dạng `[id | id]` hoặc chép nguyên header `[id | blld-2012 | năm 2012 | trang … | Điều …]`. Bộ đọc của agent (commit 446525a) chỉ nhận `[id]` hoặc `[id, id]`, nên những câu này bị gán `no_citation`, tức là từ chối. Bảng dưới cho thấy câu nào sẽ đổi status nếu bộ đọc chấp nhận các dạng trên.

| Config | Query | Answerable | Status chính thức | Status hậu kiểm | Citation hậu kiểm nằm trong context |
|---|---|---|---|---|---|
