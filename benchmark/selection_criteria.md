# Tiêu chí chọn cấu hình (đăng ký trước khi so sánh)

Trạng thái: **ĐÃ XÁC NHẬN** ngày 2026-11-16, học viên giữ nguyên bản nháp (roadmap P2.7). File được commit cùng benchmark trước mọi lần chạy retrieval/agent của Day 7 và không được sửa nữa.

## Phạm vi

- Chọn **chỉ dựa trên dev** (20 câu có đáp án + 3 câu thiếu bằng chứng). Không dùng test cho bất kỳ bước chọn nào.
- Ứng viên gồm mọi cấu hình đã chạy agent trên dev. Mỗi cấu hình là: phương pháp retrieval + top-k + rerank + cách chọn context + budget.

## Thứ tự ưu tiên

So sánh lần lượt từng tiêu chí. Hai cấu hình **chênh ≤ 1 câu** ở một tiêu chí thì coi là hòa ở tiêu chí đó và xét tiêu chí tiếp theo.

1. **Context Evidence Rate** trên dev (cao hơn tốt hơn).
2. **Grounded answer trung bình /2** trên dev, theo nhãn đã được người duyệt (cao hơn tốt hơn).
3. **Từ chối nhầm**: số câu có đáp án bị từ chối (ít hơn tốt hơn).
4. **Abstention đúng** trên 3 câu dev thiếu bằng chứng (nhiều hơn tốt hơn).
5. **Evidence Hit@3** trên dev (cao hơn tốt hơn).
6. **Latency trung vị** mỗi câu của agent (thấp hơn tốt hơn).
7. **Chi phí**: model đều chạy local, chi phí API = 0 USD, nên so sánh tổng token (thấp hơn tốt hơn).

Nếu vẫn hòa sau cả 7 tiêu chí, chọn cấu hình **đơn giản hơn** (ít thành phần hơn).

## Ghi nhận

Kết quả chọn được ghi vào `results/selection.json` gồm thời điểm, `based_on: "dev only"`, bảng xếp hạng và lý do. File được commit **trước** khi chạy test. Test chỉ chạy một lần cho baseline (dense) và cấu hình được chọn.
