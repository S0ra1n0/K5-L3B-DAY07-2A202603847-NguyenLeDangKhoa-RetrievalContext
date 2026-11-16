# Phiếu chấm agent · dev

Đọc từng câu: so câu trả lời với đáp án/lý do thiếu bằng chứng, rồi mở đoạn được cite (in ngay bên dưới) để xác nhận đoạn đó thực sự chứa khẳng định. Sửa nhãn trong file CSV cùng tên (cột human_*).

## agent_dense_k3 · q01 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, hai bên được giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn bao lâu?

**Kỳ vọng:** Hợp đồng có thời hạn dưới 01 tháng (trừ các trường hợp tại khoản 2 Điều 18, điểm a khoản 1 Điều 145 và khoản 1 Điều 162).

**Agent trả lời:** Theo Bộ luật Lao động 2019, hai bên được giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn dưới 01 tháng [410ba0a07076ab8d].

**Lượt tìm:** `hợp đồng lao động bằng lời nói thời hạn` (filter {'year': 2019}, user)

> **[410ba0a07076ab8d]** blld-2019 · Điều 14 · trang [6, 7]
>
> Điều 14. Hình thức hợp đồng lao động 1. Hợp đồng lao động phải được giao kết bằng văn bản và được làm thành 02 bản, người lao động giữ 01 bản, người sử dụng lao động giữ 01 bản, trừ trường hợp quy định tại khoản 2 Điều này. Hợp đồng lao động được giao kết thông qua phương tiện điện tử dưới hình thức thông điệp dữ liệu theo quy định của pháp luật về giao dịch điện tử có giá trị như bợp đồng lao động bằng văn bản. 2. Hai bên có thể giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn dưới 01 tháng, trừ trường hợp quy định tại khoản 2 Điều 18, điểm a khoản 1 Điều 145 và khoản 1 Điều 162 của Bộ luật này. Ss

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q02 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2012, công việc tạm thời có thời hạn bao lâu thì các bên được giao kết hợp đồng bằng lời nói?

**Kỳ vọng:** Công việc tạm thời có thời hạn dưới 03 tháng.

**Agent trả lời:** Theo Bộ luật Lao động 2012, các bên được giao kết hợp đồng lao động bằng lời nói đối với công việc tạm thời có thời hạn dưới 03 tháng [8b35e2d37ae827ce].

**Lượt tìm:** `hợp đồng bằng lời nói công việc tạm thời thời hạn` (filter {'year': 2012}, user)

> **[8b35e2d37ae827ce]** blld-2012 · Điều 16 · trang [6]
>
> Điều 16. Hình thức hợp đồng lao động 1. Hợp đồng lao động phải được giao kết bằng văn bản và được làm thành 02 bản, người lao động giữ 01 bản, người sử dụng lao động giữ 01 bản, trừ trường hợp quy định tại khoản 2 Điều này. 2. Đối với công việc tạm thời có thời hạn dưới 03 tháng, các bên có thể giao kết hợp đồng lao động bằng lời nói.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q03 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, số giờ làm thêm của người lao động tối đa trong một tháng là bao nhiêu?

**Kỳ vọng:** Không quá 40 giờ trong 01 tháng (và không quá 200 giờ/năm, trừ các trường hợp được làm đến 300 giờ/năm).

**Agent trả lời:** Theo Bộ luật Lao động 2019, số giờ làm thêm của người lao động tối đa trong một tháng là **40 giờ**.

Căn cứ:
- Điều 107, khoản 2, điểm b) quy định: "không quá 40 giờ trong 01 tháng" [71267d6e72a8bf88].

**Lượt tìm:** `số giờ làm thêm tối đa trong một tháng` (filter {'year': 2019}, user)

> **[71267d6e72a8bf88]** blld-2019 · Điều 107 · trang [40]
>
> Điều 107. Làm thêm giờ 1. Thời gian làm thêm giờ là khoảng thời gian làm việc ngoài thời giờ làm việc bình thường theo quy định của pháp luật, thỏa ước lao động tập thê hoặc nội quy lao động. 2. Người sử dụng lao động được sử dụng người lao động làm thêm giờ khi đáp ứng đây đủ các yêu câu sau đây: a) Phải được sự đồng ý của người lao động: b) Bảo đảm số giờ làm thêm của người lao động không quá 50% số giờ làm việc bình thường trong 01 ngày; trường hợp áp dụng quy định thời giờ làm việc bình thường theo tuân thì tổng số giờ làm việc bình thường và số giờ làm thêm không quá 12 giờ trong 01 ngày; không quá 40 giờ trong 01 tháng: c) Bảo đảm số giờ làm thêm của người lao động không quá 200 giờ trong 01 năm, trừ trường hợp quy định tại khoản 3 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q04 · status `answered`

**Câu hỏi:** Bộ luật Lao động 2012 giới hạn số giờ làm thêm trong một tháng là bao nhiêu?

**Kỳ vọng:** Không quá 30 giờ trong 01 tháng.

**Agent trả lời:** Theo Bộ luật Lao động 2012, số giờ làm thêm của người lao động không quá 30 giờ trong một tháng [3b164eb9c075d12a].

**Lượt tìm:** `giới hạn số giờ làm thêm trong một tháng` (filter {'year': 2012}, user)

> **[3b164eb9c075d12a]** blld-2012 · Điều 106 · trang [30, 31]
>
> Điều 106. Làm thêm giờ 1. Làm thêm giờ là khoảng thời gian làm việc ngoài thời giờ làm việc bình thường được quy định trong pháp luật, thỏa ước lao động tập thể hoặc theo nội quy. lao động. 2. Người sử dụng lao động được sử dụng người lao động làm thêm giờ khi đáp ứng đủ các điều kiện sau đây: a) Được sự đồng ý của người lao động: b) Bảo đảm số giờ làm thêm của người lao động không quá 50% số giờ làm việc bình thuờng trong 01 ngày, trường hợp áp dụng quy định làm việc theo tuần thì tông số giờ làm việc bình thường và số giờ làm thêm không quá 12 giờ trong 01 ngày, không quá 30 giờ trong 0] tháng và tông sô không quá 200 giờ trong 01 năm, trừ một sô trường hợp đặc biệt do Chính phủ quy định thì được làm thêm giờ không quá 300 giờ trong 01 năm; c) Sau mỗi đợt làm thêm giờ nhiều ngày liên tục trong tháng, người sử dụng lao động phải bô trí đề người lao động được nghỉ bù cho sô thời gian đã 

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q05 · status `answered`

**Câu hỏi:** Người được tuyển vào vị trí quản lý doanh nghiệp có thể phải thử việc tối đa bao nhiêu ngày?

**Kỳ vọng:** Không quá 180 ngày (quy định của Bộ luật Lao động 2019; bản 2012 không có mức riêng cho người quản lý doanh nghiệp).

**Agent trả lời:** Người lao động nói chung có thể thử việc tối đa 18 tháng theo quy định tại Điều 24 Bộ luật Lao động 2019 [18875379609a900a]. Tuy nhiên, đối với người lao động làm việc theo hợp đồng lao động có thời hạn dưới 01 tháng thì không áp dụng thử việc [18875379609a900a].

**Lượt tìm:** `thử việc người lao động quản lý` (filter None, none)

> **[18875379609a900a]** blld-2019 · Điều 24 · trang [10]
>
> Điều 24. Thử việc 1. Người sử dụng lao động và người lao động có thể thỏa thuận nội dung thử việc ghi trong hợp đông lao động hoặc thỏa thuận về thử việc băng việc giao kêt hợp đông thử việc. 2. Nội dung chủ yếu của hợp đồng thử việc gồm thời gian thử việc và nội dung quy định tại các điểm a, b, c, đ, g vàh khoản 1 Điều 21 của Bộ luật này. 3. Không áp dụng thử việc đối với người lao động giao kết hợp đồng lao động có thời hạn dưới 01 tháng.

*Nháp AI:* grade=0 · citation=false · abstention= · Trả lời 'tối đa 18 tháng' là bịa: Điều 24/2019 không nêu thời gian thử việc; context không có Điều 25 (180 ngày). Citation [Đ24] chỉ hỗ trợ ý phụ 'HĐ dưới 01 tháng không thử việc', không hỗ trợ khẳng định chính.

## agent_dense_k3 · q06 · status `answered`

**Câu hỏi:** Tiền lương trong thời gian thử việc ít nhất phải bằng bao nhiêu phần trăm mức lương của công việc đó?

**Kỳ vọng:** Ít nhất bằng 85% mức lương của công việc đó (giống nhau ở bản 2012 và 2019).

**Agent trả lời:** Theo Bộ luật Lao động 2012, tiền lương trong thời gian thử việc ít nhất phải bằng 85% mức lương của công việc đó [fbeaa39254552433].

Theo Bộ luật Lao động 2019, tiền lương trong thời gian thử việc cũng ít nhất phải bằng 85% mức lương của công việc đó [0eeeb5f152e2ed3b].

**Lượt tìm:** `tiền lương thời gian thử việc tỷ lệ phần trăm mức lương công việc` (filter None, none)

> **[fbeaa39254552433]** blld-2012 · Điều 28 · trang [9]
>
> Điều 28. Tiền lương trong thời gian thử việc Tiền lương của người lao động trong thời gian thử việc do hai bên thoả thuận nhưng ít nhất phải bằng 85% mức lương của công việc đó.

> **[0eeeb5f152e2ed3b]** blld-2019 · Điều 26 · trang [10]
>
> Điều 26. Tiền lương thứ việc Tiền lương của người lao động trong thời gian thử việc do hai bên thỏa thuận nhưng ít nhất phải băng 85% mức lương của công việc đó.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q07 · status `answered`

**Câu hỏi:** Nhân viên ký hợp đồng không thời hạn muốn tự nghỉ việc thì phải báo trước cho công ty ít nhất bao lâu?

**Kỳ vọng:** Ít nhất 45 ngày (bản 2012 có ngoại lệ cho lao động nữ mang thai theo Điều 156).

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động làm việc theo hợp đồng lao động không xác định thời hạn muốn đơn phương chấm dứt hợp đồng lao động phải báo trước cho người sử dụng lao động ít nhất 45 ngày [88d5dd520c3fcef6].

Theo Bộ luật Lao động 2012, người lao động làm việc theo hợp đồng lao động không xác định thời hạn muốn đơn phương chấm dứt hợp đồng lao động phải báo trước cho người sử dụng lao động ít nhất 45 ngày [fceb706dab47570b].

**Lượt tìm:** `tự thôi việc hợp đồng không thời hạn báo trước` (filter None, none)

> **[88d5dd520c3fcef6]** blld-2019 · Điều 35 · trang [14]
>
> Điều 35. Quyền đơn phương chấm dứt hợp đồng lao động của người lao động 1. Người lao động có quyền đơn phương chấm dứt hợp đồng lao động nhưng phải báo trước cho người sử dụng lao động như sau: a) Ít nhất 45 ngày nếu làm việc theo hợp đồng lao động không xác định thời hạn; b) Ít nhất 30 ngày nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn từ 12 tháng đên 36 tháng: c) Ít nhất 03 ngày làm việc nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn dưới 12 tháng: d) Đối với một số ngành, nghề, công việc đặc thù thì thời hạn báo trước được thực hiện theo quy định của Chính phủ.

> **[fceb706dab47570b]** blld-2012 · Điều 40 · trang [13]
>
> Điều 40. Huỷ bỏ việc đơn phương chấm dứt hợp đồng lao động Mỗi bên đều có quyền huỷ bỏ việc đơn phương chấm dứt hợp đồng lao động trước khi hết thời hạn báo trước nhưng phải thông báo bằng văn bản và phải được bên kia đồng ý.

*Nháp AI:* grade=2 · citation=true;false · abstention= · Đáp án 45 ngày đúng và được Điều 35/2019 hỗ trợ. Citation thứ hai (Điều 40/2012 'Hủy bỏ việc đơn phương chấm dứt') KHÔNG chứa mức 45 ngày của bản 2012, nên sai.

## agent_dense_k3 · q08 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, nếu người lao động bị trả lương không đúng thời hạn thì có phải báo trước khi đơn phương chấm dứt hợp đồng không?

**Kỳ vọng:** Không cần báo trước, trừ trường hợp quy định tại khoản 4 Điều 97.

**Agent trả lời:** Không, Bộ luật Lao động 2019 không quy định trường hợp người lao động bị trả lương không đúng thời hạn là lý do để đơn phương chấm dứt hợp đồng lao động mà không cần báo trước.

Theo Điều 35 [88d5dd520c3fcef6], người lao động chỉ được đơn phương chấm dứt hợp đồng lao động khi có một trong các lý do được quy định tại các Điều 35, 36 và 37 của Bộ luật này. Việc trả lương không đúng thời hạn không nằm trong các lý do này.

Do đó, nếu người lao động đơn phương chấm dứt hợp đồng lao động vì lý do trả lương không đúng thời hạn, sẽ được coi là đơn phương chấm dứt hợp đồng lao động trái pháp luật theo Điều 39 [2b82e938dbe5e213] và phải chịu các nghĩa vụ theo Điều 40 [ebea0c01b9dd25d1].

**Lượt tìm:** `người lao động bị trả lương không đúng thời hạn đơn phương chấm dứt hợp đồng` (filter {'year': 2019}, user)

> **[88d5dd520c3fcef6]** blld-2019 · Điều 35 · trang [14]
>
> Điều 35. Quyền đơn phương chấm dứt hợp đồng lao động của người lao động 1. Người lao động có quyền đơn phương chấm dứt hợp đồng lao động nhưng phải báo trước cho người sử dụng lao động như sau: a) Ít nhất 45 ngày nếu làm việc theo hợp đồng lao động không xác định thời hạn; b) Ít nhất 30 ngày nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn từ 12 tháng đên 36 tháng: c) Ít nhất 03 ngày làm việc nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn dưới 12 tháng: d) Đối với một số ngành, nghề, công việc đặc thù thì thời hạn báo trước được thực hiện theo quy định của Chính phủ.

> **[2b82e938dbe5e213]** blld-2019 · Điều 39 · trang [16]
>
> Điều 39. Đơn phương chấm dứt hợp đồng lao động trái pháp luật Đơn phương chấm dứt hợp đồng lao động trái pháp luật là trường hợp châm dứt hợp đông lao động không đúng quy định tại các điêu 35, 36 và 37 của Bộ luật này.

> **[ebea0c01b9dd25d1]** blld-2019 · Điều 40 · trang [16]
>
> Điều 40. Nghĩa vụ của người lao động khi đơn phương chấm dứt hợp đồng lao động trái pháp luật 1. Không được trợ cấp thôi việc. 2. Phải bồi thường cho người sử dụng lao động nửa tháng tiền lương theo hợp đông lao động và một khoản tiền tương ứng với tiền lương theo hợp đồng lao động trong những ngày không báo trước 3. Phải hoàn trả cho người sử dụng lao động chỉ phí đào tạo quy định tại Điều 62 của Bộ luật này.

*Nháp AI:* grade=0 · citation=false;false;false · abstention= · Kết luận ngược: nói trả lương không đúng hạn KHÔNG phải lý do chấm dứt không cần báo trước. Context thiếu khoản 2 Điều 35 (final_context_has_evidence=false). Câu 'chỉ được chấm dứt khi có lý do tại Điều 35, 36, 37' không có trong Điều 35 part 1; Điều 39, 40 không liên quan.

## agent_dense_k3 · q09 · status `answered`

**Câu hỏi:** Trợ cấp thôi việc được tính bao nhiêu cho mỗi năm làm việc?

**Kỳ vọng:** Mỗi năm làm việc được trợ cấp một nửa tháng tiền lương (áp dụng cho người làm việc thường xuyên từ đủ 12 tháng trở lên).

**Agent trả lời:** Theo Bộ luật Lao động 2019 và 2012, trợ cấp thôi việc được tính như sau:

- **Bộ luật Lao động 2019** [e3c977d516130853]: Mỗi năm làm việc, người lao động được trợ cấp một nửa tháng tiền lương.
- **Bộ luật Lao động 2012** [a099008554b28f45]: Mỗi năm làm việc, người lao động được trợ cấp một nửa tháng tiền lương.

Tiền lương để tính trợ cấp là tiền lương bình quân của 06 tháng liền kề trước khi thôi việc.

**Lượt tìm:** `trợ cấp thôi việc tính theo năm làm việc` (filter None, none)

> **[e3c977d516130853]** blld-2019 · Điều 46 · trang [19]
>
> Điều 46. Trợ cấp thôi việc 1. Khi hợp đồng lao động chấm dứt theo quy định tại các khoản 1, 2,3, 4,6,7,9và 10 Điều 34 của Bộ luật này thì người sử dụng lao động có trách nhiệm trả trợ cấp thôi việc cho người lao động đã làm việc thường xuyên cho mình từ đủ 12 tháng trở lên, mỗi năm làm việc được trợ cấp một nửa tháng tiền lương, trừ trường hợp đủ điều kiện hưởng lương hưu theo quy định của pháp luật về bảo hiểm xã hội và trường hợp quy định tại điểm e khoản 1 Điều 36 của Bộ luật này. 2. Thời gian làm việc để tính trợ cấp thôi việc là tổng thời gian người lao động đã làm việc thực tế cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiểm thất nghiệp theo quy định của pháp luật về bảo hiểm thất nghiệp và thời gian làm việc đã được người sử dụng lao động chỉ trả trợ cấp thôi việc, trợ cấp mất việc làm. 3 Tiền lương để tính trợ cấp thôi việc là tiền lương bình quân c

> **[a099008554b28f45]** blld-2012 · Điều 48 · trang [15, 16]
>
> Điều 48. Trợ cấp thôi việc 1. Khi hợp đồng lao động chấm dứt theo quy định tại các khoản 1,2,3, 5,6, 7, 9 và 10 Điều 36 của Bộ luật này thì người sử dụng lao động có trách nhiệm chi trả trợ cấp thôi việc cho người lao động đã làm việc thường xuyên từ đủ 12 tháng trở lên, mỗi năm làm việc được trợ cấp một nửa tháng tiền lương. 2. Thời gian làm việc đề tính trợ cấp thôi việc là tổng thời gian người lao động đã làm việc thực tế cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiểm thất nghiệp theo quy định của Luật bảo hiểm xã hội và thời gian làm việc đã được người sử dụng lao động chỉ trả trợ cấp thôi việc. ló 3. Tiền lương đề tính trợ cấp thôi việc là tiền lương bình quân theo hợp đồng lao động của 06 tháng liên kê trước khi người lao động thôi việc.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q10 · status `answered`

**Câu hỏi:** Người lao động bị mất việc làm được nhận trợ cấp tối thiểu bằng bao nhiêu tháng lương?

**Kỳ vọng:** Mỗi năm làm việc trả 01 tháng tiền lương nhưng ít nhất bằng 02 tháng tiền lương.

**Agent trả lời:** Người lao động bị mất việc làm được nhận trợ cấp mất việc làm tối thiểu bằng 02 tháng tiền lương [e174576b407acec5].

**Lượt tìm:** `trợ cấp thôi việc tối thiểu tháng lương` (filter None, none)

> **[e174576b407acec5]** blld-2012 · Điều 49 · trang [16]
>
> Điều 49. Trợ cấp mất việc làm ]. Người sử dụng lao động trả trợ cấp mất việc làm cho người lao động đã làm việc thường xuyên cho mình từ 12 tháng trở lên mà bị mất việc làm theo quy định tại Điều 44 và Điều 45 của Bộ luật này, mỗi năm làm việc trả 0] tháng tiền lương nhung ít nhất phải bằng 02 tháng tiền lương. 2. Thời gian làm việc để tính trợ cấp mắt việc làm là tông thời gian người lao động đã làm việc thực tê cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiêm thật nghiệp theo quy định của Luật bảo hiêm xã hội và thời gian làm việc đã được người sử dụng lao động ch trả trợ cấp thôi việc. mm Tiền lương để tính trợ cấp mất việc làm là tiền lương bình quân theo hợp đông lao động của 06 tháng liên kê trước khi người lao động mât việc làm.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q11 · status `answered`

**Câu hỏi:** Khi chấm dứt hợp đồng lao động, thời hạn thanh toán các khoản tiền giữa hai bên có thể được kéo dài tối đa bao nhiêu ngày?

**Kỳ vọng:** Không quá 30 ngày (bản 2019: chỉ trong các trường hợp liệt kê tại khoản 1 Điều 48; bản 2012: trường hợp đặc biệt).

**Agent trả lời:** Theo Bộ luật Lao động 2012, thời hạn thanh toán các khoản tiền giữa hai bên khi chấm dứt hợp đồng lao động là 07 ngày làm việc, có thể kéo dài nhưng không quá 30 ngày [0cbc2d076afca5c4].

Theo Bộ luật Lao động 2019, thời hạn thanh toán là 14 ngày làm việc, trừ các trường hợp đặc biệt có thể kéo dài nhưng không quá 30 ngày [2a48cb65dea01121].

**Lượt tìm:** `thanh toán tiền lương và các khoản tiền khác khi chấm dứt hợp đồng lao động thời hạn` (filter None, none)

> **[0cbc2d076afca5c4]** blld-2012 · Điều 47 · trang [15]
>
> Điều 47. Trách nhiệm của người sử dụng lao động khi chấm dứt hợp đồng lao động ]. Ít nhất 15 ngày trước ngày hợp đồng lao động xác định thời hạn hết hạn, người sử dụng lao động phải thông báo bằng văn bản cho người lao động biết thời điểm chấm dứt hợp đồng lao động. 2. Trong thời hạn 07 ngày làm việc, kể từ ngày chấm dứt hợp đồng lao động, hai bên có trách nhiệm thanh toán đây đủ các khoản có liên quan đến quyền lợi của mỗi bên; trường hợp đặc biệt, có thể kéo dài nhưng không được quá 30 ngày. 3. Người sử dụng lao động có trách nhiệm hoàn thành thủ tục xác nhận và trả lại sô bảo hiêm xã hội và những giây tờ khác mà người sử dụng lao động đã giữ lại của người lao động. 4. Trong trường hợp doanh nghiệp, hợp tác xã bị chấm dứt hoạt động, bị giải thể, phá sản thì tiền lương, trợ cấp thôi việc, bảo hiểm xã hội, bảo hiểm y tế, bảo hiểm thất nghiệp và các quyền lợi khác của người lao động theo 

> **[2a48cb65dea01121]** blld-2019 · Điều 48 · trang [19, 20]
>
> Điều 48. Trách nhiệm khi chấm dứt hợp đồng lao động 1. Trong thời hạn 14 ngày làm việc. kể từ ngày chấm đứt hợp đồng lao động, hai bên có trách nhiệm thanh toán đầy đủ các khoản tiền có liên quan đến quyền lợi của mỗi bên, trừ trường hợp sau đây có thể kéo đài nhưng không được quá 30 ngày: a) Người sử dụng lao động không phải là cá nhân chấm dứt hoạt động; b) Người sử dụng lao động thay đổi cơ cầu, công nghệ hoặc vì lý do kinh tế; c) Chia, tách, hợp nhất, sáp nhập; bán, cho thuê, chuyển đổi loại hình doanh nghiệp; chuyên nhượng quyền sở hữu, quyên sử dụng tài sản của doanh nghiệp, hợp tác xã; d) Do thiên tai, hỏa hoạn, địch họa hoặc dịch bệnh nguy hiểm. 2. Tiền lương, bảo hiểm xã hội, bảo hiểm y tế, bảo hiểm thất nghiệp, trợ cấp thôi việc và các quyên lợi khác của người lao động theo thỏa ước lao động tập thê, hợp đông lao động được ưu tiên thanh toán trong trường hợp doanh nghiệp, hợp t

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q12 · status `answered`

**Câu hỏi:** Giờ làm việc ban đêm được tính từ mấy giờ đến mấy giờ?

**Kỳ vọng:** Từ 22 giờ đến 06 giờ sáng ngày hôm sau.

**Agent trả lời:** Giờ làm việc ban đêm được tính từ 22 giờ đến 06 giờ sáng ngày hôm sau theo quy định tại Điều 106 Bộ luật Lao động 2019 [f8097e0a7bdcadcf].

Cũng theo Điều 105 Bộ luật Lao động 2012, giờ làm việc ban đêm được tính từ 22 giờ đến 6 giờ sáng ngày hôm sau [43ef3ba1a0f56f9c].

**Lượt tìm:** `giờ làm việc ban đêm` (filter None, none)

> **[f8097e0a7bdcadcf]** blld-2019 · Điều 106 · trang [40]
>
> Điều 106. Giờ làm việc ban đêm Giờ làm việc ban đêm được tính từ 22 giờ đến 06 giờ sáng ngày hôm sau.

> **[43ef3ba1a0f56f9c]** blld-2012 · Điều 105 · trang [30]
>
> Điều 105. Giờ làm việc ban đêm Giờ làm việc ban đêm được tính từ 22 giờ đến 6 giờ sáng ngày hôm sau.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q13 · status `answered`

**Câu hỏi:** Người làm ca đêm được nghỉ giữa ca ít nhất bao nhiêu phút?

**Kỳ vọng:** Ít nhất 45 phút (bản 2019 ghi rõ là 45 phút liên tục).

**Agent trả lời:** Người làm ca đêm được nghỉ giữa ca ít nhất 45 phút liên tục theo quy định tại Điều 109 của Bộ luật Lao động 2019 [5a45954688b086dc].

**Lượt tìm:** `nghỉ giữa ca người làm ca đêm` (filter None, none)

> **[5a45954688b086dc]** blld-2019 · Điều 109 · trang [41]
>
> Điều 109. Nghĩ trong giờ làm việc 1. Người lao động làm việc theo thời giờ làm việc quy định tại Điều 105 của Bộ luật này từ 06 giờ trở lên trong một ngày thì được nghỉ giữa giờ ít nhất 30 phút liên tục, làm việc ban đêm thì được nghỉ giữa giờ ít nhất 45 phút liên tục. Trường hợp người lao động làm việc theo ca liên tục từ 06 giờ trở lên thì thời gian nghỉ giữa giờ được tính vào giờ làm việc. 2. Ngoài thời gian nghỉ quy định tại khoản 1 Điều này, người sử dụng lao động bố trí cho người lao động các đợt nghỉ giải lao và ghi vào nội quy lao động.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q14 · status `answered`

**Câu hỏi:** Người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bao nhiêu?

**Kỳ vọng:** Ít nhất bằng 300%, chưa kể tiền lương ngày lễ đối với người lao động hưởng lương ngày.

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bằng 300% chưa kể tiền lương ngày lễ, tết, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày [8bf032c21470d951].

Theo Bộ luật Lao động 2012, người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bằng 300% chưa kể tiền lương ngày lễ, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày [43cd550df5a10ee9].

**Lượt tìm:** `làm thêm giờ ngày nghỉ lễ trả lương` (filter None, none)

> **[8bf032c21470d951]** blld-2019 · Điều 98 · trang [37]
>
> Điều 98. Tiền lương làm thêm giờ, làm việc vào ban đêm 1. Người lao động làm thêm giờ được trả lương tính theo đơn giá tiền lương hoặc tiền lương thực trả theo công việc đang làm như sau: a) Vào ngày thường, ít nhất bằng 150%; b) Vào ngày nghỉ hằng tuần, ít nhất bằng 200%; c) Vào ngày nghỉ lễ, tết, "ngày nghỉ có hưởng lương, ít nhất bằng 300% chưa kể tiền lương ngày lễ, tết, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày. 2. _Người lao động làm việc vào ban đêm thì được trả thêm ít nhất bằng 30% tiền lương tính theo đơn giá tiền lương hoặc tiền lương thực trả theo công việc của ngày làm việc bình thường. 3. Người lao động làm thêm giờ vào ban đêm thì ngoài việc trả lương theo quy định tại khoản 1 và khoản 2 Điều này, người lao động còn được trả thêm 20% tiền lương tính theo đơn giá tiền lương hoặc tiền lương theo công việc làm vào ban ngày của ngày làm việc bình thường 

> **[43cd550df5a10ee9]** blld-2012 · Điều 97 · trang [28, 29]
>
> Điều 97. Tiền lương làm thêm giờ, làm việc vào ban đêm 1. Người lao động làm thêm giờ được trả lương tính theo đơn giá tiền lương hoặc tiên lương theo công việc đang làm như sau: a) Vào ngày thường, ít nhất bằng 150%; b) Vào ngày nghỉ hằng tuần, ít nhất bằng 200%; c) Vào ngày nghỉ lễ, ngày nghỉ có hưởng lương, ít nhất băng 300% chua kể tiền lương ngày lễ, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày. 2. Người lao động làm việc vào ban đêm, thì được trả thêm ít nhất băng 30% tiền lương tính theo đon giá tiền lương hoặc tiền lương theo công việc của ngày làm việc bình thường. 3. Người lao động làm thêm giờ vào ban đêm thì ngoài việc trả lương theo quy định tại khoản 1 và khoản 2 Điều này, người lao động còn được trả thêm 20% tiền lương tính theo đơn giá tiền lương hoặc tiền lương theo công việc làm vào ban ngày.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q15 · status `answered`

**Câu hỏi:** Người làm công việc nặng nhọc, độc hại, nguy hiểm được nghỉ hằng năm bao nhiêu ngày?

**Kỳ vọng:** 14 ngày làm việc (16 ngày nếu là công việc đặc biệt nặng nhọc, độc hại, nguy hiểm).

**Agent trả lời:** Người lao động làm công việc nặng nhọc, độc hại, nguy hiểm được nghỉ hằng năm 14 ngày làm việc.

Căn cứ:
- Bộ luật Lao động 2012, Điều 111, khoản 1, điểm b) [b268f97122b4fcbd]: "14 ngày làm việc đối với người làm công việc nặng nhọc, độc hại, nguy hiểm...".
- Bộ luật Lao động 2019, Điều 113, khoản 1, điểm b) [3fe27b9fd53b4099]: "14 ngày làm việc đối với... người làm nghề, công việc nặng nhọc, độc hại, nguy hiểm".

**Lượt tìm:** `nghỉ hằng năm người lao động làm công việc nặng nhọc độc hại nguy hiểm` (filter None, none)

> **[b268f97122b4fcbd]** blld-2012 · Điều 111 · trang [32]
>
> Điều 111. Nghỉ hằng năm 1. Người lao động có đủ 12 tháng làm việc cho một người sử dụng lao động thì được nghỉ hăng năm, hưởng nguyên lương theo hợp đông lao động như sau: a) 12 ngày làm việc đối với người làm công việc trong điều kiện bình thường: b) 14 ngày làm việc đối với người làm công việc nặng nhọc, độc hại, nguy hiểm hoặc người làm việc ở những nơi có có điều kiện sinh sống khắc nghiệt theo danh mục do Bộ Lao động - Thương binh và Xã hội chủ trì phối hợp với Bộ Y tế ban hành hoặc lao động chưa thành niên hoặc lao động là người khuyêt tật; c) 16 ngày làm việc đối với người làm công việc đặc biệt nặng nhọc, độc hại, nguy hiểm hoặc người làm việc ở những nơi có điều kiện sinh sống đặc biệt khắc nghiệt theo danh mục do Bộ Lao động - Thương bình và Xã hội chủ trì ì phối hợp với Bộ Y tế ban hành. 2. Người sử dụng lao động có quyền quy định lịch nghi hằng năm sau khi tham khảo ý kiên củ

> **[3fe27b9fd53b4099]** blld-2019 · Điều 113 · trang [42]
>
> Điều 113. Nghĩ hằng năm l 1. Người lao động làm việc đủ 12 tháng cho một người sử dụng lao động thì được nghỉ hăng năm, hưởng nguyên lương theo hợp đông lao động như sau: a) 12 ngày làm việc đối với người làm công việc trong điều kiện bình thường: b) 14 ngày làm việc đối với người lao động chưa thành niên, lao động là người khuyêt tật, người làm nghề, công việc nặng nhọc, độc hại, nguy hiểm; c) 16 ngày làm việc đối với người làm nghề, công việc đặc biệt nặng nhọc, độc hại, nguy hiêm. 2. Người lao động làm việc chưa đủ 12 tháng cho một người sử dụng lao động thì sô ngày nghỉ hăng năm theo tỷ lệ tương ứng với sô tháng làm việc. 3. Trường hợp do thôi việc, bị mất việc làm mà chưa nghỉ hằng năm hoặc chưa nghỉ hết số ngày nghỉ hăng năm thì được người sử dụng lao động thanh toán tiên lương cho những ngày chưa nghỉ... 4. Người sử dụng lao động có trách nhiệm quy định lịch nghỉ hằng năm sau khi 

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q16 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2012, người lao động được hưởng lương hưu khi đủ bao nhiêu tuổi?

**Kỳ vọng:** Nam đủ 60 tuổi, nữ đủ 55 tuổi (khi bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội).

**Agent trả lời:** Theo Bộ luật Lao động 2012, người lao động được hưởng lương hưu khi nam đủ 60 tuổi, nữ đủ 55 tuổi [67976ce3fa4d3293].

**Lượt tìm:** `tuổi hưởng lương hưu người lao động` (filter {'year': 2012}, user)

> **[67976ce3fa4d3293]** blld-2012 · Điều 187 · trang [52]
>
> Điều 187. Tuổi nghỉ hưu 1. Người lao động bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội theo quy định của pháp luật về bảo hiểm xã hội được hưởng lương hưu khi nam đủ 60 tuổi, nữ đủ 55 tuổi. 2. Người lao động bị suy giảm khả năng lao động; làm công việc đặc biệt nặng nhọc, độc hại, nguy hiểm; làm công việc nặng nhọc, độc hại, nguy hiểm; làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo thuộc danh mục do Chính phủ quy định có thể nghỉ hưu ở tuổi thấp hơn so với quy định tại khoản 1 Điều này. 3. Người lao động có trình độ chuyên môn kỹ thuật cao, người lao động làm công tác quản lý và một số trường hợp đặc biệt khác có thể nghỉ hưu ở tuổi cao hơn nhưng không quá 05 năm so với quy định tại khoản 1 Điều này. 4. Chính phủ quy định chi tiết khoản 2 và khoản 3 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q17 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, từ năm 2021 tuổi nghỉ hưu của lao động nữ trong điều kiện lao động bình thường là bao nhiêu?

**Kỳ vọng:** Đủ 55 tuổi 04 tháng; sau đó mỗi năm tăng thêm 04 tháng cho đến khi đủ 60 tuổi vào năm 2035.

**Agent trả lời:** Theo Bộ luật Lao động 2019, từ năm 2021, tuổi nghỉ hưu của lao động nữ trong điều kiện lao động bình thường là đủ 55 tuổi 04 tháng [c40fad20889e6976].

**Lượt tìm:** `tuổi nghỉ hưu lao động nữ điều kiện lao động bình thường` (filter {'year': 2019}, user)

> **[c40fad20889e6976]** blld-2019 · Điều 169 · trang [60]
>
> Điều 169. Tuổi nghỉ hưu 1. Người lao động bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội theo quy định của pháp luật về bảo hiểm xã hội được hưởng lương hưu khi đủ tuôi nghỉ hưu. 2. Tuổi nghỉ hưu của người lao động trong điều kiện lao động bình thường được điều chỉnh theo lộ trình cho đên khi đủ 62 tuổi đối với lao động nam vào năm 2028 và đủ 60 tuôi đôi với lao động nữ vào năm 2035. Kể từ năm 2021, tuổi nghỉ hưu của người lao động trong điều kiện lao động bình thường là đủ 60 tuổi 03 tháng đối với lao động nam và đủ 55 tuổi 04 tháng đối với lao động nữ; sau đó, cứ mỗi năm tăng thêm 03 tháng đối với lao động nam và 04 tháng đối với lao động nữ. 3. Người lao động bị suy giảm khả năng lao động; làm nghề, công việc đặc biệt nặng nhọc, độc hại, nguy hiểm; làm nghề, công việc nặng nhọc, độc hại, nguy hiểm; làm việc ở vùng có điều kiện kinh tế - xã hội đặc biệt khó khăn có thể nghỉ hưu ở 

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q18 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, người lao động được nghỉ bao nhiêu ngày vào dịp Quốc khánh?

**Kỳ vọng:** 02 ngày (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau).

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động được nghỉ 02 ngày vào dịp Quốc khánh (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau) [70c23213ef936eb5].

**Lượt tìm:** `nghỉ lễ Quốc khánh` (filter {'year': 2019}, user)

> **[70c23213ef936eb5]** blld-2019 · Điều 112 · trang [41, 42]
>
> Điều 112. Nghỉ lễ, tết 1. Người lao động được nghỉ làm việc, hưởng nguyên lương trong những ngày lỗ, tết sau đây: a) Tết Dương lịch: 01 ngày (ngày 01 tháng 01 đương lịch); b) Tết Âm lịch: 05 ngày; c) Ngày Chiến thắng: 01 ngày (ngày 30 tháng 4 dương lịch); d) Ngày Quốc tế lao động: 01 ngày (ngày 01 tháng 5 dương lịch); đ) Quốc khánh: 02 ngày (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau); e) Ngày Giỗ Tổ Hùng Vương: 01 ngày (ngày 10 tháng 3 âm lịch). 2. Lao động là người nước ngoài làm việc tại Việt Nam ngoài các ngày nghỉ theo quy định tại khoản 1 Điều này còn được nghỉ thêm 01 ngày Tết cổ truyền dân tộc và 01 ngày Quốc khánh của nước họ. 3. Hằng năm, căn cứ vào điều kiện thực tế, Thủ tướng Chính phủ quyết định cụ thể ngày nghỉ quy định tại điêm b và điểm đ khoản 1 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q19 · status `answered`

**Câu hỏi:** Nếu nhân viên vi phạm liên quan trực tiếp đến tài sản của công ty thì thời hiệu xử lý kỷ luật lao động là bao lâu?

**Kỳ vọng:** 12 tháng (thay vì 06 tháng như thông thường).

**Agent trả lời:** Theo Bộ luật Lao động 2019, thời hiệu xử lý kỷ luật lao động đối với hành vi vi phạm liên quan trực tiếp đến tài sản của người sử dụng lao động là 12 tháng [ddd5e6ef6c45d7a2].

Theo Bộ luật Lao động 2012, thời hiệu xử lý kỷ luật lao động đối với hành vi vi phạm liên quan trực tiếp đến tài sản của người sử dụng lao động là 12 tháng [4829c9234e35ab72].

**Lượt tìm:** `thời hiệu xử lý kỷ luật lao động vi phạm tài sản` (filter None, none)

> **[ddd5e6ef6c45d7a2]** blld-2019 · Điều 123 · trang [46]
>
> Điều 123. Thời hiệu xử lý kỷ luật lao động 1. Thời hiệu xử lý kỷ luật lao động là 06 tháng kể từ ngày xảy ra hành vi vi phạm; trường hợp hành vi vi phạm liên quan trực tiếp đến tài chính, tài sản, tiệt lộ bí mật công nghệ, bí mật kinh doanh của người sử dụng lao động thì thời hiệu xử lý kỷ luật lao động là 12 tháng. 2. Khi hết thời gian quy định tại khoản 4 Điều 122 của Bộ luật này, nếu hết thời hiệu hoặc còn thời hiệu nhưng không đủ 60 ngày thì được kéo dài thời hiệu đê xử lý kỷ luật lao động nhưng không quá 60 ngày kề từ ngày hết thời gian nêu trên. 3. Người sử dụng lao động phải ban hành quyết định xử lý kỷ luật lao động trong thời hạn quy định tại khoản 1 và khoản 2 Điều này.

> **[4829c9234e35ab72]** blld-2012 · Điều 124 · trang [35, 36]
>
> Điều 124. Thời hiệu xử lý kỷ luật lao động 1. Thời hiệu xử lý kỷ luật lao động tối đa là 06 tháng, kể từ ngày xảy ra hành vi vi phạm; trường hợp hành vi vi phạm liên quan trực tiếp đến tài chính, tài sản, tiết lộ bí mật công nghệ, bí mật kinh doanh của người sử dụng lao động thì thời hiệu xử lý kỷ luật lao động tối đa là 12 tháng. 2. Khi hết thời gian quy định tại các điểm a, b và c khoản 4 Điều 123, nếu còn thời hiệu đề xử lý kỷ luật lao động thì người sử dụng lao động tiền hành xử lý kỹ luật lao động ngay, nếu hết thời hiệu thì được kéo dài thời hiệu để xử lý kỷ luật lao động nhưng tôi đa không quá 60 ngày kế từ ngày hết thời gian nêu trên. so Khi hết thời gian quy định tại điểm d khoản 4 Điều 123, mà thời hiệu xử lý kỷ luật lao động đã hết thì được kéo dài thời hiệu xử lý kỷ luật lao động nhưng tôi đa không quá 60 ngày kê từ ngày hết thời gian nêu trên. 3. Quyết định xử lý kỷ luật lao

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · q20 · status `answered`

**Câu hỏi:** Lao động nữ mang thai làm việc ở vùng cao hoặc hải đảo không được bố trí làm việc ban đêm kể từ tháng thai thứ mấy?

**Kỳ vọng:** Từ tháng thứ 06 (thay vì tháng thứ 07 như nơi khác).

**Agent trả lời:** Lao động nữ mang thai làm việc ở vùng cao hoặc hải đảo không được bố trí làm việc ban đêm kể từ tháng thai thứ 06.

Căn cứ:
- Bộ luật Lao động 2012, Điều 155, khoản 1, điểm a [ffe02f16c93fddb4].
- Bộ luật Lao động 2019, Điều 137, khoản 1, điểm a [53201ad6737fab80].

**Lượt tìm:** `lao động nữ mang thai vùng cao hải đảo không được bố trí làm việc ban đêm` (filter None, none)

> **[ffe02f16c93fddb4]** blld-2012 · Điều 155 · trang [44]
>
> Điều 155. Bảo vệ thai sản đối với lao động nữ 1. Người sử dụng lao động không được sử dụng lao động nữ làm việc ban đêm, làm thêm giờ và đi công tác xa trong các trường hợp sau đây: a) Mang thai từ tháng thứ 07 hoặc từ tháng thứ 06 nếu làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo; b) Đang nuôi con dưới 12 tháng tuổi. 2. Lao động nữ làm công việc nặng nhọc khi mang thai từ tháng thứ 07, được chuyển làm công việc nhẹ hơn hoặc được giảm bớt 01 giờ làm việc hằng ngày mà vân hưởng đủ lương. 3. Người sử dụng lao động không được sa thải hoặc đơn phương chấm dứt hợp đồng lao động đối với lao động nữ vì lý do kết hôn, mang thai, nghỉ thai sản, nuôi con dưới 12 tháng tuổi, trừ trường hợp người sử dụng lao động là cá nhân chết, bị Tòa án tuyên bố mất năng lực hành vi dân sự, mât tích hoặc là đã chết hoặc người sử dụng lao động không phải là cá nhân chấm dứt hoạt động. 4. Trong thời gi

> **[53201ad6737fab80]** blld-2019 · Điều 137 · trang [50]
>
> Điều 137. Bảo vệ thai sản 1. Người sử dụng lao động không được sử dụng người lao động làm việc ban đêm, làm thêm giờ và đi công tác xa trong trường hợp sau đây: a) Mang thai từ tháng thứ 07 hoặc từ tháng thứ 06 nếu làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo; b) Đang nuôi con đưới 12 tháng tuổi, trừ trường hợp được người lao động đồng ý. 2. Lao động nữ làm nghề, công việc nặng nhọc, độc hại, nguy hiểm hoặc đặc biệt nặng nhọc, độc hại, nguy hiêm hoặc làm nghề, công việc có ảnh hưởng xâu tới chức năng sinh sản và nuôi con khi mang thai và có thông báo cho người sử dụng lao động biết thì được người sử dụng lao động chuyển sang làm công việc nhẹ hơn, an toàn hơn hoặc giảm bớt 01 giờ làm việc hằng ngày mà không bị cắt giảm tiền lương và quyền, lợi ích cho đến hết thời gian nuôi con dưới 12 tháng tuổi,

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · u01 · status `answered`

**Câu hỏi:** Mức lương tối thiểu vùng I hiện nay là bao nhiêu đồng một tháng?

**Kỳ vọng:** (thiếu bằng chứng) Cả hai bộ luật chỉ nói mức lương tối thiểu (vùng) do Chính phủ quy định/công bố; không có con số tiền nào.

**Agent trả lời:** Bộ luật Lao động 2019 quy định về mức lương tối thiểu nhưng không nêu cụ thể con số. Con số này được Chính phủ ban hành trong các quyết định riêng biệt.

Theo Điều 91 Bộ luật Lao động 2019, mức lương tối thiểu được xác lập theo vùng và ấn định theo tháng [43fdabab0f59a94e].

Tuy nhiên, Bộ luật Lao động không ghi rõ mức lương tối thiểu vùng I hiện tại là bao nhiêu. Mức lương này được Chính phủ quy định chi tiết và công bố trong các văn bản pháp luật riêng (như Quyết định của Chính phủ).

**Lượt tìm:** `mức lương tối thiểu vùng` (filter {'year': 2019}, inferred)

> **[43fdabab0f59a94e]** blld-2019 · Điều 91 · trang [35]
>
> Điều 91. Mức lương tối thiếu 1. Mức lương tối thiểu là mức lương thấp nhất được trả cho người lao động làm công việc giản đơn nhất trong điều kiện lao động bình thường nhằm bảo đảm mức sống tối thiểu của người lao động và gia đình họ, phà hợp với điều kiện phát triển kinh tế - xã hội. 2. Mức lương tối thiểu được xác lập theo vùng, ấn định theo tháng, giờ. 3. Mức lường tối thiểu được điều chỉnh dựa trên mức sống tối thiểu của người lao động và gia đình họ; tương quan giữa mức lương tối thiểu và mức lương trên thị trường; chỉ số giá tiêu dùng, tốc độ tăng trưởng kinh tế; quan hệ cung, cầu lao động: việc làm và thất nghiệp; năng suất lao động; khả năng chỉ trả của doanh nghiệp. 4. Chính phủ quy định chi tiết Điều này; quyết định và công bố mức lương tối thiểu trên cơ sở khuyến nghị của Hội đồng tiền lương quốc gia.

*Nháp AI:* grade= · citation=true · abstention=false · Nội dung về bản chất là đúng (bộ luật không có con số), nhưng agent TRẢ LỜI có citation (status answered) thay vì từ chối theo quy ước, và thêm ý ngoài evidence ('Chính phủ ban hành trong các quyết định riêng'). Citation Điều 91 hỗ trợ ý 'xác lập theo vùng, ấn định theo tháng'.

## agent_dense_k3 · u02 · status `abstain`

**Câu hỏi:** Người sử dụng lao động phải đóng bảo hiểm xã hội bắt buộc bằng bao nhiêu phần trăm quỹ tiền lương?

**Kỳ vọng:** (thiếu bằng chứng) Bộ luật chỉ quy định nghĩa vụ tham gia/đóng bảo hiểm xã hội theo pháp luật về bảo hiểm xã hội; không có tỷ lệ đóng.

**Agent trả lời:** Các đoạn tìm được trong Bộ luật Lao động 2012 và 2019 không nêu cụ thể tỷ lệ phần trăm người sử dụng lao động phải đóng bảo hiểm xã hội bắt buộc. Thông tin này thường được quy định trong Luật Bảo hiểm xã hội và các văn bản hướng dẫn thi hành.

Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời.

**Lượt tìm:** `tỷ lệ đóng bảo hiểm xã hội bắt buộc người sử dụng lao động` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối đúng, không đưa tỷ lệ nào. Có thêm câu 'thường quy định trong Luật BHXH/văn bản hướng dẫn', ý này khớp với dẫn chiếu 'theo pháp luật về BHXH' trong bộ luật. CẦN NGƯỜI DUYỆT (quy tắc: không thêm khẳng định vô căn cứ).

## agent_dense_k3 · u03 · status `abstain`

**Câu hỏi:** Người lao động làm việc từ xa tại nhà được hưởng phụ cấp bao nhiêu mỗi tháng?

**Kỳ vọng:** (thiếu bằng chứng) Không bộ luật nào quy định làm việc từ xa hay phụ cấp cho hình thức này.

**Agent trả lời:** Bộ luật Lao động 2019 và 2012 không quy định cụ thể mức phụ cấp cho người lao động làm việc từ xa tại nhà. Các điều luật tìm được chỉ đề cập đến việc người lao động có thể thỏa thuận nhận việc về làm tại nhà, nhưng không nêu rõ về phụ cấp hay mức lương cụ thể cho hình thức này.

Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời.

**Lượt tìm:** `phụ cấp làm việc từ xa tại nhà` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối đúng, không đưa con số phụ cấp. Câu giải thích (nếu có) chỉ nói bộ luật không quy định.

## agent_hybrid_rrf · q01 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, hai bên được giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn bao lâu?

**Kỳ vọng:** Hợp đồng có thời hạn dưới 01 tháng (trừ các trường hợp tại khoản 2 Điều 18, điểm a khoản 1 Điều 145 và khoản 1 Điều 162).

**Agent trả lời:** Theo Bộ luật Lao động 2019, hai bên được giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn dưới 01 tháng [410ba0a07076ab8d].

**Lượt tìm:** `hợp đồng lao động bằng lời nói thời hạn` (filter {'year': 2019}, user)

> **[410ba0a07076ab8d]** blld-2019 · Điều 14 · trang [6, 7]
>
> Điều 14. Hình thức hợp đồng lao động 1. Hợp đồng lao động phải được giao kết bằng văn bản và được làm thành 02 bản, người lao động giữ 01 bản, người sử dụng lao động giữ 01 bản, trừ trường hợp quy định tại khoản 2 Điều này. Hợp đồng lao động được giao kết thông qua phương tiện điện tử dưới hình thức thông điệp dữ liệu theo quy định của pháp luật về giao dịch điện tử có giá trị như bợp đồng lao động bằng văn bản. 2. Hai bên có thể giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn dưới 01 tháng, trừ trường hợp quy định tại khoản 2 Điều 18, điểm a khoản 1 Điều 145 và khoản 1 Điều 162 của Bộ luật này. Ss

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q02 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2012, công việc tạm thời có thời hạn bao lâu thì các bên được giao kết hợp đồng bằng lời nói?

**Kỳ vọng:** Công việc tạm thời có thời hạn dưới 03 tháng.

**Agent trả lời:** Theo Bộ luật Lao động 2012, các bên được giao kết hợp đồng lao động bằng lời nói đối với công việc tạm thời có thời hạn dưới 03 tháng [8b35e2d37ae827ce].

**Lượt tìm:** `hợp đồng bằng lời nói công việc tạm thời thời hạn` (filter {'year': 2012}, user)

> **[8b35e2d37ae827ce]** blld-2012 · Điều 16 · trang [6]
>
> Điều 16. Hình thức hợp đồng lao động 1. Hợp đồng lao động phải được giao kết bằng văn bản và được làm thành 02 bản, người lao động giữ 01 bản, người sử dụng lao động giữ 01 bản, trừ trường hợp quy định tại khoản 2 Điều này. 2. Đối với công việc tạm thời có thời hạn dưới 03 tháng, các bên có thể giao kết hợp đồng lao động bằng lời nói.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q03 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, số giờ làm thêm của người lao động tối đa trong một tháng là bao nhiêu?

**Kỳ vọng:** Không quá 40 giờ trong 01 tháng (và không quá 200 giờ/năm, trừ các trường hợp được làm đến 300 giờ/năm).

**Agent trả lời:** Theo Bộ luật Lao động 2019, số giờ làm thêm của người lao động tối đa trong một tháng là **40 giờ**.

Căn cứ:
- Điều 107, khoản 2, điểm b) quy định: "không quá 40 giờ trong 01 tháng" [71267d6e72a8bf88].

**Lượt tìm:** `số giờ làm thêm tối đa trong một tháng` (filter {'year': 2019}, user)

> **[71267d6e72a8bf88]** blld-2019 · Điều 107 · trang [40]
>
> Điều 107. Làm thêm giờ 1. Thời gian làm thêm giờ là khoảng thời gian làm việc ngoài thời giờ làm việc bình thường theo quy định của pháp luật, thỏa ước lao động tập thê hoặc nội quy lao động. 2. Người sử dụng lao động được sử dụng người lao động làm thêm giờ khi đáp ứng đây đủ các yêu câu sau đây: a) Phải được sự đồng ý của người lao động: b) Bảo đảm số giờ làm thêm của người lao động không quá 50% số giờ làm việc bình thường trong 01 ngày; trường hợp áp dụng quy định thời giờ làm việc bình thường theo tuân thì tổng số giờ làm việc bình thường và số giờ làm thêm không quá 12 giờ trong 01 ngày; không quá 40 giờ trong 01 tháng: c) Bảo đảm số giờ làm thêm của người lao động không quá 200 giờ trong 01 năm, trừ trường hợp quy định tại khoản 3 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q04 · status `answered`

**Câu hỏi:** Bộ luật Lao động 2012 giới hạn số giờ làm thêm trong một tháng là bao nhiêu?

**Kỳ vọng:** Không quá 30 giờ trong 01 tháng.

**Agent trả lời:** Theo Bộ luật Lao động 2012, số giờ làm thêm của người lao động không quá 30 giờ trong một tháng [3b164eb9c075d12a].

**Lượt tìm:** `giới hạn số giờ làm thêm trong một tháng` (filter {'year': 2012}, user)

> **[3b164eb9c075d12a]** blld-2012 · Điều 106 · trang [30, 31]
>
> Điều 106. Làm thêm giờ 1. Làm thêm giờ là khoảng thời gian làm việc ngoài thời giờ làm việc bình thường được quy định trong pháp luật, thỏa ước lao động tập thể hoặc theo nội quy. lao động. 2. Người sử dụng lao động được sử dụng người lao động làm thêm giờ khi đáp ứng đủ các điều kiện sau đây: a) Được sự đồng ý của người lao động: b) Bảo đảm số giờ làm thêm của người lao động không quá 50% số giờ làm việc bình thuờng trong 01 ngày, trường hợp áp dụng quy định làm việc theo tuần thì tông số giờ làm việc bình thường và số giờ làm thêm không quá 12 giờ trong 01 ngày, không quá 30 giờ trong 0] tháng và tông sô không quá 200 giờ trong 01 năm, trừ một sô trường hợp đặc biệt do Chính phủ quy định thì được làm thêm giờ không quá 300 giờ trong 01 năm; c) Sau mỗi đợt làm thêm giờ nhiều ngày liên tục trong tháng, người sử dụng lao động phải bô trí đề người lao động được nghỉ bù cho sô thời gian đã 

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q05 · status `answered`

**Câu hỏi:** Người được tuyển vào vị trí quản lý doanh nghiệp có thể phải thử việc tối đa bao nhiêu ngày?

**Kỳ vọng:** Không quá 180 ngày (quy định của Bộ luật Lao động 2019; bản 2012 không có mức riêng cho người quản lý doanh nghiệp).

**Agent trả lời:** Người lao động nói chung có thể thử việc tối đa 12 tháng theo quy định tại Điều 24 Bộ luật Lao động 2019 [18875379609a900a]. Tuy nhiên, đối với người lao động làm công việc quản lý, thời gian thử việc tối đa là 18 tháng theo quy định tại Điều 24 Bộ luật Lao động 2019 [18875379609a900a].

**Lượt tìm:** `thử việc người lao động quản lý` (filter None, none)

> **[18875379609a900a]** blld-2019 · Điều 24 · trang [10]
>
> Điều 24. Thử việc 1. Người sử dụng lao động và người lao động có thể thỏa thuận nội dung thử việc ghi trong hợp đông lao động hoặc thỏa thuận về thử việc băng việc giao kêt hợp đông thử việc. 2. Nội dung chủ yếu của hợp đồng thử việc gồm thời gian thử việc và nội dung quy định tại các điểm a, b, c, đ, g vàh khoản 1 Điều 21 của Bộ luật này. 3. Không áp dụng thử việc đối với người lao động giao kết hợp đồng lao động có thời hạn dưới 01 tháng.

*Nháp AI:* grade=0 · citation=false · abstention= · '12 tháng' và 'quản lý 18 tháng' đều bịa; Điều 24/2019 không chứa các con số này; thiếu Điều 25.

## agent_hybrid_rrf · q06 · status `answered`

**Câu hỏi:** Tiền lương trong thời gian thử việc ít nhất phải bằng bao nhiêu phần trăm mức lương của công việc đó?

**Kỳ vọng:** Ít nhất bằng 85% mức lương của công việc đó (giống nhau ở bản 2012 và 2019).

**Agent trả lời:** Theo Bộ luật Lao động 2012, tiền lương trong thời gian thử việc ít nhất phải bằng 85% mức lương của công việc đó [fbeaa39254552433].

Theo Bộ luật Lao động 2019, tiền lương trong thời gian thử việc cũng ít nhất phải bằng 85% mức lương của công việc đó [0eeeb5f152e2ed3b].

**Lượt tìm:** `tiền lương thời gian thử việc tỷ lệ phần trăm mức lương công việc` (filter None, none)

> **[fbeaa39254552433]** blld-2012 · Điều 28 · trang [9]
>
> Điều 28. Tiền lương trong thời gian thử việc Tiền lương của người lao động trong thời gian thử việc do hai bên thoả thuận nhưng ít nhất phải bằng 85% mức lương của công việc đó.

> **[0eeeb5f152e2ed3b]** blld-2019 · Điều 26 · trang [10]
>
> Điều 26. Tiền lương thứ việc Tiền lương của người lao động trong thời gian thử việc do hai bên thỏa thuận nhưng ít nhất phải băng 85% mức lương của công việc đó.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q07 · status `answered`

**Câu hỏi:** Nhân viên ký hợp đồng không thời hạn muốn tự nghỉ việc thì phải báo trước cho công ty ít nhất bao lâu?

**Kỳ vọng:** Ít nhất 45 ngày (bản 2012 có ngoại lệ cho lao động nữ mang thai theo Điều 156).

**Agent trả lời:** Theo Bộ luật Lao động 2012 và 2019, người lao động muốn tự nghỉ việc (đơn phương chấm dứt hợp đồng lao động) với hợp đồng không thời hạn phải báo trước cho người sử dụng lao động ít nhất **30 ngày** đối với hợp đồng không thời hạn.

Căn cứ:
- Điều 40 Bộ luật Lao động 2012 [fceb706dab47570b]
- Điều 38 Bộ luật Lao động 2019 [67fae6f16fb865d5]
- Điều 43 Bộ luật Lao động 2012 [b83d05d1864f3e9d]

**Lượt tìm:** `tự thôi việc hợp đồng không thời hạn báo trước` (filter None, none)

> **[fceb706dab47570b]** blld-2012 · Điều 40 · trang [13]
>
> Điều 40. Huỷ bỏ việc đơn phương chấm dứt hợp đồng lao động Mỗi bên đều có quyền huỷ bỏ việc đơn phương chấm dứt hợp đồng lao động trước khi hết thời hạn báo trước nhưng phải thông báo bằng văn bản và phải được bên kia đồng ý.

> **[67fae6f16fb865d5]** blld-2019 · Điều 38 · trang [16]
>
> Điều 38. Hủy bỏ việc đơn phương chấm dứt hợp đồng lao động Mỗi bên đều có quyền hủy bỏ việc đơn phương chấm dứt hợp đồng lao động trước khi hết thời hạn báo trước nhưng phải thông báo băng văn bản và phải được bên kia đồng ý. :

> **[b83d05d1864f3e9d]** blld-2012 · Điều 43 · trang [14]
>
> Điều 43. Nghĩa vụ của người lao động khi đơn phương chấm dứt hợp đồng lao động trái pháp luật 1. Không được trợ cấp thôi việc và phải bồi thường cho người sử dụng lao động nửa tháng tiền lương theo hợp đồng lao động. 2. Nếu vi phạm quy định về thời hạn báo trước thì phải bồi thường cho người sử dụng lao động một khoản tiền tương ứng với tiền lương của người lao động trong những ngày không báo trước. 3. Phải hoàn trả chi phí đào tạo cho người sử dụng lao động theo quy định tại Điều 62 của Bộ luật này.

*Nháp AI:* grade=0 · citation=false;false;false · abstention= · Trả lời '30 ngày' là sai (đúng là 45 ngày). Cả 3 citation (Điều 40/2012, Điều 38/2019 về hủy bỏ; Điều 43/2012 về nghĩa vụ khi chấm dứt trái luật) đều không chứa thời hạn báo trước.

## agent_hybrid_rrf · q08 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, nếu người lao động bị trả lương không đúng thời hạn thì có phải báo trước khi đơn phương chấm dứt hợp đồng không?

**Kỳ vọng:** Không cần báo trước, trừ trường hợp quy định tại khoản 4 Điều 97.

**Agent trả lời:** Theo Bộ luật Lao động 2019, nếu người lao động bị trả lương không đúng thời hạn thì **không phải báo trước** khi đơn phương chấm dứt hợp đồng lao động.

Căn cứ:
- Điều 35 quy định về thời hạn báo trước khi người lao động đơn phương chấm dứt hợp đồng lao động [88d5dd520c3fcef6].
- Điều 39 và Điều 40 quy định về đơn phương chấm dứt hợp đồng lao động trái pháp luật và nghĩa vụ của người lao động khi đơn phương chấm dứt hợp đồng lao động trái pháp luật [2b82e938dbe5e213, ebea0c01b9dd25d1].
- Tuy nhiên, Bộ luật Lao động 2019 không quy định cụ thể về trường hợp người lao động bị trả lương không đúng thời hạn thì có quyền đơn phương chấm dứt hợp đồng lao động mà không cần báo trước. Do đó, người lao động vẫn phải tuân thủ quy định về thời hạn báo trước theo Điều 35 [88d5dd520c3fcef6].

**Lượt tìm:** `người lao động bị trả lương không đúng thời hạn đơn phương chấm dứt hợp đồng` (filter {'year': 2019}, user)

> **[88d5dd520c3fcef6]** blld-2019 · Điều 35 · trang [14]
>
> Điều 35. Quyền đơn phương chấm dứt hợp đồng lao động của người lao động 1. Người lao động có quyền đơn phương chấm dứt hợp đồng lao động nhưng phải báo trước cho người sử dụng lao động như sau: a) Ít nhất 45 ngày nếu làm việc theo hợp đồng lao động không xác định thời hạn; b) Ít nhất 30 ngày nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn từ 12 tháng đên 36 tháng: c) Ít nhất 03 ngày làm việc nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn dưới 12 tháng: d) Đối với một số ngành, nghề, công việc đặc thù thì thời hạn báo trước được thực hiện theo quy định của Chính phủ.

> **[2b82e938dbe5e213]** blld-2019 · Điều 39 · trang [16]
>
> Điều 39. Đơn phương chấm dứt hợp đồng lao động trái pháp luật Đơn phương chấm dứt hợp đồng lao động trái pháp luật là trường hợp châm dứt hợp đông lao động không đúng quy định tại các điêu 35, 36 và 37 của Bộ luật này.

> **[ebea0c01b9dd25d1]** blld-2019 · Điều 40 · trang [16]
>
> Điều 40. Nghĩa vụ của người lao động khi đơn phương chấm dứt hợp đồng lao động trái pháp luật 1. Không được trợ cấp thôi việc. 2. Phải bồi thường cho người sử dụng lao động nửa tháng tiền lương theo hợp đông lao động và một khoản tiền tương ứng với tiền lương theo hợp đồng lao động trong những ngày không báo trước 3. Phải hoàn trả cho người sử dụng lao động chỉ phí đào tạo quy định tại Điều 62 của Bộ luật này.

*Nháp AI:* grade=0 · citation=false;true;true · abstention= · SỬA sau đối chiếu lượt 2: câu trả lời TỰ MÂU THUẪN. Câu đầu nói 'không phải báo trước', câu cuối nói 'vẫn phải tuân thủ thời hạn báo trước theo Điều 35'. Context thiếu khoản 2 Điều 35 (final_context_has_evidence=false). Citation Điều 35 part 1 bị gắn vào kết luận sai ở câu cuối nên false. Điều 39 và Điều 40 (ngoặc gộp, bị bỏ sót ở lần đọc citation đầu) đúng với mô tả 'đơn phương chấm dứt trái pháp luật / nghĩa vụ của NLĐ'.

## agent_hybrid_rrf · q09 · status `answered`

**Câu hỏi:** Trợ cấp thôi việc được tính bao nhiêu cho mỗi năm làm việc?

**Kỳ vọng:** Mỗi năm làm việc được trợ cấp một nửa tháng tiền lương (áp dụng cho người làm việc thường xuyên từ đủ 12 tháng trở lên).

**Agent trả lời:** Theo Bộ luật Lao động 2012 và 2019, trợ cấp thôi việc được tính như sau:

- **Bộ luật Lao động 2012**: Mỗi năm làm việc, người lao động được trợ cấp một nửa tháng tiền lương [a099008554b28f45].
- **Bộ luật Lao động 2019**: Tương tự, mỗi năm làm việc, người lao động được trợ cấp một nửa tháng tiền lương, trừ một số trường hợp đặc biệt [e3c977d516130853].

Tiền lương để tính trợ cấp là tiền lương bình quân của 06 tháng liên tiếp trước khi thôi việc [a099008554b28f45, e3c977d516130853].

**Lượt tìm:** `trợ cấp thôi việc tính theo năm làm việc` (filter None, none)

> **[a099008554b28f45]** blld-2012 · Điều 48 · trang [15, 16]
>
> Điều 48. Trợ cấp thôi việc 1. Khi hợp đồng lao động chấm dứt theo quy định tại các khoản 1,2,3, 5,6, 7, 9 và 10 Điều 36 của Bộ luật này thì người sử dụng lao động có trách nhiệm chi trả trợ cấp thôi việc cho người lao động đã làm việc thường xuyên từ đủ 12 tháng trở lên, mỗi năm làm việc được trợ cấp một nửa tháng tiền lương. 2. Thời gian làm việc đề tính trợ cấp thôi việc là tổng thời gian người lao động đã làm việc thực tế cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiểm thất nghiệp theo quy định của Luật bảo hiểm xã hội và thời gian làm việc đã được người sử dụng lao động chỉ trả trợ cấp thôi việc. ló 3. Tiền lương đề tính trợ cấp thôi việc là tiền lương bình quân theo hợp đồng lao động của 06 tháng liên kê trước khi người lao động thôi việc.

> **[e3c977d516130853]** blld-2019 · Điều 46 · trang [19]
>
> Điều 46. Trợ cấp thôi việc 1. Khi hợp đồng lao động chấm dứt theo quy định tại các khoản 1, 2,3, 4,6,7,9và 10 Điều 34 của Bộ luật này thì người sử dụng lao động có trách nhiệm trả trợ cấp thôi việc cho người lao động đã làm việc thường xuyên cho mình từ đủ 12 tháng trở lên, mỗi năm làm việc được trợ cấp một nửa tháng tiền lương, trừ trường hợp đủ điều kiện hưởng lương hưu theo quy định của pháp luật về bảo hiểm xã hội và trường hợp quy định tại điểm e khoản 1 Điều 36 của Bộ luật này. 2. Thời gian làm việc để tính trợ cấp thôi việc là tổng thời gian người lao động đã làm việc thực tế cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiểm thất nghiệp theo quy định của pháp luật về bảo hiểm thất nghiệp và thời gian làm việc đã được người sử dụng lao động chỉ trả trợ cấp thôi việc, trợ cấp mất việc làm. 3 Tiền lương để tính trợ cấp thôi việc là tiền lương bình quân c

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q10 · status `answered`

**Câu hỏi:** Người lao động bị mất việc làm được nhận trợ cấp tối thiểu bằng bao nhiêu tháng lương?

**Kỳ vọng:** Mỗi năm làm việc trả 01 tháng tiền lương nhưng ít nhất bằng 02 tháng tiền lương.

**Agent trả lời:** Người lao động bị mất việc làm được nhận trợ cấp mất việc làm tối thiểu bằng 02 tháng tiền lương [e174576b407acec5].

**Lượt tìm:** `trợ cấp thôi việc tối thiểu tháng lương` (filter None, none)

> **[e174576b407acec5]** blld-2012 · Điều 49 · trang [16]
>
> Điều 49. Trợ cấp mất việc làm ]. Người sử dụng lao động trả trợ cấp mất việc làm cho người lao động đã làm việc thường xuyên cho mình từ 12 tháng trở lên mà bị mất việc làm theo quy định tại Điều 44 và Điều 45 của Bộ luật này, mỗi năm làm việc trả 0] tháng tiền lương nhung ít nhất phải bằng 02 tháng tiền lương. 2. Thời gian làm việc để tính trợ cấp mắt việc làm là tông thời gian người lao động đã làm việc thực tê cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiêm thật nghiệp theo quy định của Luật bảo hiêm xã hội và thời gian làm việc đã được người sử dụng lao động ch trả trợ cấp thôi việc. mm Tiền lương để tính trợ cấp mất việc làm là tiền lương bình quân theo hợp đông lao động của 06 tháng liên kê trước khi người lao động mât việc làm.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q11 · status `answered`

**Câu hỏi:** Khi chấm dứt hợp đồng lao động, thời hạn thanh toán các khoản tiền giữa hai bên có thể được kéo dài tối đa bao nhiêu ngày?

**Kỳ vọng:** Không quá 30 ngày (bản 2019: chỉ trong các trường hợp liệt kê tại khoản 1 Điều 48; bản 2012: trường hợp đặc biệt).

**Agent trả lời:** Theo Bộ luật Lao động 2012, thời hạn thanh toán các khoản tiền giữa hai bên khi chấm dứt hợp đồng lao động là 07 ngày làm việc, có thể kéo dài nhưng không quá 30 ngày [0cbc2d076afca5c4].

Theo Bộ luật Lao động 2019, thời hạn thanh toán là 14 ngày làm việc, trừ các trường hợp đặc biệt có thể kéo dài nhưng không quá 30 ngày [2a48cb65dea01121].

**Lượt tìm:** `thanh toán tiền lương và các khoản tiền khác khi chấm dứt hợp đồng lao động thời hạn` (filter None, none)

> **[0cbc2d076afca5c4]** blld-2012 · Điều 47 · trang [15]
>
> Điều 47. Trách nhiệm của người sử dụng lao động khi chấm dứt hợp đồng lao động ]. Ít nhất 15 ngày trước ngày hợp đồng lao động xác định thời hạn hết hạn, người sử dụng lao động phải thông báo bằng văn bản cho người lao động biết thời điểm chấm dứt hợp đồng lao động. 2. Trong thời hạn 07 ngày làm việc, kể từ ngày chấm dứt hợp đồng lao động, hai bên có trách nhiệm thanh toán đây đủ các khoản có liên quan đến quyền lợi của mỗi bên; trường hợp đặc biệt, có thể kéo dài nhưng không được quá 30 ngày. 3. Người sử dụng lao động có trách nhiệm hoàn thành thủ tục xác nhận và trả lại sô bảo hiêm xã hội và những giây tờ khác mà người sử dụng lao động đã giữ lại của người lao động. 4. Trong trường hợp doanh nghiệp, hợp tác xã bị chấm dứt hoạt động, bị giải thể, phá sản thì tiền lương, trợ cấp thôi việc, bảo hiểm xã hội, bảo hiểm y tế, bảo hiểm thất nghiệp và các quyền lợi khác của người lao động theo 

> **[2a48cb65dea01121]** blld-2019 · Điều 48 · trang [19, 20]
>
> Điều 48. Trách nhiệm khi chấm dứt hợp đồng lao động 1. Trong thời hạn 14 ngày làm việc. kể từ ngày chấm đứt hợp đồng lao động, hai bên có trách nhiệm thanh toán đầy đủ các khoản tiền có liên quan đến quyền lợi của mỗi bên, trừ trường hợp sau đây có thể kéo đài nhưng không được quá 30 ngày: a) Người sử dụng lao động không phải là cá nhân chấm dứt hoạt động; b) Người sử dụng lao động thay đổi cơ cầu, công nghệ hoặc vì lý do kinh tế; c) Chia, tách, hợp nhất, sáp nhập; bán, cho thuê, chuyển đổi loại hình doanh nghiệp; chuyên nhượng quyền sở hữu, quyên sử dụng tài sản của doanh nghiệp, hợp tác xã; d) Do thiên tai, hỏa hoạn, địch họa hoặc dịch bệnh nguy hiểm. 2. Tiền lương, bảo hiểm xã hội, bảo hiểm y tế, bảo hiểm thất nghiệp, trợ cấp thôi việc và các quyên lợi khác của người lao động theo thỏa ước lao động tập thê, hợp đông lao động được ưu tiên thanh toán trong trường hợp doanh nghiệp, hợp t

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q12 · status `answered`

**Câu hỏi:** Giờ làm việc ban đêm được tính từ mấy giờ đến mấy giờ?

**Kỳ vọng:** Từ 22 giờ đến 06 giờ sáng ngày hôm sau.

**Agent trả lời:** Giờ làm việc ban đêm được tính từ 22 giờ đến 06 giờ sáng ngày hôm sau theo quy định tại Điều 106 Bộ luật Lao động 2019 [f8097e0a7bdcadcf].

Cũng theo Điều 105 Bộ luật Lao động 2012, giờ làm việc ban đêm được tính từ 22 giờ đến 6 giờ sáng ngày hôm sau [43ef3ba1a0f56f9c].

**Lượt tìm:** `giờ làm việc ban đêm` (filter None, none)

> **[f8097e0a7bdcadcf]** blld-2019 · Điều 106 · trang [40]
>
> Điều 106. Giờ làm việc ban đêm Giờ làm việc ban đêm được tính từ 22 giờ đến 06 giờ sáng ngày hôm sau.

> **[43ef3ba1a0f56f9c]** blld-2012 · Điều 105 · trang [30]
>
> Điều 105. Giờ làm việc ban đêm Giờ làm việc ban đêm được tính từ 22 giờ đến 6 giờ sáng ngày hôm sau.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q13 · status `answered`

**Câu hỏi:** Người làm ca đêm được nghỉ giữa ca ít nhất bao nhiêu phút?

**Kỳ vọng:** Ít nhất 45 phút (bản 2019 ghi rõ là 45 phút liên tục).

**Agent trả lời:** Người làm ca đêm được nghỉ giữa ca ít nhất 45 phút liên tục theo quy định tại Điều 109 của Bộ luật Lao động 2019 [5a45954688b086dc].

**Lượt tìm:** `nghỉ giữa ca người làm ca đêm` (filter None, none)

> **[5a45954688b086dc]** blld-2019 · Điều 109 · trang [41]
>
> Điều 109. Nghĩ trong giờ làm việc 1. Người lao động làm việc theo thời giờ làm việc quy định tại Điều 105 của Bộ luật này từ 06 giờ trở lên trong một ngày thì được nghỉ giữa giờ ít nhất 30 phút liên tục, làm việc ban đêm thì được nghỉ giữa giờ ít nhất 45 phút liên tục. Trường hợp người lao động làm việc theo ca liên tục từ 06 giờ trở lên thì thời gian nghỉ giữa giờ được tính vào giờ làm việc. 2. Ngoài thời gian nghỉ quy định tại khoản 1 Điều này, người sử dụng lao động bố trí cho người lao động các đợt nghỉ giải lao và ghi vào nội quy lao động.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q14 · status `answered`

**Câu hỏi:** Người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bao nhiêu?

**Kỳ vọng:** Ít nhất bằng 300%, chưa kể tiền lương ngày lễ đối với người lao động hưởng lương ngày.

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bằng 300% chưa kể tiền lương ngày lễ, tết, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày [8bf032c21470d951].

Theo Bộ luật Lao động 2012, người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bằng 300% chưa kể tiền lương ngày lễ, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày [43cd550df5a10ee9].

**Lượt tìm:** `làm thêm giờ ngày nghỉ lễ trả lương` (filter None, none)

> **[8bf032c21470d951]** blld-2019 · Điều 98 · trang [37]
>
> Điều 98. Tiền lương làm thêm giờ, làm việc vào ban đêm 1. Người lao động làm thêm giờ được trả lương tính theo đơn giá tiền lương hoặc tiền lương thực trả theo công việc đang làm như sau: a) Vào ngày thường, ít nhất bằng 150%; b) Vào ngày nghỉ hằng tuần, ít nhất bằng 200%; c) Vào ngày nghỉ lễ, tết, "ngày nghỉ có hưởng lương, ít nhất bằng 300% chưa kể tiền lương ngày lễ, tết, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày. 2. _Người lao động làm việc vào ban đêm thì được trả thêm ít nhất bằng 30% tiền lương tính theo đơn giá tiền lương hoặc tiền lương thực trả theo công việc của ngày làm việc bình thường. 3. Người lao động làm thêm giờ vào ban đêm thì ngoài việc trả lương theo quy định tại khoản 1 và khoản 2 Điều này, người lao động còn được trả thêm 20% tiền lương tính theo đơn giá tiền lương hoặc tiền lương theo công việc làm vào ban ngày của ngày làm việc bình thường 

> **[43cd550df5a10ee9]** blld-2012 · Điều 97 · trang [28, 29]
>
> Điều 97. Tiền lương làm thêm giờ, làm việc vào ban đêm 1. Người lao động làm thêm giờ được trả lương tính theo đơn giá tiền lương hoặc tiên lương theo công việc đang làm như sau: a) Vào ngày thường, ít nhất bằng 150%; b) Vào ngày nghỉ hằng tuần, ít nhất bằng 200%; c) Vào ngày nghỉ lễ, ngày nghỉ có hưởng lương, ít nhất băng 300% chua kể tiền lương ngày lễ, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày. 2. Người lao động làm việc vào ban đêm, thì được trả thêm ít nhất băng 30% tiền lương tính theo đon giá tiền lương hoặc tiền lương theo công việc của ngày làm việc bình thường. 3. Người lao động làm thêm giờ vào ban đêm thì ngoài việc trả lương theo quy định tại khoản 1 và khoản 2 Điều này, người lao động còn được trả thêm 20% tiền lương tính theo đơn giá tiền lương hoặc tiền lương theo công việc làm vào ban ngày.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q15 · status `answered`

**Câu hỏi:** Người làm công việc nặng nhọc, độc hại, nguy hiểm được nghỉ hằng năm bao nhiêu ngày?

**Kỳ vọng:** 14 ngày làm việc (16 ngày nếu là công việc đặc biệt nặng nhọc, độc hại, nguy hiểm).

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động làm công việc nặng nhọc, độc hại, nguy hiểm được nghỉ hằng năm 14 ngày làm việc [3fe27b9fd53b4099].

Theo Bộ luật Lao động 2012, người lao động làm công việc nặng nhọc, độc hại, nguy hiểm cũng được nghỉ hằng năm 14 ngày làm việc [b268f97122b4fcbd].

**Lượt tìm:** `nghỉ hằng năm người lao động làm công việc nặng nhọc độc hại nguy hiểm` (filter None, none)

> **[3fe27b9fd53b4099]** blld-2019 · Điều 113 · trang [42]
>
> Điều 113. Nghĩ hằng năm l 1. Người lao động làm việc đủ 12 tháng cho một người sử dụng lao động thì được nghỉ hăng năm, hưởng nguyên lương theo hợp đông lao động như sau: a) 12 ngày làm việc đối với người làm công việc trong điều kiện bình thường: b) 14 ngày làm việc đối với người lao động chưa thành niên, lao động là người khuyêt tật, người làm nghề, công việc nặng nhọc, độc hại, nguy hiểm; c) 16 ngày làm việc đối với người làm nghề, công việc đặc biệt nặng nhọc, độc hại, nguy hiêm. 2. Người lao động làm việc chưa đủ 12 tháng cho một người sử dụng lao động thì sô ngày nghỉ hăng năm theo tỷ lệ tương ứng với sô tháng làm việc. 3. Trường hợp do thôi việc, bị mất việc làm mà chưa nghỉ hằng năm hoặc chưa nghỉ hết số ngày nghỉ hăng năm thì được người sử dụng lao động thanh toán tiên lương cho những ngày chưa nghỉ... 4. Người sử dụng lao động có trách nhiệm quy định lịch nghỉ hằng năm sau khi 

> **[b268f97122b4fcbd]** blld-2012 · Điều 111 · trang [32]
>
> Điều 111. Nghỉ hằng năm 1. Người lao động có đủ 12 tháng làm việc cho một người sử dụng lao động thì được nghỉ hăng năm, hưởng nguyên lương theo hợp đông lao động như sau: a) 12 ngày làm việc đối với người làm công việc trong điều kiện bình thường: b) 14 ngày làm việc đối với người làm công việc nặng nhọc, độc hại, nguy hiểm hoặc người làm việc ở những nơi có có điều kiện sinh sống khắc nghiệt theo danh mục do Bộ Lao động - Thương binh và Xã hội chủ trì phối hợp với Bộ Y tế ban hành hoặc lao động chưa thành niên hoặc lao động là người khuyêt tật; c) 16 ngày làm việc đối với người làm công việc đặc biệt nặng nhọc, độc hại, nguy hiểm hoặc người làm việc ở những nơi có điều kiện sinh sống đặc biệt khắc nghiệt theo danh mục do Bộ Lao động - Thương bình và Xã hội chủ trì ì phối hợp với Bộ Y tế ban hành. 2. Người sử dụng lao động có quyền quy định lịch nghi hằng năm sau khi tham khảo ý kiên củ

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q16 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2012, người lao động được hưởng lương hưu khi đủ bao nhiêu tuổi?

**Kỳ vọng:** Nam đủ 60 tuổi, nữ đủ 55 tuổi (khi bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội).

**Agent trả lời:** Theo Bộ luật Lao động 2012, người lao động được hưởng lương hưu khi nam đủ 60 tuổi, nữ đủ 55 tuổi [67976ce3fa4d3293].

**Lượt tìm:** `tuổi hưởng lương hưu người lao động` (filter {'year': 2012}, user)

> **[67976ce3fa4d3293]** blld-2012 · Điều 187 · trang [52]
>
> Điều 187. Tuổi nghỉ hưu 1. Người lao động bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội theo quy định của pháp luật về bảo hiểm xã hội được hưởng lương hưu khi nam đủ 60 tuổi, nữ đủ 55 tuổi. 2. Người lao động bị suy giảm khả năng lao động; làm công việc đặc biệt nặng nhọc, độc hại, nguy hiểm; làm công việc nặng nhọc, độc hại, nguy hiểm; làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo thuộc danh mục do Chính phủ quy định có thể nghỉ hưu ở tuổi thấp hơn so với quy định tại khoản 1 Điều này. 3. Người lao động có trình độ chuyên môn kỹ thuật cao, người lao động làm công tác quản lý và một số trường hợp đặc biệt khác có thể nghỉ hưu ở tuổi cao hơn nhưng không quá 05 năm so với quy định tại khoản 1 Điều này. 4. Chính phủ quy định chi tiết khoản 2 và khoản 3 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q17 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, từ năm 2021 tuổi nghỉ hưu của lao động nữ trong điều kiện lao động bình thường là bao nhiêu?

**Kỳ vọng:** Đủ 55 tuổi 04 tháng; sau đó mỗi năm tăng thêm 04 tháng cho đến khi đủ 60 tuổi vào năm 2035.

**Agent trả lời:** Theo Bộ luật Lao động 2019, từ năm 2021, tuổi nghỉ hưu của lao động nữ trong điều kiện lao động bình thường là đủ 55 tuổi 04 tháng [c40fad20889e6976].

**Lượt tìm:** `tuổi nghỉ hưu lao động nữ điều kiện lao động bình thường` (filter {'year': 2019}, user)

> **[c40fad20889e6976]** blld-2019 · Điều 169 · trang [60]
>
> Điều 169. Tuổi nghỉ hưu 1. Người lao động bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội theo quy định của pháp luật về bảo hiểm xã hội được hưởng lương hưu khi đủ tuôi nghỉ hưu. 2. Tuổi nghỉ hưu của người lao động trong điều kiện lao động bình thường được điều chỉnh theo lộ trình cho đên khi đủ 62 tuổi đối với lao động nam vào năm 2028 và đủ 60 tuôi đôi với lao động nữ vào năm 2035. Kể từ năm 2021, tuổi nghỉ hưu của người lao động trong điều kiện lao động bình thường là đủ 60 tuổi 03 tháng đối với lao động nam và đủ 55 tuổi 04 tháng đối với lao động nữ; sau đó, cứ mỗi năm tăng thêm 03 tháng đối với lao động nam và 04 tháng đối với lao động nữ. 3. Người lao động bị suy giảm khả năng lao động; làm nghề, công việc đặc biệt nặng nhọc, độc hại, nguy hiểm; làm nghề, công việc nặng nhọc, độc hại, nguy hiểm; làm việc ở vùng có điều kiện kinh tế - xã hội đặc biệt khó khăn có thể nghỉ hưu ở 

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q18 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, người lao động được nghỉ bao nhiêu ngày vào dịp Quốc khánh?

**Kỳ vọng:** 02 ngày (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau).

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động được nghỉ 02 ngày vào dịp Quốc khánh (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau) [70c23213ef936eb5].

**Lượt tìm:** `nghỉ lễ Quốc khánh` (filter {'year': 2019}, user)

> **[70c23213ef936eb5]** blld-2019 · Điều 112 · trang [41, 42]
>
> Điều 112. Nghỉ lễ, tết 1. Người lao động được nghỉ làm việc, hưởng nguyên lương trong những ngày lỗ, tết sau đây: a) Tết Dương lịch: 01 ngày (ngày 01 tháng 01 đương lịch); b) Tết Âm lịch: 05 ngày; c) Ngày Chiến thắng: 01 ngày (ngày 30 tháng 4 dương lịch); d) Ngày Quốc tế lao động: 01 ngày (ngày 01 tháng 5 dương lịch); đ) Quốc khánh: 02 ngày (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau); e) Ngày Giỗ Tổ Hùng Vương: 01 ngày (ngày 10 tháng 3 âm lịch). 2. Lao động là người nước ngoài làm việc tại Việt Nam ngoài các ngày nghỉ theo quy định tại khoản 1 Điều này còn được nghỉ thêm 01 ngày Tết cổ truyền dân tộc và 01 ngày Quốc khánh của nước họ. 3. Hằng năm, căn cứ vào điều kiện thực tế, Thủ tướng Chính phủ quyết định cụ thể ngày nghỉ quy định tại điêm b và điểm đ khoản 1 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q19 · status `answered`

**Câu hỏi:** Nếu nhân viên vi phạm liên quan trực tiếp đến tài sản của công ty thì thời hiệu xử lý kỷ luật lao động là bao lâu?

**Kỳ vọng:** 12 tháng (thay vì 06 tháng như thông thường).

**Agent trả lời:** Nếu hành vi vi phạm của nhân viên liên quan trực tiếp đến tài sản của công ty, thời hiệu xử lý kỷ luật lao động là 12 tháng.

Căn cứ:
- Bộ luật Lao động 2019, Điều 123, Khoản 1: "...trường hợp hành vi vi phạm liên quan trực tiếp đến tài chính, tài sản... của người sử dụng lao động thì thời hiệu xử lý kỷ luật lao động là 12 tháng." [ddd5e6ef6c45d7a2]
- Bộ luật Lao động 2012, Điều 124, Khoản 1: "...trường hợp hành vi vi phạm liên quan trực tiếp đến tài chính, tài sản... của người sử dụng lao động thì thời hiệu xử lý kỷ luật lao động tối đa là 12 tháng." [4829c9234e35ab72]

**Lượt tìm:** `thời hiệu xử lý kỷ luật lao động vi phạm tài sản` (filter None, none)

> **[ddd5e6ef6c45d7a2]** blld-2019 · Điều 123 · trang [46]
>
> Điều 123. Thời hiệu xử lý kỷ luật lao động 1. Thời hiệu xử lý kỷ luật lao động là 06 tháng kể từ ngày xảy ra hành vi vi phạm; trường hợp hành vi vi phạm liên quan trực tiếp đến tài chính, tài sản, tiệt lộ bí mật công nghệ, bí mật kinh doanh của người sử dụng lao động thì thời hiệu xử lý kỷ luật lao động là 12 tháng. 2. Khi hết thời gian quy định tại khoản 4 Điều 122 của Bộ luật này, nếu hết thời hiệu hoặc còn thời hiệu nhưng không đủ 60 ngày thì được kéo dài thời hiệu đê xử lý kỷ luật lao động nhưng không quá 60 ngày kề từ ngày hết thời gian nêu trên. 3. Người sử dụng lao động phải ban hành quyết định xử lý kỷ luật lao động trong thời hạn quy định tại khoản 1 và khoản 2 Điều này.

> **[4829c9234e35ab72]** blld-2012 · Điều 124 · trang [35, 36]
>
> Điều 124. Thời hiệu xử lý kỷ luật lao động 1. Thời hiệu xử lý kỷ luật lao động tối đa là 06 tháng, kể từ ngày xảy ra hành vi vi phạm; trường hợp hành vi vi phạm liên quan trực tiếp đến tài chính, tài sản, tiết lộ bí mật công nghệ, bí mật kinh doanh của người sử dụng lao động thì thời hiệu xử lý kỷ luật lao động tối đa là 12 tháng. 2. Khi hết thời gian quy định tại các điểm a, b và c khoản 4 Điều 123, nếu còn thời hiệu đề xử lý kỷ luật lao động thì người sử dụng lao động tiền hành xử lý kỹ luật lao động ngay, nếu hết thời hiệu thì được kéo dài thời hiệu để xử lý kỷ luật lao động nhưng tôi đa không quá 60 ngày kế từ ngày hết thời gian nêu trên. so Khi hết thời gian quy định tại điểm d khoản 4 Điều 123, mà thời hiệu xử lý kỷ luật lao động đã hết thì được kéo dài thời hiệu xử lý kỷ luật lao động nhưng tôi đa không quá 60 ngày kê từ ngày hết thời gian nêu trên. 3. Quyết định xử lý kỷ luật lao

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · q20 · status `answered`

**Câu hỏi:** Lao động nữ mang thai làm việc ở vùng cao hoặc hải đảo không được bố trí làm việc ban đêm kể từ tháng thai thứ mấy?

**Kỳ vọng:** Từ tháng thứ 06 (thay vì tháng thứ 07 như nơi khác).

**Agent trả lời:** Lao động nữ mang thai làm việc ở vùng cao hoặc hải đảo không được bố trí làm việc ban đêm kể từ tháng thai thứ 06.

Căn cứ:
- Bộ luật Lao động 2012, Điều 155, khoản 1, điểm a [ffe02f16c93fddb4].
- Bộ luật Lao động 2019, Điều 137, khoản 1, điểm a [53201ad6737fab80].

**Lượt tìm:** `lao động nữ mang thai vùng cao hải đảo không được bố trí làm việc ban đêm` (filter None, none)

> **[ffe02f16c93fddb4]** blld-2012 · Điều 155 · trang [44]
>
> Điều 155. Bảo vệ thai sản đối với lao động nữ 1. Người sử dụng lao động không được sử dụng lao động nữ làm việc ban đêm, làm thêm giờ và đi công tác xa trong các trường hợp sau đây: a) Mang thai từ tháng thứ 07 hoặc từ tháng thứ 06 nếu làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo; b) Đang nuôi con dưới 12 tháng tuổi. 2. Lao động nữ làm công việc nặng nhọc khi mang thai từ tháng thứ 07, được chuyển làm công việc nhẹ hơn hoặc được giảm bớt 01 giờ làm việc hằng ngày mà vân hưởng đủ lương. 3. Người sử dụng lao động không được sa thải hoặc đơn phương chấm dứt hợp đồng lao động đối với lao động nữ vì lý do kết hôn, mang thai, nghỉ thai sản, nuôi con dưới 12 tháng tuổi, trừ trường hợp người sử dụng lao động là cá nhân chết, bị Tòa án tuyên bố mất năng lực hành vi dân sự, mât tích hoặc là đã chết hoặc người sử dụng lao động không phải là cá nhân chấm dứt hoạt động. 4. Trong thời gi

> **[53201ad6737fab80]** blld-2019 · Điều 137 · trang [50]
>
> Điều 137. Bảo vệ thai sản 1. Người sử dụng lao động không được sử dụng người lao động làm việc ban đêm, làm thêm giờ và đi công tác xa trong trường hợp sau đây: a) Mang thai từ tháng thứ 07 hoặc từ tháng thứ 06 nếu làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo; b) Đang nuôi con đưới 12 tháng tuổi, trừ trường hợp được người lao động đồng ý. 2. Lao động nữ làm nghề, công việc nặng nhọc, độc hại, nguy hiểm hoặc đặc biệt nặng nhọc, độc hại, nguy hiêm hoặc làm nghề, công việc có ảnh hưởng xâu tới chức năng sinh sản và nuôi con khi mang thai và có thông báo cho người sử dụng lao động biết thì được người sử dụng lao động chuyển sang làm công việc nhẹ hơn, an toàn hơn hoặc giảm bớt 01 giờ làm việc hằng ngày mà không bị cắt giảm tiền lương và quyền, lợi ích cho đến hết thời gian nuôi con dưới 12 tháng tuổi,

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_hybrid_rrf · u01 · status `abstain`

**Câu hỏi:** Mức lương tối thiểu vùng I hiện nay là bao nhiêu đồng một tháng?

**Kỳ vọng:** (thiếu bằng chứng) Cả hai bộ luật chỉ nói mức lương tối thiểu (vùng) do Chính phủ quy định/công bố; không có con số tiền nào.

**Agent trả lời:** Bộ luật Lao động 2019 quy định về mức lương tối thiểu nhưng không nêu cụ thể con số. Mức lương tối thiểu vùng I hiện nay được quy định trong các văn bản pháp luật khác (như Quyết định của Chính phủ) dựa trên cơ sở khuyến nghị của Hội đồng tiền lương quốc gia, không phải trong Bộ luật Lao động.

Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời.

**Lượt tìm:** `mức lương tối thiểu vùng` (filter {'year': 2019}, inferred)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối đúng. Câu mở đầu nhắc Hội đồng tiền lương quốc gia/Chính phủ quy định, khớp Điều 91–92, không đưa con số. CẦN NGƯỜI DUYỆT xem phần giải thích có bị coi là khẳng định thêm không.

## agent_hybrid_rrf · u02 · status `abstain`

**Câu hỏi:** Người sử dụng lao động phải đóng bảo hiểm xã hội bắt buộc bằng bao nhiêu phần trăm quỹ tiền lương?

**Kỳ vọng:** (thiếu bằng chứng) Bộ luật chỉ quy định nghĩa vụ tham gia/đóng bảo hiểm xã hội theo pháp luật về bảo hiểm xã hội; không có tỷ lệ đóng.

**Agent trả lời:** Các đoạn tìm được trong Bộ luật Lao động 2012 và 2019 không nêu cụ thể tỷ lệ phần trăm người sử dụng lao động phải đóng bảo hiểm xã hội bắt buộc. Thông tin này thường được quy định trong Luật Bảo hiểm xã hội và các văn bản hướng dẫn thi hành.

Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời.

**Lượt tìm:** `tỷ lệ đóng bảo hiểm xã hội bắt buộc người sử dụng lao động` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối đúng, không đưa tỷ lệ nào. Có thêm câu 'thường quy định trong Luật BHXH/văn bản hướng dẫn', ý này khớp với dẫn chiếu 'theo pháp luật về BHXH' trong bộ luật. CẦN NGƯỜI DUYỆT (quy tắc: không thêm khẳng định vô căn cứ).

## agent_hybrid_rrf · u03 · status `abstain`

**Câu hỏi:** Người lao động làm việc từ xa tại nhà được hưởng phụ cấp bao nhiêu mỗi tháng?

**Kỳ vọng:** (thiếu bằng chứng) Không bộ luật nào quy định làm việc từ xa hay phụ cấp cho hình thức này.

**Agent trả lời:** Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời.

**Lượt tìm:** `phụ cấp làm việc từ xa tại nhà` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối đúng, không đưa con số phụ cấp. Câu giải thích (nếu có) chỉ nói bộ luật không quy định.

## agent_dense_inferred · q01 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, hai bên được giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn bao lâu?

**Kỳ vọng:** Hợp đồng có thời hạn dưới 01 tháng (trừ các trường hợp tại khoản 2 Điều 18, điểm a khoản 1 Điều 145 và khoản 1 Điều 162).

**Agent trả lời:** Theo Bộ luật Lao động 2019, hai bên được giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn dưới 01 tháng [410ba0a07076ab8d].

**Lượt tìm:** `hợp đồng lao động bằng lời nói thời hạn` (filter {'year': 2019}, inferred)

> **[410ba0a07076ab8d]** blld-2019 · Điều 14 · trang [6, 7]
>
> Điều 14. Hình thức hợp đồng lao động 1. Hợp đồng lao động phải được giao kết bằng văn bản và được làm thành 02 bản, người lao động giữ 01 bản, người sử dụng lao động giữ 01 bản, trừ trường hợp quy định tại khoản 2 Điều này. Hợp đồng lao động được giao kết thông qua phương tiện điện tử dưới hình thức thông điệp dữ liệu theo quy định của pháp luật về giao dịch điện tử có giá trị như bợp đồng lao động bằng văn bản. 2. Hai bên có thể giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn dưới 01 tháng, trừ trường hợp quy định tại khoản 2 Điều 18, điểm a khoản 1 Điều 145 và khoản 1 Điều 162 của Bộ luật này. Ss

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q02 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2012, công việc tạm thời có thời hạn bao lâu thì các bên được giao kết hợp đồng bằng lời nói?

**Kỳ vọng:** Công việc tạm thời có thời hạn dưới 03 tháng.

**Agent trả lời:** Theo Bộ luật Lao động 2012, các bên được giao kết hợp đồng lao động bằng lời nói đối với công việc tạm thời có thời hạn dưới 03 tháng [8b35e2d37ae827ce].

**Lượt tìm:** `hợp đồng bằng lời nói công việc tạm thời thời hạn` (filter {'year': 2012}, inferred)

> **[8b35e2d37ae827ce]** blld-2012 · Điều 16 · trang [6]
>
> Điều 16. Hình thức hợp đồng lao động 1. Hợp đồng lao động phải được giao kết bằng văn bản và được làm thành 02 bản, người lao động giữ 01 bản, người sử dụng lao động giữ 01 bản, trừ trường hợp quy định tại khoản 2 Điều này. 2. Đối với công việc tạm thời có thời hạn dưới 03 tháng, các bên có thể giao kết hợp đồng lao động bằng lời nói.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q03 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, số giờ làm thêm của người lao động tối đa trong một tháng là bao nhiêu?

**Kỳ vọng:** Không quá 40 giờ trong 01 tháng (và không quá 200 giờ/năm, trừ các trường hợp được làm đến 300 giờ/năm).

**Agent trả lời:** Theo Bộ luật Lao động 2019, số giờ làm thêm của người lao động tối đa trong một tháng là **40 giờ**.

Căn cứ:
- Điều 107, khoản 2, điểm b) quy định: "không quá 40 giờ trong 01 tháng" [71267d6e72a8bf88].

**Lượt tìm:** `số giờ làm thêm tối đa trong một tháng` (filter {'year': 2019}, inferred)

> **[71267d6e72a8bf88]** blld-2019 · Điều 107 · trang [40]
>
> Điều 107. Làm thêm giờ 1. Thời gian làm thêm giờ là khoảng thời gian làm việc ngoài thời giờ làm việc bình thường theo quy định của pháp luật, thỏa ước lao động tập thê hoặc nội quy lao động. 2. Người sử dụng lao động được sử dụng người lao động làm thêm giờ khi đáp ứng đây đủ các yêu câu sau đây: a) Phải được sự đồng ý của người lao động: b) Bảo đảm số giờ làm thêm của người lao động không quá 50% số giờ làm việc bình thường trong 01 ngày; trường hợp áp dụng quy định thời giờ làm việc bình thường theo tuân thì tổng số giờ làm việc bình thường và số giờ làm thêm không quá 12 giờ trong 01 ngày; không quá 40 giờ trong 01 tháng: c) Bảo đảm số giờ làm thêm của người lao động không quá 200 giờ trong 01 năm, trừ trường hợp quy định tại khoản 3 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q04 · status `answered`

**Câu hỏi:** Bộ luật Lao động 2012 giới hạn số giờ làm thêm trong một tháng là bao nhiêu?

**Kỳ vọng:** Không quá 30 giờ trong 01 tháng.

**Agent trả lời:** Theo Bộ luật Lao động 2012, số giờ làm thêm của người lao động không quá 30 giờ trong một tháng [3b164eb9c075d12a].

**Lượt tìm:** `giới hạn số giờ làm thêm trong một tháng` (filter {'year': 2012}, inferred)

> **[3b164eb9c075d12a]** blld-2012 · Điều 106 · trang [30, 31]
>
> Điều 106. Làm thêm giờ 1. Làm thêm giờ là khoảng thời gian làm việc ngoài thời giờ làm việc bình thường được quy định trong pháp luật, thỏa ước lao động tập thể hoặc theo nội quy. lao động. 2. Người sử dụng lao động được sử dụng người lao động làm thêm giờ khi đáp ứng đủ các điều kiện sau đây: a) Được sự đồng ý của người lao động: b) Bảo đảm số giờ làm thêm của người lao động không quá 50% số giờ làm việc bình thuờng trong 01 ngày, trường hợp áp dụng quy định làm việc theo tuần thì tông số giờ làm việc bình thường và số giờ làm thêm không quá 12 giờ trong 01 ngày, không quá 30 giờ trong 0] tháng và tông sô không quá 200 giờ trong 01 năm, trừ một sô trường hợp đặc biệt do Chính phủ quy định thì được làm thêm giờ không quá 300 giờ trong 01 năm; c) Sau mỗi đợt làm thêm giờ nhiều ngày liên tục trong tháng, người sử dụng lao động phải bô trí đề người lao động được nghỉ bù cho sô thời gian đã 

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q05 · status `answered`

**Câu hỏi:** Người được tuyển vào vị trí quản lý doanh nghiệp có thể phải thử việc tối đa bao nhiêu ngày?

**Kỳ vọng:** Không quá 180 ngày (quy định của Bộ luật Lao động 2019; bản 2012 không có mức riêng cho người quản lý doanh nghiệp).

**Agent trả lời:** Người lao động nói chung có thể thử việc tối đa 18 tháng theo Bộ luật Lao động 2019 [18875379609a900a]. Tuy nhiên, đối với người lao động làm việc theo hợp đồng lao động có thời hạn dưới 01 tháng thì không áp dụng thử việc [18875379609a900a].

**Lượt tìm:** `thử việc người lao động quản lý` (filter None, none)

> **[18875379609a900a]** blld-2019 · Điều 24 · trang [10]
>
> Điều 24. Thử việc 1. Người sử dụng lao động và người lao động có thể thỏa thuận nội dung thử việc ghi trong hợp đông lao động hoặc thỏa thuận về thử việc băng việc giao kêt hợp đông thử việc. 2. Nội dung chủ yếu của hợp đồng thử việc gồm thời gian thử việc và nội dung quy định tại các điểm a, b, c, đ, g vàh khoản 1 Điều 21 của Bộ luật này. 3. Không áp dụng thử việc đối với người lao động giao kết hợp đồng lao động có thời hạn dưới 01 tháng.

*Nháp AI:* grade=0 · citation=false · abstention= · Giống agent_dense_k3: '18 tháng' không có căn cứ; Điều 25 không vào context.

## agent_dense_inferred · q06 · status `answered`

**Câu hỏi:** Tiền lương trong thời gian thử việc ít nhất phải bằng bao nhiêu phần trăm mức lương của công việc đó?

**Kỳ vọng:** Ít nhất bằng 85% mức lương của công việc đó (giống nhau ở bản 2012 và 2019).

**Agent trả lời:** Theo Bộ luật Lao động 2012, tiền lương trong thời gian thử việc ít nhất phải bằng 85% mức lương của công việc đó [fbeaa39254552433].

Theo Bộ luật Lao động 2019, tiền lương trong thời gian thử việc cũng ít nhất phải bằng 85% mức lương của công việc đó [0eeeb5f152e2ed3b].

**Lượt tìm:** `tiền lương thời gian thử việc tỷ lệ phần trăm mức lương công việc` (filter None, none)

> **[fbeaa39254552433]** blld-2012 · Điều 28 · trang [9]
>
> Điều 28. Tiền lương trong thời gian thử việc Tiền lương của người lao động trong thời gian thử việc do hai bên thoả thuận nhưng ít nhất phải bằng 85% mức lương của công việc đó.

> **[0eeeb5f152e2ed3b]** blld-2019 · Điều 26 · trang [10]
>
> Điều 26. Tiền lương thứ việc Tiền lương của người lao động trong thời gian thử việc do hai bên thỏa thuận nhưng ít nhất phải băng 85% mức lương của công việc đó.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q07 · status `answered`

**Câu hỏi:** Nhân viên ký hợp đồng không thời hạn muốn tự nghỉ việc thì phải báo trước cho công ty ít nhất bao lâu?

**Kỳ vọng:** Ít nhất 45 ngày (bản 2012 có ngoại lệ cho lao động nữ mang thai theo Điều 156).

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động làm việc theo hợp đồng lao động không xác định thời hạn muốn đơn phương chấm dứt hợp đồng lao động phải báo trước cho người sử dụng lao động ít nhất 45 ngày [88d5dd520c3fcef6].

Theo Bộ luật Lao động 2012, người lao động làm việc theo hợp đồng lao động không xác định thời hạn muốn đơn phương chấm dứt hợp đồng lao động phải báo trước cho người sử dụng lao động ít nhất 45 ngày [fceb706dab47570b].

**Lượt tìm:** `tự thôi việc hợp đồng không thời hạn báo trước` (filter None, none)

> **[88d5dd520c3fcef6]** blld-2019 · Điều 35 · trang [14]
>
> Điều 35. Quyền đơn phương chấm dứt hợp đồng lao động của người lao động 1. Người lao động có quyền đơn phương chấm dứt hợp đồng lao động nhưng phải báo trước cho người sử dụng lao động như sau: a) Ít nhất 45 ngày nếu làm việc theo hợp đồng lao động không xác định thời hạn; b) Ít nhất 30 ngày nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn từ 12 tháng đên 36 tháng: c) Ít nhất 03 ngày làm việc nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn dưới 12 tháng: d) Đối với một số ngành, nghề, công việc đặc thù thì thời hạn báo trước được thực hiện theo quy định của Chính phủ.

> **[fceb706dab47570b]** blld-2012 · Điều 40 · trang [13]
>
> Điều 40. Huỷ bỏ việc đơn phương chấm dứt hợp đồng lao động Mỗi bên đều có quyền huỷ bỏ việc đơn phương chấm dứt hợp đồng lao động trước khi hết thời hạn báo trước nhưng phải thông báo bằng văn bản và phải được bên kia đồng ý.

*Nháp AI:* grade=2 · citation=true;false · abstention= · Giống agent_dense_k3: Điều 35/2019 đúng; Điều 40/2012 (hủy bỏ) không hỗ trợ ý '45 ngày theo 2012'.

## agent_dense_inferred · q08 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, nếu người lao động bị trả lương không đúng thời hạn thì có phải báo trước khi đơn phương chấm dứt hợp đồng không?

**Kỳ vọng:** Không cần báo trước, trừ trường hợp quy định tại khoản 4 Điều 97.

**Agent trả lời:** Không, Bộ luật Lao động 2019 không quy định trường hợp người lao động bị trả lương không đúng thời hạn là lý do để đơn phương chấm dứt hợp đồng lao động mà không cần báo trước.

Theo Điều 35 [88d5dd520c3fcef6], người lao động chỉ được đơn phương chấm dứt hợp đồng lao động khi có một trong các lý do được quy định tại các Điều 35, 36 và 37 của Bộ luật này. Việc trả lương không đúng thời hạn không nằm trong các lý do này.

Do đó, nếu người lao động đơn phương chấm dứt hợp đồng lao động vì lý do trả lương không đúng thời hạn, sẽ được coi là đơn phương chấm dứt hợp đồng lao động trái pháp luật theo Điều 39 [2b82e938dbe5e213] và phải chịu các nghĩa vụ theo Điều 40 [ebea0c01b9dd25d1].

**Lượt tìm:** `người lao động bị trả lương không đúng thời hạn đơn phương chấm dứt hợp đồng` (filter {'year': 2019}, inferred)

> **[88d5dd520c3fcef6]** blld-2019 · Điều 35 · trang [14]
>
> Điều 35. Quyền đơn phương chấm dứt hợp đồng lao động của người lao động 1. Người lao động có quyền đơn phương chấm dứt hợp đồng lao động nhưng phải báo trước cho người sử dụng lao động như sau: a) Ít nhất 45 ngày nếu làm việc theo hợp đồng lao động không xác định thời hạn; b) Ít nhất 30 ngày nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn từ 12 tháng đên 36 tháng: c) Ít nhất 03 ngày làm việc nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn dưới 12 tháng: d) Đối với một số ngành, nghề, công việc đặc thù thì thời hạn báo trước được thực hiện theo quy định của Chính phủ.

> **[2b82e938dbe5e213]** blld-2019 · Điều 39 · trang [16]
>
> Điều 39. Đơn phương chấm dứt hợp đồng lao động trái pháp luật Đơn phương chấm dứt hợp đồng lao động trái pháp luật là trường hợp châm dứt hợp đông lao động không đúng quy định tại các điêu 35, 36 và 37 của Bộ luật này.

> **[ebea0c01b9dd25d1]** blld-2019 · Điều 40 · trang [16]
>
> Điều 40. Nghĩa vụ của người lao động khi đơn phương chấm dứt hợp đồng lao động trái pháp luật 1. Không được trợ cấp thôi việc. 2. Phải bồi thường cho người sử dụng lao động nửa tháng tiền lương theo hợp đông lao động và một khoản tiền tương ứng với tiền lương theo hợp đồng lao động trong những ngày không báo trước 3. Phải hoàn trả cho người sử dụng lao động chỉ phí đào tạo quy định tại Điều 62 của Bộ luật này.

*Nháp AI:* grade=0 · citation=false;false;false · abstention= · Giống agent_dense_k3: kết luận sai, thiếu khoản 2 Điều 35 trong context.

## agent_dense_inferred · q09 · status `answered`

**Câu hỏi:** Trợ cấp thôi việc được tính bao nhiêu cho mỗi năm làm việc?

**Kỳ vọng:** Mỗi năm làm việc được trợ cấp một nửa tháng tiền lương (áp dụng cho người làm việc thường xuyên từ đủ 12 tháng trở lên).

**Agent trả lời:** Theo Bộ luật Lao động 2019 và 2012, trợ cấp thôi việc được tính như sau:

- **Bộ luật Lao động 2019** [e3c977d516130853]: Mỗi năm làm việc, người lao động được trợ cấp một nửa tháng tiền lương.
- **Bộ luật Lao động 2012** [a099008554b28f45]: Mỗi năm làm việc, người lao động được trợ cấp một nửa tháng tiền lương.

Tiền lương để tính trợ cấp là tiền lương bình quân của 06 tháng liền kề trước khi thôi việc.

**Lượt tìm:** `trợ cấp thôi việc tính theo năm làm việc` (filter None, none)

> **[e3c977d516130853]** blld-2019 · Điều 46 · trang [19]
>
> Điều 46. Trợ cấp thôi việc 1. Khi hợp đồng lao động chấm dứt theo quy định tại các khoản 1, 2,3, 4,6,7,9và 10 Điều 34 của Bộ luật này thì người sử dụng lao động có trách nhiệm trả trợ cấp thôi việc cho người lao động đã làm việc thường xuyên cho mình từ đủ 12 tháng trở lên, mỗi năm làm việc được trợ cấp một nửa tháng tiền lương, trừ trường hợp đủ điều kiện hưởng lương hưu theo quy định của pháp luật về bảo hiểm xã hội và trường hợp quy định tại điểm e khoản 1 Điều 36 của Bộ luật này. 2. Thời gian làm việc để tính trợ cấp thôi việc là tổng thời gian người lao động đã làm việc thực tế cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiểm thất nghiệp theo quy định của pháp luật về bảo hiểm thất nghiệp và thời gian làm việc đã được người sử dụng lao động chỉ trả trợ cấp thôi việc, trợ cấp mất việc làm. 3 Tiền lương để tính trợ cấp thôi việc là tiền lương bình quân c

> **[a099008554b28f45]** blld-2012 · Điều 48 · trang [15, 16]
>
> Điều 48. Trợ cấp thôi việc 1. Khi hợp đồng lao động chấm dứt theo quy định tại các khoản 1,2,3, 5,6, 7, 9 và 10 Điều 36 của Bộ luật này thì người sử dụng lao động có trách nhiệm chi trả trợ cấp thôi việc cho người lao động đã làm việc thường xuyên từ đủ 12 tháng trở lên, mỗi năm làm việc được trợ cấp một nửa tháng tiền lương. 2. Thời gian làm việc đề tính trợ cấp thôi việc là tổng thời gian người lao động đã làm việc thực tế cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiểm thất nghiệp theo quy định của Luật bảo hiểm xã hội và thời gian làm việc đã được người sử dụng lao động chỉ trả trợ cấp thôi việc. ló 3. Tiền lương đề tính trợ cấp thôi việc là tiền lương bình quân theo hợp đồng lao động của 06 tháng liên kê trước khi người lao động thôi việc.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q10 · status `answered`

**Câu hỏi:** Người lao động bị mất việc làm được nhận trợ cấp tối thiểu bằng bao nhiêu tháng lương?

**Kỳ vọng:** Mỗi năm làm việc trả 01 tháng tiền lương nhưng ít nhất bằng 02 tháng tiền lương.

**Agent trả lời:** Người lao động bị mất việc làm được nhận trợ cấp mất việc làm tối thiểu bằng 02 tháng tiền lương [e174576b407acec5].

**Lượt tìm:** `trợ cấp thôi việc tối thiểu tháng lương` (filter None, none)

> **[e174576b407acec5]** blld-2012 · Điều 49 · trang [16]
>
> Điều 49. Trợ cấp mất việc làm ]. Người sử dụng lao động trả trợ cấp mất việc làm cho người lao động đã làm việc thường xuyên cho mình từ 12 tháng trở lên mà bị mất việc làm theo quy định tại Điều 44 và Điều 45 của Bộ luật này, mỗi năm làm việc trả 0] tháng tiền lương nhung ít nhất phải bằng 02 tháng tiền lương. 2. Thời gian làm việc để tính trợ cấp mắt việc làm là tông thời gian người lao động đã làm việc thực tê cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiêm thật nghiệp theo quy định của Luật bảo hiêm xã hội và thời gian làm việc đã được người sử dụng lao động ch trả trợ cấp thôi việc. mm Tiền lương để tính trợ cấp mất việc làm là tiền lương bình quân theo hợp đông lao động của 06 tháng liên kê trước khi người lao động mât việc làm.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q11 · status `answered`

**Câu hỏi:** Khi chấm dứt hợp đồng lao động, thời hạn thanh toán các khoản tiền giữa hai bên có thể được kéo dài tối đa bao nhiêu ngày?

**Kỳ vọng:** Không quá 30 ngày (bản 2019: chỉ trong các trường hợp liệt kê tại khoản 1 Điều 48; bản 2012: trường hợp đặc biệt).

**Agent trả lời:** Theo Bộ luật Lao động 2012, thời hạn thanh toán các khoản tiền giữa hai bên khi chấm dứt hợp đồng lao động là 07 ngày làm việc, có thể kéo dài nhưng không quá 30 ngày [0cbc2d076afca5c4].

Theo Bộ luật Lao động 2019, thời hạn thanh toán là 14 ngày làm việc, trừ các trường hợp đặc biệt có thể kéo dài nhưng không quá 30 ngày [2a48cb65dea01121].

**Lượt tìm:** `thanh toán tiền lương và các khoản tiền khác khi chấm dứt hợp đồng lao động thời hạn` (filter None, none)

> **[0cbc2d076afca5c4]** blld-2012 · Điều 47 · trang [15]
>
> Điều 47. Trách nhiệm của người sử dụng lao động khi chấm dứt hợp đồng lao động ]. Ít nhất 15 ngày trước ngày hợp đồng lao động xác định thời hạn hết hạn, người sử dụng lao động phải thông báo bằng văn bản cho người lao động biết thời điểm chấm dứt hợp đồng lao động. 2. Trong thời hạn 07 ngày làm việc, kể từ ngày chấm dứt hợp đồng lao động, hai bên có trách nhiệm thanh toán đây đủ các khoản có liên quan đến quyền lợi của mỗi bên; trường hợp đặc biệt, có thể kéo dài nhưng không được quá 30 ngày. 3. Người sử dụng lao động có trách nhiệm hoàn thành thủ tục xác nhận và trả lại sô bảo hiêm xã hội và những giây tờ khác mà người sử dụng lao động đã giữ lại của người lao động. 4. Trong trường hợp doanh nghiệp, hợp tác xã bị chấm dứt hoạt động, bị giải thể, phá sản thì tiền lương, trợ cấp thôi việc, bảo hiểm xã hội, bảo hiểm y tế, bảo hiểm thất nghiệp và các quyền lợi khác của người lao động theo 

> **[2a48cb65dea01121]** blld-2019 · Điều 48 · trang [19, 20]
>
> Điều 48. Trách nhiệm khi chấm dứt hợp đồng lao động 1. Trong thời hạn 14 ngày làm việc. kể từ ngày chấm đứt hợp đồng lao động, hai bên có trách nhiệm thanh toán đầy đủ các khoản tiền có liên quan đến quyền lợi của mỗi bên, trừ trường hợp sau đây có thể kéo đài nhưng không được quá 30 ngày: a) Người sử dụng lao động không phải là cá nhân chấm dứt hoạt động; b) Người sử dụng lao động thay đổi cơ cầu, công nghệ hoặc vì lý do kinh tế; c) Chia, tách, hợp nhất, sáp nhập; bán, cho thuê, chuyển đổi loại hình doanh nghiệp; chuyên nhượng quyền sở hữu, quyên sử dụng tài sản của doanh nghiệp, hợp tác xã; d) Do thiên tai, hỏa hoạn, địch họa hoặc dịch bệnh nguy hiểm. 2. Tiền lương, bảo hiểm xã hội, bảo hiểm y tế, bảo hiểm thất nghiệp, trợ cấp thôi việc và các quyên lợi khác của người lao động theo thỏa ước lao động tập thê, hợp đông lao động được ưu tiên thanh toán trong trường hợp doanh nghiệp, hợp t

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q12 · status `answered`

**Câu hỏi:** Giờ làm việc ban đêm được tính từ mấy giờ đến mấy giờ?

**Kỳ vọng:** Từ 22 giờ đến 06 giờ sáng ngày hôm sau.

**Agent trả lời:** Giờ làm việc ban đêm được tính từ 22 giờ đến 06 giờ sáng ngày hôm sau theo quy định tại Điều 106 Bộ luật Lao động 2019 [f8097e0a7bdcadcf].

Cũng theo Điều 105 Bộ luật Lao động 2012, giờ làm việc ban đêm được tính từ 22 giờ đến 6 giờ sáng ngày hôm sau [43ef3ba1a0f56f9c].

**Lượt tìm:** `giờ làm việc ban đêm` (filter None, none)

> **[f8097e0a7bdcadcf]** blld-2019 · Điều 106 · trang [40]
>
> Điều 106. Giờ làm việc ban đêm Giờ làm việc ban đêm được tính từ 22 giờ đến 06 giờ sáng ngày hôm sau.

> **[43ef3ba1a0f56f9c]** blld-2012 · Điều 105 · trang [30]
>
> Điều 105. Giờ làm việc ban đêm Giờ làm việc ban đêm được tính từ 22 giờ đến 6 giờ sáng ngày hôm sau.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q13 · status `answered`

**Câu hỏi:** Người làm ca đêm được nghỉ giữa ca ít nhất bao nhiêu phút?

**Kỳ vọng:** Ít nhất 45 phút (bản 2019 ghi rõ là 45 phút liên tục).

**Agent trả lời:** Người làm ca đêm được nghỉ giữa ca ít nhất 45 phút liên tục theo quy định tại Điều 109 của Bộ luật Lao động 2019 [5a45954688b086dc].

**Lượt tìm:** `nghỉ giữa ca người làm ca đêm` (filter None, none)

> **[5a45954688b086dc]** blld-2019 · Điều 109 · trang [41]
>
> Điều 109. Nghĩ trong giờ làm việc 1. Người lao động làm việc theo thời giờ làm việc quy định tại Điều 105 của Bộ luật này từ 06 giờ trở lên trong một ngày thì được nghỉ giữa giờ ít nhất 30 phút liên tục, làm việc ban đêm thì được nghỉ giữa giờ ít nhất 45 phút liên tục. Trường hợp người lao động làm việc theo ca liên tục từ 06 giờ trở lên thì thời gian nghỉ giữa giờ được tính vào giờ làm việc. 2. Ngoài thời gian nghỉ quy định tại khoản 1 Điều này, người sử dụng lao động bố trí cho người lao động các đợt nghỉ giải lao và ghi vào nội quy lao động.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q14 · status `answered`

**Câu hỏi:** Người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bao nhiêu?

**Kỳ vọng:** Ít nhất bằng 300%, chưa kể tiền lương ngày lễ đối với người lao động hưởng lương ngày.

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bằng 300% chưa kể tiền lương ngày lễ, tết, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày [8bf032c21470d951].

Theo Bộ luật Lao động 2012, người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bằng 300% chưa kể tiền lương ngày lễ, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày [43cd550df5a10ee9].

**Lượt tìm:** `làm thêm giờ ngày nghỉ lễ trả lương` (filter None, none)

> **[8bf032c21470d951]** blld-2019 · Điều 98 · trang [37]
>
> Điều 98. Tiền lương làm thêm giờ, làm việc vào ban đêm 1. Người lao động làm thêm giờ được trả lương tính theo đơn giá tiền lương hoặc tiền lương thực trả theo công việc đang làm như sau: a) Vào ngày thường, ít nhất bằng 150%; b) Vào ngày nghỉ hằng tuần, ít nhất bằng 200%; c) Vào ngày nghỉ lễ, tết, "ngày nghỉ có hưởng lương, ít nhất bằng 300% chưa kể tiền lương ngày lễ, tết, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày. 2. _Người lao động làm việc vào ban đêm thì được trả thêm ít nhất bằng 30% tiền lương tính theo đơn giá tiền lương hoặc tiền lương thực trả theo công việc của ngày làm việc bình thường. 3. Người lao động làm thêm giờ vào ban đêm thì ngoài việc trả lương theo quy định tại khoản 1 và khoản 2 Điều này, người lao động còn được trả thêm 20% tiền lương tính theo đơn giá tiền lương hoặc tiền lương theo công việc làm vào ban ngày của ngày làm việc bình thường 

> **[43cd550df5a10ee9]** blld-2012 · Điều 97 · trang [28, 29]
>
> Điều 97. Tiền lương làm thêm giờ, làm việc vào ban đêm 1. Người lao động làm thêm giờ được trả lương tính theo đơn giá tiền lương hoặc tiên lương theo công việc đang làm như sau: a) Vào ngày thường, ít nhất bằng 150%; b) Vào ngày nghỉ hằng tuần, ít nhất bằng 200%; c) Vào ngày nghỉ lễ, ngày nghỉ có hưởng lương, ít nhất băng 300% chua kể tiền lương ngày lễ, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày. 2. Người lao động làm việc vào ban đêm, thì được trả thêm ít nhất băng 30% tiền lương tính theo đon giá tiền lương hoặc tiền lương theo công việc của ngày làm việc bình thường. 3. Người lao động làm thêm giờ vào ban đêm thì ngoài việc trả lương theo quy định tại khoản 1 và khoản 2 Điều này, người lao động còn được trả thêm 20% tiền lương tính theo đơn giá tiền lương hoặc tiền lương theo công việc làm vào ban ngày.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q15 · status `answered`

**Câu hỏi:** Người làm công việc nặng nhọc, độc hại, nguy hiểm được nghỉ hằng năm bao nhiêu ngày?

**Kỳ vọng:** 14 ngày làm việc (16 ngày nếu là công việc đặc biệt nặng nhọc, độc hại, nguy hiểm).

**Agent trả lời:** Người lao động làm công việc nặng nhọc, độc hại, nguy hiểm được nghỉ hằng năm 14 ngày làm việc.

Căn cứ:
- Bộ luật Lao động 2012, Điều 111, khoản 1, điểm b) [b268f97122b4fcbd]: "14 ngày làm việc đối với người làm công việc nặng nhọc, độc hại, nguy hiểm...".
- Bộ luật Lao động 2019, Điều 113, khoản 1, điểm b) [3fe27b9fd53b4099]: "14 ngày làm việc đối với... người làm nghề, công việc nặng nhọc, độc hại, nguy hiểm".

**Lượt tìm:** `nghỉ hằng năm người lao động làm công việc nặng nhọc độc hại nguy hiểm` (filter None, none)

> **[b268f97122b4fcbd]** blld-2012 · Điều 111 · trang [32]
>
> Điều 111. Nghỉ hằng năm 1. Người lao động có đủ 12 tháng làm việc cho một người sử dụng lao động thì được nghỉ hăng năm, hưởng nguyên lương theo hợp đông lao động như sau: a) 12 ngày làm việc đối với người làm công việc trong điều kiện bình thường: b) 14 ngày làm việc đối với người làm công việc nặng nhọc, độc hại, nguy hiểm hoặc người làm việc ở những nơi có có điều kiện sinh sống khắc nghiệt theo danh mục do Bộ Lao động - Thương binh và Xã hội chủ trì phối hợp với Bộ Y tế ban hành hoặc lao động chưa thành niên hoặc lao động là người khuyêt tật; c) 16 ngày làm việc đối với người làm công việc đặc biệt nặng nhọc, độc hại, nguy hiểm hoặc người làm việc ở những nơi có điều kiện sinh sống đặc biệt khắc nghiệt theo danh mục do Bộ Lao động - Thương bình và Xã hội chủ trì ì phối hợp với Bộ Y tế ban hành. 2. Người sử dụng lao động có quyền quy định lịch nghi hằng năm sau khi tham khảo ý kiên củ

> **[3fe27b9fd53b4099]** blld-2019 · Điều 113 · trang [42]
>
> Điều 113. Nghĩ hằng năm l 1. Người lao động làm việc đủ 12 tháng cho một người sử dụng lao động thì được nghỉ hăng năm, hưởng nguyên lương theo hợp đông lao động như sau: a) 12 ngày làm việc đối với người làm công việc trong điều kiện bình thường: b) 14 ngày làm việc đối với người lao động chưa thành niên, lao động là người khuyêt tật, người làm nghề, công việc nặng nhọc, độc hại, nguy hiểm; c) 16 ngày làm việc đối với người làm nghề, công việc đặc biệt nặng nhọc, độc hại, nguy hiêm. 2. Người lao động làm việc chưa đủ 12 tháng cho một người sử dụng lao động thì sô ngày nghỉ hăng năm theo tỷ lệ tương ứng với sô tháng làm việc. 3. Trường hợp do thôi việc, bị mất việc làm mà chưa nghỉ hằng năm hoặc chưa nghỉ hết số ngày nghỉ hăng năm thì được người sử dụng lao động thanh toán tiên lương cho những ngày chưa nghỉ... 4. Người sử dụng lao động có trách nhiệm quy định lịch nghỉ hằng năm sau khi 

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q16 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2012, người lao động được hưởng lương hưu khi đủ bao nhiêu tuổi?

**Kỳ vọng:** Nam đủ 60 tuổi, nữ đủ 55 tuổi (khi bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội).

**Agent trả lời:** Theo Bộ luật Lao động 2012, người lao động được hưởng lương hưu khi nam đủ 60 tuổi, nữ đủ 55 tuổi [67976ce3fa4d3293].

**Lượt tìm:** `tuổi hưởng lương hưu người lao động` (filter {'year': 2012}, inferred)

> **[67976ce3fa4d3293]** blld-2012 · Điều 187 · trang [52]
>
> Điều 187. Tuổi nghỉ hưu 1. Người lao động bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội theo quy định của pháp luật về bảo hiểm xã hội được hưởng lương hưu khi nam đủ 60 tuổi, nữ đủ 55 tuổi. 2. Người lao động bị suy giảm khả năng lao động; làm công việc đặc biệt nặng nhọc, độc hại, nguy hiểm; làm công việc nặng nhọc, độc hại, nguy hiểm; làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo thuộc danh mục do Chính phủ quy định có thể nghỉ hưu ở tuổi thấp hơn so với quy định tại khoản 1 Điều này. 3. Người lao động có trình độ chuyên môn kỹ thuật cao, người lao động làm công tác quản lý và một số trường hợp đặc biệt khác có thể nghỉ hưu ở tuổi cao hơn nhưng không quá 05 năm so với quy định tại khoản 1 Điều này. 4. Chính phủ quy định chi tiết khoản 2 và khoản 3 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q17 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, từ năm 2021 tuổi nghỉ hưu của lao động nữ trong điều kiện lao động bình thường là bao nhiêu?

**Kỳ vọng:** Đủ 55 tuổi 04 tháng; sau đó mỗi năm tăng thêm 04 tháng cho đến khi đủ 60 tuổi vào năm 2035.

**Agent trả lời:** Theo Bộ luật Lao động 2019, từ năm 2021, tuổi nghỉ hưu của lao động nữ trong điều kiện lao động bình thường là đủ 55 tuổi 04 tháng [c40fad20889e6976].

**Lượt tìm:** `tuổi nghỉ hưu lao động nữ điều kiện lao động bình thường` (filter {'year': 2019}, inferred)

> **[c40fad20889e6976]** blld-2019 · Điều 169 · trang [60]
>
> Điều 169. Tuổi nghỉ hưu 1. Người lao động bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội theo quy định của pháp luật về bảo hiểm xã hội được hưởng lương hưu khi đủ tuôi nghỉ hưu. 2. Tuổi nghỉ hưu của người lao động trong điều kiện lao động bình thường được điều chỉnh theo lộ trình cho đên khi đủ 62 tuổi đối với lao động nam vào năm 2028 và đủ 60 tuôi đôi với lao động nữ vào năm 2035. Kể từ năm 2021, tuổi nghỉ hưu của người lao động trong điều kiện lao động bình thường là đủ 60 tuổi 03 tháng đối với lao động nam và đủ 55 tuổi 04 tháng đối với lao động nữ; sau đó, cứ mỗi năm tăng thêm 03 tháng đối với lao động nam và 04 tháng đối với lao động nữ. 3. Người lao động bị suy giảm khả năng lao động; làm nghề, công việc đặc biệt nặng nhọc, độc hại, nguy hiểm; làm nghề, công việc nặng nhọc, độc hại, nguy hiểm; làm việc ở vùng có điều kiện kinh tế - xã hội đặc biệt khó khăn có thể nghỉ hưu ở 

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q18 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, người lao động được nghỉ bao nhiêu ngày vào dịp Quốc khánh?

**Kỳ vọng:** 02 ngày (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau).

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động được nghỉ 02 ngày vào dịp Quốc khánh (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau) [70c23213ef936eb5].

**Lượt tìm:** `nghỉ lễ Quốc khánh` (filter {'year': 2019}, inferred)

> **[70c23213ef936eb5]** blld-2019 · Điều 112 · trang [41, 42]
>
> Điều 112. Nghỉ lễ, tết 1. Người lao động được nghỉ làm việc, hưởng nguyên lương trong những ngày lỗ, tết sau đây: a) Tết Dương lịch: 01 ngày (ngày 01 tháng 01 đương lịch); b) Tết Âm lịch: 05 ngày; c) Ngày Chiến thắng: 01 ngày (ngày 30 tháng 4 dương lịch); d) Ngày Quốc tế lao động: 01 ngày (ngày 01 tháng 5 dương lịch); đ) Quốc khánh: 02 ngày (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau); e) Ngày Giỗ Tổ Hùng Vương: 01 ngày (ngày 10 tháng 3 âm lịch). 2. Lao động là người nước ngoài làm việc tại Việt Nam ngoài các ngày nghỉ theo quy định tại khoản 1 Điều này còn được nghỉ thêm 01 ngày Tết cổ truyền dân tộc và 01 ngày Quốc khánh của nước họ. 3. Hằng năm, căn cứ vào điều kiện thực tế, Thủ tướng Chính phủ quyết định cụ thể ngày nghỉ quy định tại điêm b và điểm đ khoản 1 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q19 · status `answered`

**Câu hỏi:** Nếu nhân viên vi phạm liên quan trực tiếp đến tài sản của công ty thì thời hiệu xử lý kỷ luật lao động là bao lâu?

**Kỳ vọng:** 12 tháng (thay vì 06 tháng như thông thường).

**Agent trả lời:** Theo Bộ luật Lao động 2019, thời hiệu xử lý kỷ luật lao động đối với hành vi vi phạm liên quan trực tiếp đến tài sản của người sử dụng lao động là 12 tháng [ddd5e6ef6c45d7a2].

Theo Bộ luật Lao động 2012, thời hiệu xử lý kỷ luật lao động đối với hành vi vi phạm liên quan trực tiếp đến tài sản của người sử dụng lao động là 12 tháng [4829c9234e35ab72].

**Lượt tìm:** `thời hiệu xử lý kỷ luật lao động vi phạm tài sản` (filter None, none)

> **[ddd5e6ef6c45d7a2]** blld-2019 · Điều 123 · trang [46]
>
> Điều 123. Thời hiệu xử lý kỷ luật lao động 1. Thời hiệu xử lý kỷ luật lao động là 06 tháng kể từ ngày xảy ra hành vi vi phạm; trường hợp hành vi vi phạm liên quan trực tiếp đến tài chính, tài sản, tiệt lộ bí mật công nghệ, bí mật kinh doanh của người sử dụng lao động thì thời hiệu xử lý kỷ luật lao động là 12 tháng. 2. Khi hết thời gian quy định tại khoản 4 Điều 122 của Bộ luật này, nếu hết thời hiệu hoặc còn thời hiệu nhưng không đủ 60 ngày thì được kéo dài thời hiệu đê xử lý kỷ luật lao động nhưng không quá 60 ngày kề từ ngày hết thời gian nêu trên. 3. Người sử dụng lao động phải ban hành quyết định xử lý kỷ luật lao động trong thời hạn quy định tại khoản 1 và khoản 2 Điều này.

> **[4829c9234e35ab72]** blld-2012 · Điều 124 · trang [35, 36]
>
> Điều 124. Thời hiệu xử lý kỷ luật lao động 1. Thời hiệu xử lý kỷ luật lao động tối đa là 06 tháng, kể từ ngày xảy ra hành vi vi phạm; trường hợp hành vi vi phạm liên quan trực tiếp đến tài chính, tài sản, tiết lộ bí mật công nghệ, bí mật kinh doanh của người sử dụng lao động thì thời hiệu xử lý kỷ luật lao động tối đa là 12 tháng. 2. Khi hết thời gian quy định tại các điểm a, b và c khoản 4 Điều 123, nếu còn thời hiệu đề xử lý kỷ luật lao động thì người sử dụng lao động tiền hành xử lý kỹ luật lao động ngay, nếu hết thời hiệu thì được kéo dài thời hiệu để xử lý kỷ luật lao động nhưng tôi đa không quá 60 ngày kế từ ngày hết thời gian nêu trên. so Khi hết thời gian quy định tại điểm d khoản 4 Điều 123, mà thời hiệu xử lý kỷ luật lao động đã hết thì được kéo dài thời hiệu xử lý kỷ luật lao động nhưng tôi đa không quá 60 ngày kê từ ngày hết thời gian nêu trên. 3. Quyết định xử lý kỷ luật lao

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · q20 · status `answered`

**Câu hỏi:** Lao động nữ mang thai làm việc ở vùng cao hoặc hải đảo không được bố trí làm việc ban đêm kể từ tháng thai thứ mấy?

**Kỳ vọng:** Từ tháng thứ 06 (thay vì tháng thứ 07 như nơi khác).

**Agent trả lời:** Lao động nữ mang thai làm việc ở vùng cao hoặc hải đảo không được bố trí làm việc ban đêm kể từ tháng thai thứ 06.

Căn cứ:
- Bộ luật Lao động 2012, Điều 155, khoản 1, điểm a [ffe02f16c93fddb4].
- Bộ luật Lao động 2019, Điều 137, khoản 1, điểm a [53201ad6737fab80].

**Lượt tìm:** `lao động nữ mang thai vùng cao hải đảo không được bố trí làm việc ban đêm` (filter None, none)

> **[ffe02f16c93fddb4]** blld-2012 · Điều 155 · trang [44]
>
> Điều 155. Bảo vệ thai sản đối với lao động nữ 1. Người sử dụng lao động không được sử dụng lao động nữ làm việc ban đêm, làm thêm giờ và đi công tác xa trong các trường hợp sau đây: a) Mang thai từ tháng thứ 07 hoặc từ tháng thứ 06 nếu làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo; b) Đang nuôi con dưới 12 tháng tuổi. 2. Lao động nữ làm công việc nặng nhọc khi mang thai từ tháng thứ 07, được chuyển làm công việc nhẹ hơn hoặc được giảm bớt 01 giờ làm việc hằng ngày mà vân hưởng đủ lương. 3. Người sử dụng lao động không được sa thải hoặc đơn phương chấm dứt hợp đồng lao động đối với lao động nữ vì lý do kết hôn, mang thai, nghỉ thai sản, nuôi con dưới 12 tháng tuổi, trừ trường hợp người sử dụng lao động là cá nhân chết, bị Tòa án tuyên bố mất năng lực hành vi dân sự, mât tích hoặc là đã chết hoặc người sử dụng lao động không phải là cá nhân chấm dứt hoạt động. 4. Trong thời gi

> **[53201ad6737fab80]** blld-2019 · Điều 137 · trang [50]
>
> Điều 137. Bảo vệ thai sản 1. Người sử dụng lao động không được sử dụng người lao động làm việc ban đêm, làm thêm giờ và đi công tác xa trong trường hợp sau đây: a) Mang thai từ tháng thứ 07 hoặc từ tháng thứ 06 nếu làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo; b) Đang nuôi con đưới 12 tháng tuổi, trừ trường hợp được người lao động đồng ý. 2. Lao động nữ làm nghề, công việc nặng nhọc, độc hại, nguy hiểm hoặc đặc biệt nặng nhọc, độc hại, nguy hiêm hoặc làm nghề, công việc có ảnh hưởng xâu tới chức năng sinh sản và nuôi con khi mang thai và có thông báo cho người sử dụng lao động biết thì được người sử dụng lao động chuyển sang làm công việc nhẹ hơn, an toàn hơn hoặc giảm bớt 01 giờ làm việc hằng ngày mà không bị cắt giảm tiền lương và quyền, lợi ích cho đến hết thời gian nuôi con dưới 12 tháng tuổi,

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_inferred · u01 · status `answered`

**Câu hỏi:** Mức lương tối thiểu vùng I hiện nay là bao nhiêu đồng một tháng?

**Kỳ vọng:** (thiếu bằng chứng) Cả hai bộ luật chỉ nói mức lương tối thiểu (vùng) do Chính phủ quy định/công bố; không có con số tiền nào.

**Agent trả lời:** Bộ luật Lao động 2019 quy định về mức lương tối thiểu nhưng không nêu cụ thể con số. Con số này được Chính phủ ban hành trong các quyết định riêng biệt.

Theo Điều 91 Bộ luật Lao động 2019, mức lương tối thiểu được xác lập theo vùng và ấn định theo tháng [43fdabab0f59a94e].

Tuy nhiên, Bộ luật Lao động không ghi rõ mức lương tối thiểu vùng I hiện tại là bao nhiêu. Mức lương này được Chính phủ quy định chi tiết và công bố trong các văn bản pháp luật riêng (như Quyết định của Chính phủ).

**Lượt tìm:** `mức lương tối thiểu vùng` (filter {'year': 2019}, inferred)

> **[43fdabab0f59a94e]** blld-2019 · Điều 91 · trang [35]
>
> Điều 91. Mức lương tối thiếu 1. Mức lương tối thiểu là mức lương thấp nhất được trả cho người lao động làm công việc giản đơn nhất trong điều kiện lao động bình thường nhằm bảo đảm mức sống tối thiểu của người lao động và gia đình họ, phà hợp với điều kiện phát triển kinh tế - xã hội. 2. Mức lương tối thiểu được xác lập theo vùng, ấn định theo tháng, giờ. 3. Mức lường tối thiểu được điều chỉnh dựa trên mức sống tối thiểu của người lao động và gia đình họ; tương quan giữa mức lương tối thiểu và mức lương trên thị trường; chỉ số giá tiêu dùng, tốc độ tăng trưởng kinh tế; quan hệ cung, cầu lao động: việc làm và thất nghiệp; năng suất lao động; khả năng chỉ trả của doanh nghiệp. 4. Chính phủ quy định chi tiết Điều này; quyết định và công bố mức lương tối thiểu trên cơ sở khuyến nghị của Hội đồng tiền lương quốc gia.

*Nháp AI:* grade= · citation=true · abstention=false · Giống agent_dense_k3: không từ chối theo quy ước (status answered).

## agent_dense_inferred · u02 · status `abstain`

**Câu hỏi:** Người sử dụng lao động phải đóng bảo hiểm xã hội bắt buộc bằng bao nhiêu phần trăm quỹ tiền lương?

**Kỳ vọng:** (thiếu bằng chứng) Bộ luật chỉ quy định nghĩa vụ tham gia/đóng bảo hiểm xã hội theo pháp luật về bảo hiểm xã hội; không có tỷ lệ đóng.

**Agent trả lời:** Các đoạn tìm được trong Bộ luật Lao động 2012 và 2019 không nêu cụ thể tỷ lệ phần trăm người sử dụng lao động phải đóng bảo hiểm xã hội bắt buộc. Thông tin này thường được quy định trong Luật Bảo hiểm xã hội và các văn bản hướng dẫn thi hành.

Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời.

**Lượt tìm:** `tỷ lệ đóng bảo hiểm xã hội bắt buộc người sử dụng lao động` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối đúng, không đưa tỷ lệ nào. Có thêm câu 'thường quy định trong Luật BHXH/văn bản hướng dẫn', ý này khớp với dẫn chiếu 'theo pháp luật về BHXH' trong bộ luật. CẦN NGƯỜI DUYỆT (quy tắc: không thêm khẳng định vô căn cứ).

## agent_dense_inferred · u03 · status `abstain`

**Câu hỏi:** Người lao động làm việc từ xa tại nhà được hưởng phụ cấp bao nhiêu mỗi tháng?

**Kỳ vọng:** (thiếu bằng chứng) Không bộ luật nào quy định làm việc từ xa hay phụ cấp cho hình thức này.

**Agent trả lời:** Bộ luật Lao động 2019 và 2012 không quy định cụ thể mức phụ cấp cho người lao động làm việc từ xa tại nhà. Các điều luật tìm được chỉ đề cập đến việc người lao động có thể thỏa thuận nhận việc về làm tại nhà, nhưng không nêu rõ về phụ cấp hay mức lương cụ thể cho hình thức này.

Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời.

**Lượt tìm:** `phụ cấp làm việc từ xa tại nhà` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối đúng, không đưa con số phụ cấp. Câu giải thích (nếu có) chỉ nói bộ luật không quy định.

## agent_rerank_hybrid · q01 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, hai bên được giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn bao lâu?

**Kỳ vọng:** Hợp đồng có thời hạn dưới 01 tháng (trừ các trường hợp tại khoản 2 Điều 18, điểm a khoản 1 Điều 145 và khoản 1 Điều 162).

**Agent trả lời:** Theo Bộ luật Lao động 2019, hai bên được giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn dưới 01 tháng [410ba0a07076ab8d].

**Lượt tìm:** `hợp đồng lao động bằng lời nói thời hạn` (filter {'year': 2019}, user)

> **[410ba0a07076ab8d]** blld-2019 · Điều 14 · trang [6, 7]
>
> Điều 14. Hình thức hợp đồng lao động 1. Hợp đồng lao động phải được giao kết bằng văn bản và được làm thành 02 bản, người lao động giữ 01 bản, người sử dụng lao động giữ 01 bản, trừ trường hợp quy định tại khoản 2 Điều này. Hợp đồng lao động được giao kết thông qua phương tiện điện tử dưới hình thức thông điệp dữ liệu theo quy định của pháp luật về giao dịch điện tử có giá trị như bợp đồng lao động bằng văn bản. 2. Hai bên có thể giao kết hợp đồng lao động bằng lời nói đối với hợp đồng có thời hạn dưới 01 tháng, trừ trường hợp quy định tại khoản 2 Điều 18, điểm a khoản 1 Điều 145 và khoản 1 Điều 162 của Bộ luật này. Ss

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q02 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2012, công việc tạm thời có thời hạn bao lâu thì các bên được giao kết hợp đồng bằng lời nói?

**Kỳ vọng:** Công việc tạm thời có thời hạn dưới 03 tháng.

**Agent trả lời:** Theo Bộ luật Lao động 2012, các bên được giao kết hợp đồng lao động bằng lời nói đối với công việc tạm thời có thời hạn dưới 03 tháng [8b35e2d37ae827ce].

**Lượt tìm:** `hợp đồng bằng lời nói công việc tạm thời thời hạn` (filter {'year': 2012}, user)

> **[8b35e2d37ae827ce]** blld-2012 · Điều 16 · trang [6]
>
> Điều 16. Hình thức hợp đồng lao động 1. Hợp đồng lao động phải được giao kết bằng văn bản và được làm thành 02 bản, người lao động giữ 01 bản, người sử dụng lao động giữ 01 bản, trừ trường hợp quy định tại khoản 2 Điều này. 2. Đối với công việc tạm thời có thời hạn dưới 03 tháng, các bên có thể giao kết hợp đồng lao động bằng lời nói.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q03 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, số giờ làm thêm của người lao động tối đa trong một tháng là bao nhiêu?

**Kỳ vọng:** Không quá 40 giờ trong 01 tháng (và không quá 200 giờ/năm, trừ các trường hợp được làm đến 300 giờ/năm).

**Agent trả lời:** Theo Bộ luật Lao động 2019, số giờ làm thêm của người lao động tối đa trong một tháng là 40 giờ [71267d6e72a8bf88].

**Lượt tìm:** `số giờ làm thêm tối đa trong một tháng` (filter {'year': 2019}, user)

> **[71267d6e72a8bf88]** blld-2019 · Điều 107 · trang [40]
>
> Điều 107. Làm thêm giờ 1. Thời gian làm thêm giờ là khoảng thời gian làm việc ngoài thời giờ làm việc bình thường theo quy định của pháp luật, thỏa ước lao động tập thê hoặc nội quy lao động. 2. Người sử dụng lao động được sử dụng người lao động làm thêm giờ khi đáp ứng đây đủ các yêu câu sau đây: a) Phải được sự đồng ý của người lao động: b) Bảo đảm số giờ làm thêm của người lao động không quá 50% số giờ làm việc bình thường trong 01 ngày; trường hợp áp dụng quy định thời giờ làm việc bình thường theo tuân thì tổng số giờ làm việc bình thường và số giờ làm thêm không quá 12 giờ trong 01 ngày; không quá 40 giờ trong 01 tháng: c) Bảo đảm số giờ làm thêm của người lao động không quá 200 giờ trong 01 năm, trừ trường hợp quy định tại khoản 3 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q04 · status `answered`

**Câu hỏi:** Bộ luật Lao động 2012 giới hạn số giờ làm thêm trong một tháng là bao nhiêu?

**Kỳ vọng:** Không quá 30 giờ trong 01 tháng.

**Agent trả lời:** Theo Bộ luật Lao động 2012, số giờ làm thêm của người lao động trong một tháng không quá 30 giờ [3b164eb9c075d12a].

**Lượt tìm:** `giới hạn số giờ làm thêm trong một tháng` (filter {'year': 2012}, user)

> **[3b164eb9c075d12a]** blld-2012 · Điều 106 · trang [30, 31]
>
> Điều 106. Làm thêm giờ 1. Làm thêm giờ là khoảng thời gian làm việc ngoài thời giờ làm việc bình thường được quy định trong pháp luật, thỏa ước lao động tập thể hoặc theo nội quy. lao động. 2. Người sử dụng lao động được sử dụng người lao động làm thêm giờ khi đáp ứng đủ các điều kiện sau đây: a) Được sự đồng ý của người lao động: b) Bảo đảm số giờ làm thêm của người lao động không quá 50% số giờ làm việc bình thuờng trong 01 ngày, trường hợp áp dụng quy định làm việc theo tuần thì tông số giờ làm việc bình thường và số giờ làm thêm không quá 12 giờ trong 01 ngày, không quá 30 giờ trong 0] tháng và tông sô không quá 200 giờ trong 01 năm, trừ một sô trường hợp đặc biệt do Chính phủ quy định thì được làm thêm giờ không quá 300 giờ trong 01 năm; c) Sau mỗi đợt làm thêm giờ nhiều ngày liên tục trong tháng, người sử dụng lao động phải bô trí đề người lao động được nghỉ bù cho sô thời gian đã 

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q05 · status `answered`

**Câu hỏi:** Người được tuyển vào vị trí quản lý doanh nghiệp có thể phải thử việc tối đa bao nhiêu ngày?

**Kỳ vọng:** Không quá 180 ngày (quy định của Bộ luật Lao động 2019; bản 2012 không có mức riêng cho người quản lý doanh nghiệp).

**Agent trả lời:** Người được tuyển vào vị trí quản lý doanh nghiệp có thể phải thử việc tối đa 180 ngày theo quy định tại Điều 25 của Bộ luật Lao động 2019 [997d4c701fda2340].

**Lượt tìm:** `thử việc người lao động quản lý` (filter None, none)

> **[997d4c701fda2340]** blld-2019 · Điều 25 · trang [10]
>
> Điều 25. Thời gian thử việc Thời gian thử việc do hai bên thỏa thuận căn cứ vào tính chất và mức độ phức tạp của công việc nhưng chỉ được thử việc một lần đối với một công việc và bảo đảm điều kiện sau đây: 1. Không quá 180 ngày đối với công việc của người quản lý doanh nghiệp theo quy định của Luật Doanh nghiệp, Luật Quản lý, sử dụng vôn nhà nước đầu tư vào sản xuất, kinh doanh tại doanh nghiệp; 2. Không quá 60 ngày đối với công việc có chức danh nghề nghiệp cần trình độ chuyên môn, kỹ thuật từ cao đẳng trở lên; 3. Không quá 30 ngày đối với công việc có chức danh nghề nghiệp cần trình độ chuyên môn, kỹ thuật trung cấp, công nhân kỹ thuật, nhân viên nghiệp vụ; 4. Không quá 06 ngày làm việc đối với công việc khác.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q06 · status `answered`

**Câu hỏi:** Tiền lương trong thời gian thử việc ít nhất phải bằng bao nhiêu phần trăm mức lương của công việc đó?

**Kỳ vọng:** Ít nhất bằng 85% mức lương của công việc đó (giống nhau ở bản 2012 và 2019).

**Agent trả lời:** Theo Bộ luật Lao động 2012, tiền lương trong thời gian thử việc ít nhất phải bằng 85% mức lương của công việc đó [fbeaa39254552433].

Theo Bộ luật Lao động 2019, tiền lương trong thời gian thử việc cũng ít nhất phải bằng 85% mức lương của công việc đó [0eeeb5f152e2ed3b].

**Lượt tìm:** `tiền lương thời gian thử việc tỷ lệ phần trăm mức lương công việc` (filter None, none)

> **[fbeaa39254552433]** blld-2012 · Điều 28 · trang [9]
>
> Điều 28. Tiền lương trong thời gian thử việc Tiền lương của người lao động trong thời gian thử việc do hai bên thoả thuận nhưng ít nhất phải bằng 85% mức lương của công việc đó.

> **[0eeeb5f152e2ed3b]** blld-2019 · Điều 26 · trang [10]
>
> Điều 26. Tiền lương thứ việc Tiền lương của người lao động trong thời gian thử việc do hai bên thỏa thuận nhưng ít nhất phải băng 85% mức lương của công việc đó.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q07 · status `answered`

**Câu hỏi:** Nhân viên ký hợp đồng không thời hạn muốn tự nghỉ việc thì phải báo trước cho công ty ít nhất bao lâu?

**Kỳ vọng:** Ít nhất 45 ngày (bản 2012 có ngoại lệ cho lao động nữ mang thai theo Điều 156).

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động làm việc theo hợp đồng lao động không xác định thời hạn có quyền đơn phương chấm dứt hợp đồng lao động nhưng phải báo trước cho người sử dụng lao động ít nhất 45 ngày [88d5dd520c3fcef6].

Theo Bộ luật Lao động 2012, người lao động làm việc theo hợp đồng lao động không xác định thời hạn có quyền đơn phương chấm dứt hợp đồng lao động nhưng phải báo cho người sử dụng lao động biết trước ít nhất 45 ngày [c5de83b886428c5f].

**Lượt tìm:** `tự thôi việc hợp đồng không thời hạn báo trước` (filter None, none)

> **[88d5dd520c3fcef6]** blld-2019 · Điều 35 · trang [14]
>
> Điều 35. Quyền đơn phương chấm dứt hợp đồng lao động của người lao động 1. Người lao động có quyền đơn phương chấm dứt hợp đồng lao động nhưng phải báo trước cho người sử dụng lao động như sau: a) Ít nhất 45 ngày nếu làm việc theo hợp đồng lao động không xác định thời hạn; b) Ít nhất 30 ngày nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn từ 12 tháng đên 36 tháng: c) Ít nhất 03 ngày làm việc nếu làm việc theo hợp đồng lao động xác định thời hạn có thời hạn dưới 12 tháng: d) Đối với một số ngành, nghề, công việc đặc thù thì thời hạn báo trước được thực hiện theo quy định của Chính phủ.

> **[c5de83b886428c5f]** blld-2012 · Điều 37 · trang [12]
>
> Điều 37. Quyền đơn phương chấm đút hợp đồng lao động của người lao động 3. Người lao động làm việc theo hợp đồng lao động không xác định thời hạn có quyền đơn phương chấm dứt hợp đồng lao động, nhưng phải báo cho người sử dụng lao động biết trước ít nhất 45 ngày, trừ trường hợp quy định tại Điều 156 của Bộ luật này.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q08 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, nếu người lao động bị trả lương không đúng thời hạn thì có phải báo trước khi đơn phương chấm dứt hợp đồng không?

**Kỳ vọng:** Không cần báo trước, trừ trường hợp quy định tại khoản 4 Điều 97.

**Agent trả lời:** Theo Bộ luật Lao động 2019, nếu người lao động bị trả lương không đúng thời hạn thì **không cần báo trước** khi đơn phương chấm dứt hợp đồng lao động.

Căn cứ:
- Điều 35, khoản 2, mục b) quy định: "Người lao động có quyền đơn phương chấm dứt hợp đồng lao động không cần báo trước trong trường hợp... Không được trả đủ lương hoặc trả lương không đúng thời hạn, trừ trường hợp quy định tại khoản 4 Điều 97 của Bộ luật này" [ea3dc8618a0d48a9].

**Lượt tìm:** `người lao động bị trả lương không đúng thời hạn đơn phương chấm dứt hợp đồng` (filter {'year': 2019}, user)

> **[ea3dc8618a0d48a9]** blld-2019 · Điều 35 · trang [14]
>
> Điều 35. Quyền đơn phương chấm dứt hợp đồng lao động của người lao động 2. Người lao động có quyền đơn phương chấm đứt hợp đồng lao động không cân báo trước trong trường hợp sau đây: a) Không được bố trí theo đúng công việc, địa điểm làm việc hoặc không được bảo đảm điều kiện làm việc theo thỏa thuận, trừ trường hợp quy định tại Điêu 29 của Bộ luật này; b) Không được trả đủ lương hoặc trả lương không đúng thời hạn, trừ trường hợp quy định tại khoản 4 Điều 97 của Bộ luật này; c) Bị người sử dụng lao động ngược đãi, đánh đập hoặc có lời nói, hành vi nhục mạ, hành vi làm ảnh hưởng đến sức khỏe, nhân phẩm, danh dự; bị cưỡng bức lao động: d) Bị quấy rồi tình dục tại nơi làm việc; đ) Lao động nữ mang thai phải nghỉ việc theo quy định tại khoản 1 Điều 138 của Bộ luật này; e) Đủ tuổi nghỉ hưu theo quy định tại Điều 169 của Bộ luật này, trừ trường hợp các bên có thỏa thuận khác; g) Người sử dụng 

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q09 · status `answered`

**Câu hỏi:** Trợ cấp thôi việc được tính bao nhiêu cho mỗi năm làm việc?

**Kỳ vọng:** Mỗi năm làm việc được trợ cấp một nửa tháng tiền lương (áp dụng cho người làm việc thường xuyên từ đủ 12 tháng trở lên).

**Agent trả lời:** Theo Bộ luật Lao động 2012 và 2019, trợ cấp thôi việc được tính như sau:

- **Bộ luật Lao động 2012**: Mỗi năm làm việc, người lao động được trợ cấp một nửa tháng tiền lương [a099008554b28f45].
- **Bộ luật Lao động 2019**: Tương tự, mỗi năm làm việc, người lao động được trợ cấp một nửa tháng tiền lương, trừ một số trường hợp đặc biệt [e3c977d516130853].

Tiền lương để tính trợ cấp là tiền lương bình quân của 06 tháng liên tiếp trước khi thôi việc [a099008554b28f45, e3c977d516130853].

**Lượt tìm:** `trợ cấp thôi việc tính theo năm làm việc` (filter None, none)

> **[a099008554b28f45]** blld-2012 · Điều 48 · trang [15, 16]
>
> Điều 48. Trợ cấp thôi việc 1. Khi hợp đồng lao động chấm dứt theo quy định tại các khoản 1,2,3, 5,6, 7, 9 và 10 Điều 36 của Bộ luật này thì người sử dụng lao động có trách nhiệm chi trả trợ cấp thôi việc cho người lao động đã làm việc thường xuyên từ đủ 12 tháng trở lên, mỗi năm làm việc được trợ cấp một nửa tháng tiền lương. 2. Thời gian làm việc đề tính trợ cấp thôi việc là tổng thời gian người lao động đã làm việc thực tế cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiểm thất nghiệp theo quy định của Luật bảo hiểm xã hội và thời gian làm việc đã được người sử dụng lao động chỉ trả trợ cấp thôi việc. ló 3. Tiền lương đề tính trợ cấp thôi việc là tiền lương bình quân theo hợp đồng lao động của 06 tháng liên kê trước khi người lao động thôi việc.

> **[e3c977d516130853]** blld-2019 · Điều 46 · trang [19]
>
> Điều 46. Trợ cấp thôi việc 1. Khi hợp đồng lao động chấm dứt theo quy định tại các khoản 1, 2,3, 4,6,7,9và 10 Điều 34 của Bộ luật này thì người sử dụng lao động có trách nhiệm trả trợ cấp thôi việc cho người lao động đã làm việc thường xuyên cho mình từ đủ 12 tháng trở lên, mỗi năm làm việc được trợ cấp một nửa tháng tiền lương, trừ trường hợp đủ điều kiện hưởng lương hưu theo quy định của pháp luật về bảo hiểm xã hội và trường hợp quy định tại điểm e khoản 1 Điều 36 của Bộ luật này. 2. Thời gian làm việc để tính trợ cấp thôi việc là tổng thời gian người lao động đã làm việc thực tế cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiểm thất nghiệp theo quy định của pháp luật về bảo hiểm thất nghiệp và thời gian làm việc đã được người sử dụng lao động chỉ trả trợ cấp thôi việc, trợ cấp mất việc làm. 3 Tiền lương để tính trợ cấp thôi việc là tiền lương bình quân c

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q10 · status `answered`

**Câu hỏi:** Người lao động bị mất việc làm được nhận trợ cấp tối thiểu bằng bao nhiêu tháng lương?

**Kỳ vọng:** Mỗi năm làm việc trả 01 tháng tiền lương nhưng ít nhất bằng 02 tháng tiền lương.

**Agent trả lời:** Người lao động bị mất việc làm được nhận trợ cấp mất việc làm tối thiểu bằng 02 tháng tiền lương [e174576b407acec5].

**Lượt tìm:** `trợ cấp thôi việc tối thiểu tháng lương` (filter None, none)

> **[e174576b407acec5]** blld-2012 · Điều 49 · trang [16]
>
> Điều 49. Trợ cấp mất việc làm ]. Người sử dụng lao động trả trợ cấp mất việc làm cho người lao động đã làm việc thường xuyên cho mình từ 12 tháng trở lên mà bị mất việc làm theo quy định tại Điều 44 và Điều 45 của Bộ luật này, mỗi năm làm việc trả 0] tháng tiền lương nhung ít nhất phải bằng 02 tháng tiền lương. 2. Thời gian làm việc để tính trợ cấp mắt việc làm là tông thời gian người lao động đã làm việc thực tê cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiêm thật nghiệp theo quy định của Luật bảo hiêm xã hội và thời gian làm việc đã được người sử dụng lao động ch trả trợ cấp thôi việc. mm Tiền lương để tính trợ cấp mất việc làm là tiền lương bình quân theo hợp đông lao động của 06 tháng liên kê trước khi người lao động mât việc làm.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q11 · status `answered`

**Câu hỏi:** Khi chấm dứt hợp đồng lao động, thời hạn thanh toán các khoản tiền giữa hai bên có thể được kéo dài tối đa bao nhiêu ngày?

**Kỳ vọng:** Không quá 30 ngày (bản 2019: chỉ trong các trường hợp liệt kê tại khoản 1 Điều 48; bản 2012: trường hợp đặc biệt).

**Agent trả lời:** Theo Bộ luật Lao động 2019, thời hạn thanh toán các khoản tiền giữa hai bên khi chấm dứt hợp đồng lao động là 14 ngày làm việc. Trong các trường hợp đặc biệt (như doanh nghiệp chấm dứt hoạt động, thay đổi cơ cấu, thiên tai...), thời hạn này có thể kéo dài nhưng không quá 30 ngày [2a48cb65dea01121].

Theo Bộ luật Lao động 2012, thời hạn thanh toán là 07 ngày làm việc. Trong các trường hợp đặc biệt, thời hạn này có thể kéo dài nhưng không quá 30 ngày [0cbc2d076afca5c4].

**Lượt tìm:** `thanh toán tiền lương và các khoản tiền khác khi chấm dứt hợp đồng lao động thời hạn` (filter None, none)

> **[2a48cb65dea01121]** blld-2019 · Điều 48 · trang [19, 20]
>
> Điều 48. Trách nhiệm khi chấm dứt hợp đồng lao động 1. Trong thời hạn 14 ngày làm việc. kể từ ngày chấm đứt hợp đồng lao động, hai bên có trách nhiệm thanh toán đầy đủ các khoản tiền có liên quan đến quyền lợi của mỗi bên, trừ trường hợp sau đây có thể kéo đài nhưng không được quá 30 ngày: a) Người sử dụng lao động không phải là cá nhân chấm dứt hoạt động; b) Người sử dụng lao động thay đổi cơ cầu, công nghệ hoặc vì lý do kinh tế; c) Chia, tách, hợp nhất, sáp nhập; bán, cho thuê, chuyển đổi loại hình doanh nghiệp; chuyên nhượng quyền sở hữu, quyên sử dụng tài sản của doanh nghiệp, hợp tác xã; d) Do thiên tai, hỏa hoạn, địch họa hoặc dịch bệnh nguy hiểm. 2. Tiền lương, bảo hiểm xã hội, bảo hiểm y tế, bảo hiểm thất nghiệp, trợ cấp thôi việc và các quyên lợi khác của người lao động theo thỏa ước lao động tập thê, hợp đông lao động được ưu tiên thanh toán trong trường hợp doanh nghiệp, hợp t

> **[0cbc2d076afca5c4]** blld-2012 · Điều 47 · trang [15]
>
> Điều 47. Trách nhiệm của người sử dụng lao động khi chấm dứt hợp đồng lao động ]. Ít nhất 15 ngày trước ngày hợp đồng lao động xác định thời hạn hết hạn, người sử dụng lao động phải thông báo bằng văn bản cho người lao động biết thời điểm chấm dứt hợp đồng lao động. 2. Trong thời hạn 07 ngày làm việc, kể từ ngày chấm dứt hợp đồng lao động, hai bên có trách nhiệm thanh toán đây đủ các khoản có liên quan đến quyền lợi của mỗi bên; trường hợp đặc biệt, có thể kéo dài nhưng không được quá 30 ngày. 3. Người sử dụng lao động có trách nhiệm hoàn thành thủ tục xác nhận và trả lại sô bảo hiêm xã hội và những giây tờ khác mà người sử dụng lao động đã giữ lại của người lao động. 4. Trong trường hợp doanh nghiệp, hợp tác xã bị chấm dứt hoạt động, bị giải thể, phá sản thì tiền lương, trợ cấp thôi việc, bảo hiểm xã hội, bảo hiểm y tế, bảo hiểm thất nghiệp và các quyền lợi khác của người lao động theo 

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q12 · status `answered`

**Câu hỏi:** Giờ làm việc ban đêm được tính từ mấy giờ đến mấy giờ?

**Kỳ vọng:** Từ 22 giờ đến 06 giờ sáng ngày hôm sau.

**Agent trả lời:** Giờ làm việc ban đêm được tính từ 22 giờ đến 6 giờ sáng ngày hôm sau theo quy định tại Điều 105 của Bộ luật Lao động 2012 [43ef3ba1a0f56f9c] và Điều 106 của Bộ luật Lao động 2019 [f8097e0a7bdcadcf].

**Lượt tìm:** `giờ làm việc ban đêm` (filter None, none)

> **[43ef3ba1a0f56f9c]** blld-2012 · Điều 105 · trang [30]
>
> Điều 105. Giờ làm việc ban đêm Giờ làm việc ban đêm được tính từ 22 giờ đến 6 giờ sáng ngày hôm sau.

> **[f8097e0a7bdcadcf]** blld-2019 · Điều 106 · trang [40]
>
> Điều 106. Giờ làm việc ban đêm Giờ làm việc ban đêm được tính từ 22 giờ đến 06 giờ sáng ngày hôm sau.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q13 · status `answered`

**Câu hỏi:** Người làm ca đêm được nghỉ giữa ca ít nhất bao nhiêu phút?

**Kỳ vọng:** Ít nhất 45 phút (bản 2019 ghi rõ là 45 phút liên tục).

**Agent trả lời:** Người làm ca đêm được nghỉ giữa ca ít nhất 45 phút liên tục theo quy định tại Điều 109 của Bộ luật Lao động 2019 [5a45954688b086dc] và Điều 108 của Bộ luật Lao động 2012 [8cf77d2e8ed38c20].

**Lượt tìm:** `nghỉ giữa ca người làm ca đêm` (filter None, none)

> **[5a45954688b086dc]** blld-2019 · Điều 109 · trang [41]
>
> Điều 109. Nghĩ trong giờ làm việc 1. Người lao động làm việc theo thời giờ làm việc quy định tại Điều 105 của Bộ luật này từ 06 giờ trở lên trong một ngày thì được nghỉ giữa giờ ít nhất 30 phút liên tục, làm việc ban đêm thì được nghỉ giữa giờ ít nhất 45 phút liên tục. Trường hợp người lao động làm việc theo ca liên tục từ 06 giờ trở lên thì thời gian nghỉ giữa giờ được tính vào giờ làm việc. 2. Ngoài thời gian nghỉ quy định tại khoản 1 Điều này, người sử dụng lao động bố trí cho người lao động các đợt nghỉ giải lao và ghi vào nội quy lao động.

> **[8cf77d2e8ed38c20]** blld-2012 · Điều 108 · trang [31]
>
> Mục 2 THỜI GIỜ NGHỈ NGƠI Điều 108. Nghỉ trong giờ làm việc 1. Người lao động làm việc liên tục 08 giờ hoặc 06 giờ theo quy định tại Điều 104 của Bộ luật này được nghỉ giữa giờ ít nhât 30 phút, tính vào thời giờ làm việc. 2. Trường hợp làm việc ban đêm, thì người lao động được nghỉ giữa giờ ít nhât 45 phút, tính vào thời giờ làm việc. 3. Ngoài thời gian nghỉ giữa giờ quy định tại khoản 1 và khoản 2 Điều này, người sử dụng lao động quy định thời điểm các đợt nghỉ ngắn và ghi vào nội quy lao động.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q14 · status `answered`

**Câu hỏi:** Người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bao nhiêu?

**Kỳ vọng:** Ít nhất bằng 300%, chưa kể tiền lương ngày lễ đối với người lao động hưởng lương ngày.

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bằng 300% chưa kể tiền lương ngày lễ, tết, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày [8bf032c21470d951].

Theo Bộ luật Lao động 2012, người lao động làm thêm giờ vào ngày nghỉ lễ được trả lương ít nhất bằng 300% chưa kể tiền lương ngày lễ, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày [43cd550df5a10ee9].

**Lượt tìm:** `làm thêm giờ ngày nghỉ lễ trả lương` (filter None, none)

> **[8bf032c21470d951]** blld-2019 · Điều 98 · trang [37]
>
> Điều 98. Tiền lương làm thêm giờ, làm việc vào ban đêm 1. Người lao động làm thêm giờ được trả lương tính theo đơn giá tiền lương hoặc tiền lương thực trả theo công việc đang làm như sau: a) Vào ngày thường, ít nhất bằng 150%; b) Vào ngày nghỉ hằng tuần, ít nhất bằng 200%; c) Vào ngày nghỉ lễ, tết, "ngày nghỉ có hưởng lương, ít nhất bằng 300% chưa kể tiền lương ngày lễ, tết, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày. 2. _Người lao động làm việc vào ban đêm thì được trả thêm ít nhất bằng 30% tiền lương tính theo đơn giá tiền lương hoặc tiền lương thực trả theo công việc của ngày làm việc bình thường. 3. Người lao động làm thêm giờ vào ban đêm thì ngoài việc trả lương theo quy định tại khoản 1 và khoản 2 Điều này, người lao động còn được trả thêm 20% tiền lương tính theo đơn giá tiền lương hoặc tiền lương theo công việc làm vào ban ngày của ngày làm việc bình thường 

> **[43cd550df5a10ee9]** blld-2012 · Điều 97 · trang [28, 29]
>
> Điều 97. Tiền lương làm thêm giờ, làm việc vào ban đêm 1. Người lao động làm thêm giờ được trả lương tính theo đơn giá tiền lương hoặc tiên lương theo công việc đang làm như sau: a) Vào ngày thường, ít nhất bằng 150%; b) Vào ngày nghỉ hằng tuần, ít nhất bằng 200%; c) Vào ngày nghỉ lễ, ngày nghỉ có hưởng lương, ít nhất băng 300% chua kể tiền lương ngày lễ, ngày nghỉ có hưởng lương đối với người lao động hưởng lương ngày. 2. Người lao động làm việc vào ban đêm, thì được trả thêm ít nhất băng 30% tiền lương tính theo đon giá tiền lương hoặc tiền lương theo công việc của ngày làm việc bình thường. 3. Người lao động làm thêm giờ vào ban đêm thì ngoài việc trả lương theo quy định tại khoản 1 và khoản 2 Điều này, người lao động còn được trả thêm 20% tiền lương tính theo đơn giá tiền lương hoặc tiền lương theo công việc làm vào ban ngày.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q15 · status `answered`

**Câu hỏi:** Người làm công việc nặng nhọc, độc hại, nguy hiểm được nghỉ hằng năm bao nhiêu ngày?

**Kỳ vọng:** 14 ngày làm việc (16 ngày nếu là công việc đặc biệt nặng nhọc, độc hại, nguy hiểm).

**Agent trả lời:** Theo Bộ luật Lao động 2012, người lao động làm công việc nặng nhọc, độc hại, nguy hiểm được nghỉ hằng năm 14 ngày làm việc [b268f97122b4fcbd].

Theo Bộ luật Lao động 2019, người lao động làm công việc nặng nhọc, độc hại, nguy hiểm cũng được nghỉ hằng năm 14 ngày làm việc [3fe27b9fd53b4099].

**Lượt tìm:** `nghỉ hằng năm người lao động làm công việc nặng nhọc độc hại nguy hiểm` (filter None, none)

> **[b268f97122b4fcbd]** blld-2012 · Điều 111 · trang [32]
>
> Điều 111. Nghỉ hằng năm 1. Người lao động có đủ 12 tháng làm việc cho một người sử dụng lao động thì được nghỉ hăng năm, hưởng nguyên lương theo hợp đông lao động như sau: a) 12 ngày làm việc đối với người làm công việc trong điều kiện bình thường: b) 14 ngày làm việc đối với người làm công việc nặng nhọc, độc hại, nguy hiểm hoặc người làm việc ở những nơi có có điều kiện sinh sống khắc nghiệt theo danh mục do Bộ Lao động - Thương binh và Xã hội chủ trì phối hợp với Bộ Y tế ban hành hoặc lao động chưa thành niên hoặc lao động là người khuyêt tật; c) 16 ngày làm việc đối với người làm công việc đặc biệt nặng nhọc, độc hại, nguy hiểm hoặc người làm việc ở những nơi có điều kiện sinh sống đặc biệt khắc nghiệt theo danh mục do Bộ Lao động - Thương bình và Xã hội chủ trì ì phối hợp với Bộ Y tế ban hành. 2. Người sử dụng lao động có quyền quy định lịch nghi hằng năm sau khi tham khảo ý kiên củ

> **[3fe27b9fd53b4099]** blld-2019 · Điều 113 · trang [42]
>
> Điều 113. Nghĩ hằng năm l 1. Người lao động làm việc đủ 12 tháng cho một người sử dụng lao động thì được nghỉ hăng năm, hưởng nguyên lương theo hợp đông lao động như sau: a) 12 ngày làm việc đối với người làm công việc trong điều kiện bình thường: b) 14 ngày làm việc đối với người lao động chưa thành niên, lao động là người khuyêt tật, người làm nghề, công việc nặng nhọc, độc hại, nguy hiểm; c) 16 ngày làm việc đối với người làm nghề, công việc đặc biệt nặng nhọc, độc hại, nguy hiêm. 2. Người lao động làm việc chưa đủ 12 tháng cho một người sử dụng lao động thì sô ngày nghỉ hăng năm theo tỷ lệ tương ứng với sô tháng làm việc. 3. Trường hợp do thôi việc, bị mất việc làm mà chưa nghỉ hằng năm hoặc chưa nghỉ hết số ngày nghỉ hăng năm thì được người sử dụng lao động thanh toán tiên lương cho những ngày chưa nghỉ... 4. Người sử dụng lao động có trách nhiệm quy định lịch nghỉ hằng năm sau khi 

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q16 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2012, người lao động được hưởng lương hưu khi đủ bao nhiêu tuổi?

**Kỳ vọng:** Nam đủ 60 tuổi, nữ đủ 55 tuổi (khi bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội).

**Agent trả lời:** Theo Bộ luật Lao động 2012, người lao động được hưởng lương hưu khi nam đủ 60 tuổi, nữ đủ 55 tuổi [67976ce3fa4d3293].

**Lượt tìm:** `tuổi hưởng lương hưu người lao động` (filter {'year': 2012}, user)

> **[67976ce3fa4d3293]** blld-2012 · Điều 187 · trang [52]
>
> Điều 187. Tuổi nghỉ hưu 1. Người lao động bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội theo quy định của pháp luật về bảo hiểm xã hội được hưởng lương hưu khi nam đủ 60 tuổi, nữ đủ 55 tuổi. 2. Người lao động bị suy giảm khả năng lao động; làm công việc đặc biệt nặng nhọc, độc hại, nguy hiểm; làm công việc nặng nhọc, độc hại, nguy hiểm; làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo thuộc danh mục do Chính phủ quy định có thể nghỉ hưu ở tuổi thấp hơn so với quy định tại khoản 1 Điều này. 3. Người lao động có trình độ chuyên môn kỹ thuật cao, người lao động làm công tác quản lý và một số trường hợp đặc biệt khác có thể nghỉ hưu ở tuổi cao hơn nhưng không quá 05 năm so với quy định tại khoản 1 Điều này. 4. Chính phủ quy định chi tiết khoản 2 và khoản 3 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q17 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, từ năm 2021 tuổi nghỉ hưu của lao động nữ trong điều kiện lao động bình thường là bao nhiêu?

**Kỳ vọng:** Đủ 55 tuổi 04 tháng; sau đó mỗi năm tăng thêm 04 tháng cho đến khi đủ 60 tuổi vào năm 2035.

**Agent trả lời:** Theo Bộ luật Lao động 2019, từ năm 2021, tuổi nghỉ hưu của lao động nữ trong điều kiện lao động bình thường là đủ 55 tuổi 04 tháng [c40fad20889e6976].

**Lượt tìm:** `tuổi nghỉ hưu lao động nữ điều kiện lao động bình thường` (filter {'year': 2019}, user)

> **[c40fad20889e6976]** blld-2019 · Điều 169 · trang [60]
>
> Điều 169. Tuổi nghỉ hưu 1. Người lao động bảo đảm điều kiện về thời gian đóng bảo hiểm xã hội theo quy định của pháp luật về bảo hiểm xã hội được hưởng lương hưu khi đủ tuôi nghỉ hưu. 2. Tuổi nghỉ hưu của người lao động trong điều kiện lao động bình thường được điều chỉnh theo lộ trình cho đên khi đủ 62 tuổi đối với lao động nam vào năm 2028 và đủ 60 tuôi đôi với lao động nữ vào năm 2035. Kể từ năm 2021, tuổi nghỉ hưu của người lao động trong điều kiện lao động bình thường là đủ 60 tuổi 03 tháng đối với lao động nam và đủ 55 tuổi 04 tháng đối với lao động nữ; sau đó, cứ mỗi năm tăng thêm 03 tháng đối với lao động nam và 04 tháng đối với lao động nữ. 3. Người lao động bị suy giảm khả năng lao động; làm nghề, công việc đặc biệt nặng nhọc, độc hại, nguy hiểm; làm nghề, công việc nặng nhọc, độc hại, nguy hiểm; làm việc ở vùng có điều kiện kinh tế - xã hội đặc biệt khó khăn có thể nghỉ hưu ở 

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q18 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, người lao động được nghỉ bao nhiêu ngày vào dịp Quốc khánh?

**Kỳ vọng:** 02 ngày (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau).

**Agent trả lời:** Theo Bộ luật Lao động 2019, người lao động được nghỉ 02 ngày vào dịp Quốc khánh (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau) [70c23213ef936eb5].

**Lượt tìm:** `nghỉ lễ Quốc khánh` (filter {'year': 2019}, user)

> **[70c23213ef936eb5]** blld-2019 · Điều 112 · trang [41, 42]
>
> Điều 112. Nghỉ lễ, tết 1. Người lao động được nghỉ làm việc, hưởng nguyên lương trong những ngày lỗ, tết sau đây: a) Tết Dương lịch: 01 ngày (ngày 01 tháng 01 đương lịch); b) Tết Âm lịch: 05 ngày; c) Ngày Chiến thắng: 01 ngày (ngày 30 tháng 4 dương lịch); d) Ngày Quốc tế lao động: 01 ngày (ngày 01 tháng 5 dương lịch); đ) Quốc khánh: 02 ngày (ngày 02 tháng 9 dương lịch và 01 ngày liền kề trước hoặc sau); e) Ngày Giỗ Tổ Hùng Vương: 01 ngày (ngày 10 tháng 3 âm lịch). 2. Lao động là người nước ngoài làm việc tại Việt Nam ngoài các ngày nghỉ theo quy định tại khoản 1 Điều này còn được nghỉ thêm 01 ngày Tết cổ truyền dân tộc và 01 ngày Quốc khánh của nước họ. 3. Hằng năm, căn cứ vào điều kiện thực tế, Thủ tướng Chính phủ quyết định cụ thể ngày nghỉ quy định tại điêm b và điểm đ khoản 1 Điều này.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q19 · status `answered`

**Câu hỏi:** Nếu nhân viên vi phạm liên quan trực tiếp đến tài sản của công ty thì thời hiệu xử lý kỷ luật lao động là bao lâu?

**Kỳ vọng:** 12 tháng (thay vì 06 tháng như thông thường).

**Agent trả lời:** Nếu hành vi vi phạm của nhân viên liên quan trực tiếp đến tài sản của công ty, thời hiệu xử lý kỷ luật lao động là 12 tháng.

Căn cứ:
- Bộ luật Lao động 2019, Điều 123, Khoản 1 [ddd5e6ef6c45d7a2]
- Bộ luật Lao động 2012, Điều 124, Khoản 1 [4829c9234e35ab72]

**Lượt tìm:** `thời hiệu xử lý kỷ luật lao động vi phạm tài sản` (filter None, none)

> **[ddd5e6ef6c45d7a2]** blld-2019 · Điều 123 · trang [46]
>
> Điều 123. Thời hiệu xử lý kỷ luật lao động 1. Thời hiệu xử lý kỷ luật lao động là 06 tháng kể từ ngày xảy ra hành vi vi phạm; trường hợp hành vi vi phạm liên quan trực tiếp đến tài chính, tài sản, tiệt lộ bí mật công nghệ, bí mật kinh doanh của người sử dụng lao động thì thời hiệu xử lý kỷ luật lao động là 12 tháng. 2. Khi hết thời gian quy định tại khoản 4 Điều 122 của Bộ luật này, nếu hết thời hiệu hoặc còn thời hiệu nhưng không đủ 60 ngày thì được kéo dài thời hiệu đê xử lý kỷ luật lao động nhưng không quá 60 ngày kề từ ngày hết thời gian nêu trên. 3. Người sử dụng lao động phải ban hành quyết định xử lý kỷ luật lao động trong thời hạn quy định tại khoản 1 và khoản 2 Điều này.

> **[4829c9234e35ab72]** blld-2012 · Điều 124 · trang [35, 36]
>
> Điều 124. Thời hiệu xử lý kỷ luật lao động 1. Thời hiệu xử lý kỷ luật lao động tối đa là 06 tháng, kể từ ngày xảy ra hành vi vi phạm; trường hợp hành vi vi phạm liên quan trực tiếp đến tài chính, tài sản, tiết lộ bí mật công nghệ, bí mật kinh doanh của người sử dụng lao động thì thời hiệu xử lý kỷ luật lao động tối đa là 12 tháng. 2. Khi hết thời gian quy định tại các điểm a, b và c khoản 4 Điều 123, nếu còn thời hiệu đề xử lý kỷ luật lao động thì người sử dụng lao động tiền hành xử lý kỹ luật lao động ngay, nếu hết thời hiệu thì được kéo dài thời hiệu để xử lý kỷ luật lao động nhưng tôi đa không quá 60 ngày kế từ ngày hết thời gian nêu trên. so Khi hết thời gian quy định tại điểm d khoản 4 Điều 123, mà thời hiệu xử lý kỷ luật lao động đã hết thì được kéo dài thời hiệu xử lý kỷ luật lao động nhưng tôi đa không quá 60 ngày kê từ ngày hết thời gian nêu trên. 3. Quyết định xử lý kỷ luật lao

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · q20 · status `answered`

**Câu hỏi:** Lao động nữ mang thai làm việc ở vùng cao hoặc hải đảo không được bố trí làm việc ban đêm kể từ tháng thai thứ mấy?

**Kỳ vọng:** Từ tháng thứ 06 (thay vì tháng thứ 07 như nơi khác).

**Agent trả lời:** Lao động nữ mang thai làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo không được bố trí làm việc ban đêm kể từ tháng thai thứ 06.

Căn cứ:
- Điều 137, khoản 1, điểm a của Bộ luật Lao động 2019 [53201ad6737fab80].
- Điều 155, khoản 1, điểm a của Bộ luật Lao động 2012 [ffe02f16c93fddb4].

**Lượt tìm:** `lao động nữ mang thai vùng cao hải đảo không được bố trí làm việc ban đêm` (filter None, none)

> **[53201ad6737fab80]** blld-2019 · Điều 137 · trang [50]
>
> Điều 137. Bảo vệ thai sản 1. Người sử dụng lao động không được sử dụng người lao động làm việc ban đêm, làm thêm giờ và đi công tác xa trong trường hợp sau đây: a) Mang thai từ tháng thứ 07 hoặc từ tháng thứ 06 nếu làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo; b) Đang nuôi con đưới 12 tháng tuổi, trừ trường hợp được người lao động đồng ý. 2. Lao động nữ làm nghề, công việc nặng nhọc, độc hại, nguy hiểm hoặc đặc biệt nặng nhọc, độc hại, nguy hiêm hoặc làm nghề, công việc có ảnh hưởng xâu tới chức năng sinh sản và nuôi con khi mang thai và có thông báo cho người sử dụng lao động biết thì được người sử dụng lao động chuyển sang làm công việc nhẹ hơn, an toàn hơn hoặc giảm bớt 01 giờ làm việc hằng ngày mà không bị cắt giảm tiền lương và quyền, lợi ích cho đến hết thời gian nuôi con dưới 12 tháng tuổi,

> **[ffe02f16c93fddb4]** blld-2012 · Điều 155 · trang [44]
>
> Điều 155. Bảo vệ thai sản đối với lao động nữ 1. Người sử dụng lao động không được sử dụng lao động nữ làm việc ban đêm, làm thêm giờ và đi công tác xa trong các trường hợp sau đây: a) Mang thai từ tháng thứ 07 hoặc từ tháng thứ 06 nếu làm việc ở vùng cao, vùng sâu, vùng xa, biên giới, hải đảo; b) Đang nuôi con dưới 12 tháng tuổi. 2. Lao động nữ làm công việc nặng nhọc khi mang thai từ tháng thứ 07, được chuyển làm công việc nhẹ hơn hoặc được giảm bớt 01 giờ làm việc hằng ngày mà vân hưởng đủ lương. 3. Người sử dụng lao động không được sa thải hoặc đơn phương chấm dứt hợp đồng lao động đối với lao động nữ vì lý do kết hôn, mang thai, nghỉ thai sản, nuôi con dưới 12 tháng tuổi, trừ trường hợp người sử dụng lao động là cá nhân chết, bị Tòa án tuyên bố mất năng lực hành vi dân sự, mât tích hoặc là đã chết hoặc người sử dụng lao động không phải là cá nhân chấm dứt hoạt động. 4. Trong thời gi

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · u01 · status `answered`

**Câu hỏi:** Mức lương tối thiểu vùng I hiện nay là bao nhiêu đồng một tháng?

**Kỳ vọng:** (thiếu bằng chứng) Cả hai bộ luật chỉ nói mức lương tối thiểu (vùng) do Chính phủ quy định/công bố; không có con số tiền nào.

**Agent trả lời:** Bộ luật Lao động 2019 không quy định cụ thể con số mức lương tối thiểu vùng I hiện tại. Bộ luật này chỉ quy định nguyên tắc xác lập và điều chỉnh mức lương tối thiểu [43fdabab0f59a94e], đồng thời giao cho Chính phủ quy định chi tiết và công bố mức lương tối thiểu [43fdabab0f59a94e].

Do đó, để biết mức lương tối thiểu vùng I hiện nay, bạn cần tra cứu các văn bản quy định chi tiết của Chính phủ (như Quyết định của Thủ tướng Chính phủ) được ban hành dựa trên khuyến nghị của Hội đồng tiền lương quốc gia, chứ không thể tìm thấy con số cụ thể trong nội dung của Bộ luật Lao động 2019.

**Lượt tìm:** `mức lương tối thiểu vùng` (filter {'year': 2019}, inferred)

> **[43fdabab0f59a94e]** blld-2019 · Điều 91 · trang [35]
>
> Điều 91. Mức lương tối thiếu 1. Mức lương tối thiểu là mức lương thấp nhất được trả cho người lao động làm công việc giản đơn nhất trong điều kiện lao động bình thường nhằm bảo đảm mức sống tối thiểu của người lao động và gia đình họ, phà hợp với điều kiện phát triển kinh tế - xã hội. 2. Mức lương tối thiểu được xác lập theo vùng, ấn định theo tháng, giờ. 3. Mức lường tối thiểu được điều chỉnh dựa trên mức sống tối thiểu của người lao động và gia đình họ; tương quan giữa mức lương tối thiểu và mức lương trên thị trường; chỉ số giá tiêu dùng, tốc độ tăng trưởng kinh tế; quan hệ cung, cầu lao động: việc làm và thất nghiệp; năng suất lao động; khả năng chỉ trả của doanh nghiệp. 4. Chính phủ quy định chi tiết Điều này; quyết định và công bố mức lương tối thiểu trên cơ sở khuyến nghị của Hội đồng tiền lương quốc gia.

*Nháp AI:* grade= · citation=true · abstention=false · Không từ chối theo quy ước (status answered); khuyên tra 'Quyết định của Thủ tướng' là ý ngoài corpus. Citation Điều 91 đúng với ý 'giao Chính phủ quy định chi tiết và công bố'.

## agent_rerank_hybrid · u02 · status `abstain`

**Câu hỏi:** Người sử dụng lao động phải đóng bảo hiểm xã hội bắt buộc bằng bao nhiêu phần trăm quỹ tiền lương?

**Kỳ vọng:** (thiếu bằng chứng) Bộ luật chỉ quy định nghĩa vụ tham gia/đóng bảo hiểm xã hội theo pháp luật về bảo hiểm xã hội; không có tỷ lệ đóng.

**Agent trả lời:** Các đoạn tìm được trong Bộ luật Lao động 2012 và 2019 không nêu cụ thể tỷ lệ phần trăm người sử dụng lao động phải đóng bảo hiểm xã hội bắt buộc. Thông tin này thường được quy định trong các văn bản hướng dẫn thi hành (như Nghị định, Thông tư) hoặc các văn bản pháp luật chuyên ngành về bảo hiểm xã hội, không nằm trong nội dung của Bộ luật Lao động.

Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời.

**Lượt tìm:** `tỷ lệ đóng bảo hiểm xã hội bắt buộc người sử dụng lao động` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối đúng, không đưa tỷ lệ nào. Có thêm câu 'thường quy định trong Luật BHXH/văn bản hướng dẫn', ý này khớp với dẫn chiếu 'theo pháp luật về BHXH' trong bộ luật. CẦN NGƯỜI DUYỆT (quy tắc: không thêm khẳng định vô căn cứ).

## agent_rerank_hybrid · u03 · status `abstain`

**Câu hỏi:** Người lao động làm việc từ xa tại nhà được hưởng phụ cấp bao nhiêu mỗi tháng?

**Kỳ vọng:** (thiếu bằng chứng) Không bộ luật nào quy định làm việc từ xa hay phụ cấp cho hình thức này.

**Agent trả lời:** Bộ luật Lao động 2019 và 2012 không quy định cụ thể mức phụ cấp cho người lao động làm việc từ xa tại nhà. Các điều luật tìm được chỉ đề cập đến việc người lao động có thể thỏa thuận nhận việc về làm tại nhà, nhưng không nêu rõ về phụ cấp hay mức lương cụ thể cho hình thức này.

Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời.

**Lượt tìm:** `phụ cấp làm việc từ xa tại nhà` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối đúng, không đưa con số phụ cấp. Câu giải thích (nếu có) chỉ nói bộ luật không quy định.

