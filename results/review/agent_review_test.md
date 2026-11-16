# Phiếu chấm agent · test

Đọc từng câu: so câu trả lời với đáp án/lý do thiếu bằng chứng, rồi mở đoạn được cite (in ngay bên dưới) để xác nhận đoạn đó thực sự chứa khẳng định. Sửa nhãn trong file CSV cùng tên (cột human_*).

## agent_dense_k3 · t01 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2012, hợp đồng lao động xác định thời hạn có thời hạn trong khoảng nào?

**Kỳ vọng:** Từ đủ 12 tháng đến 36 tháng (Điều 22 BLLĐ 2012).

**Agent trả lời:** Theo Bộ luật Lao động 2012, hợp đồng lao động xác định thời hạn là hợp đồng mà trong đó hai bên xác định thời hạn, thời điểm chấm dứt hiệu lực của hợp đồng trong khoảng thời gian từ đủ 12 tháng đến 36 tháng [a30b357d86050788].

**Lượt tìm:** `hợp đồng lao động xác định thời hạn thời hạn` (filter {'year': 2012}, user)

> **[a30b357d86050788]** blld-2012 · Điều 22 · trang [7]
>
> Điều 22. Loại hợp đồng lao động 1. Hợp đồng lao động phải được giao kết theo một trong các loại sau đây: a) Hợp đồng lao động không xác định thời hạn; Hợp đồng lao động không xác định thời hạn là hợp đồng mà trong đó hai bên không xác định thời hạn, thời điểm chấm dứt hiệu lực của hợp đồng. b) Hợp đồng lao động xác định thời hạn; Hợp đồng lao động xác định thời hạn là hợp đồng mà trong đó hai bên xác định thời hạn, thời điểm chấm dứt hiệu lực của hợp đồng trong khoảng thời gian từ đủ 12 tháng đến 36 tháng. c) Hợp đồng lao động theo mùa vụ hoặc theo một công việc nhất định có thời hạn dưới 12 tháng.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · t02 · status `answered`

**Câu hỏi:** Người lao động đang điều trị tai nạn lao động theo chỉ định của cơ sở khám bệnh, chữa bệnh thì người sử dụng lao động có được đơn phương chấm dứt hợp đồng lao động không?

**Kỳ vọng:** Không được (Điều 37 khoản 1 BLLĐ 2019; Điều 39 khoản 1 BLLĐ 2012), trừ trường hợp quy định tại điểm b khoản 1 Điều 36 BLLĐ 2019 (điểm b khoản 1 Điều 38 BLLĐ 2012).

**Agent trả lời:** Không, người sử dụng lao động không được đơn phương chấm dứt hợp đồng lao động khi người lao động đang điều trị tai nạn lao động theo chỉ định của cơ sở khám bệnh, chữa bệnh.

Căn cứ theo Điều 39 của Bộ luật Lao động 2012 [c8f106de608471fe] và Điều 37 của Bộ luật Lao động 2019 [91c524ff95d51f5f], người lao động ốm đau hoặc bị tai nạn lao động, bệnh nghề nghiệp đang điều trị, điều dưỡng theo quyết định/chỉ định của cơ sở khám bệnh, chữa bệnh có thẩm quyền là trường hợp người sử dụng lao động không được thực hiện quyền đơn phương chấm dứt hợp đồng lao động.

**Lượt tìm:** `đơn phương chấm dứt hợp đồng lao động người lao động điều trị tai nạn lao động` (filter None, none)

> **[c8f106de608471fe]** blld-2012 · Điều 39 · trang [13]
>
> Điều 39. Trường hợp người sử dụng lao động không được thực hiện quyền đơn phương chấm dứt hợp đồng lao động 1. Người lao động ốm đau hoặc bị tai nạn lao động, bệnh nghề nghiệp đang điều trị, điều dưỡng theo quyết định của cơ sở khám bệnh, chữa bệnh có thẩm quyền, trừ trường hợp quy định tại điểm b khoản 1 Điều 38 của Bộ luật này. 2. Người lao động đang nghỉ hằng năm, nghỉ việc riêng và những trường hợp nghỉ khác được người sử dụng lao động đồng ý. 3. Lao động nữ quy định tại khoản 3 Điều 155 của Bộ luật này. 4. Người lao động nghỉ việc hưởng chế độ thai sản theo quy định của pháp luật về bảo hiểm xã hội.

> **[91c524ff95d51f5f]** blld-2019 · Điều 37 · trang [16]
>
> Điều 37. Trường hợp người sử dụng lao động không được thực hiện quyên đơn phương chấm dứt hợp đồng lao động 1. Người lao động ốm đau hoặc bị tai nạn, bệnh nghề nghiệp đang điều trị, điều dưỡng theo chỉ định của cơ sở khám bệnh, chữa bệnh có thầm quyên, trừ trường hợp quy định tại điểm b khoản 1 Điều 36 của Bộ luật này. 2. Người lao động đang nghỉ hằng năm, nghỉ việc riêng và trường hợp nghỉ khác được người sử dụng lao động đồng ý. 3. Người lao động nữ mang thai; người lao động đang nghỉ thai sản hoặc nuôi con đưới 12 tháng tuổi.

*Nháp AI:* grade=1 · citation=true;true · abstention= · Kết luận 'không được' đúng và Điều 39/2012, Điều 37/2019 hỗ trợ, nhưng BỎ ngoại lệ 'trừ trường hợp điểm b khoản 1 Điều 38/36' có ngay trong đoạn được cite, nên chỉ đúng một phần. CẦN NGƯỜI DUYỆT (thiếu ngoại lệ là 1 hay 2).

## agent_dense_k3 · t03 · status `answered`

**Câu hỏi:** Người lao động hưởng lương theo tháng được trả lương bao lâu một lần?

**Kỳ vọng:** Một tháng một lần hoặc nửa tháng một lần (Điều 97 BLLĐ 2019; Điều 95 BLLĐ 2012).

**Agent trả lời:** Người lao động hưởng lương theo tháng được trả lương tháng một lần hoặc nửa tháng một lần.

Căn cứ:
- Bộ luật Lao động 2012, Điều 95, Khoản 2 [0bb583836536212c].
- Bộ luật Lao động 2019, Điều 97, Khoản 2 [d9fce9afe9349ceb].

**Lượt tìm:** `người lao động hưởng lương theo tháng được trả lương bao lâu một lần` (filter None, none)

> **[0bb583836536212c]** blld-2012 · Điều 95 · trang [28]
>
> Điều 95. Kỳ hạn trả lương 1. Người lao động hưởng lương giờ, ngày, tuần thì được trả lương sau giờ, ngày, tuần làm việc hoặc được trả gộp do hai bên thoả thuận, nhưng ít nhất 15 ngày phải được trả gộp một lần. 2. Người lao động hưởng lương tháng được trả lương tháng một lần hoặc nửa tháng một lần. 3. Người lao động hưởng lương theo sản phẩm, theo khoán được trả lương theo thoả thuận của hai bên; nếu công việc phải làm trong nhiều tháng thì hằng tháng được tạm ứng tiền lương theo khối lượng công việc đã làm trong tháng.

> **[d9fce9afe9349ceb]** blld-2019 · Điều 97 · trang [37]
>
> Điều 97. Kỳ hạn trả lương 1. Người lao động hướng lương theo giờ, ngày, tuần thì được trả lương sau giờ, ngày, tuần làm việc hoặc được trả gộp do hai bên thỏa thuận nhưng không quá 15 ngày phải được trả gộp một lần. 2. Người lao động hưởng lương theo tháng được trả một tháng một lần hoặc nửa tháng một lần. Thời điểm trả lương do hai bên thỏa thuận và phải được ấn định vào một thời điểm có tính chu kỳ. 3. Người lao động hưởng lương theo sản phẩm, theo khoán được trả lương theo thỏa thuận của hai bên; nêu công việc phải làm trong nhiều tháng thì hằng tháng được tạm ứng tiền lương theo khối lượng công việc đã làm trong tháng. 4. Trường hợp vì lý do bất khả kháng mà người sử dụng lao động đã tìm mọi biện pháp khăc phục nhưng không thể trả lương đúng hạn thì không được chậm quá 30 ngày; nêu trả lương chậm từ 15 ngày trở lên thì người sử "dụng lao động phải đền bù cho người lao "động một khoản

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · t04 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, nếu phải ngừng việc vì sự cố điện, nước không do lỗi của người sử dụng lao động và thời gian ngừng việc từ 14 ngày làm việc trở xuống thì tiền lương ngừng việc được xác định thế nào?

**Kỳ vọng:** Hai bên thỏa thuận tiền lương ngừng việc nhưng không thấp hơn mức lương tối thiểu (Điều 99 khoản 3 điểm a BLLĐ 2019).

**Agent trả lời:** Theo Bộ luật Lao động 2019, nếu phải ngừng việc vì sự cố điện, nước không do lỗi của người sử dụng lao động và thời gian ngừng việc từ 14 ngày làm việc trở xuống, tiền lương ngừng việc được xác định như sau:

- Tiền lương ngừng việc được hai bên thỏa thuận nhưng không thấp hơn mức lương tối thiểu [9f9b5412a3716c83].

**Lượt tìm:** `ngừng việc sự cố điện nước không do lỗi người sử dụng lao động tiền lương` (filter {'year': 2019}, user)

> **[9f9b5412a3716c83]** blld-2019 · Điều 99 · trang [38]
>
> Điều 99. Tiền lương ngừng việc Trường hợp phải ngừng việc, người lao động được trả lương như sau: 1. Nếu do lỗi của người sử dụng lao động thì người lao động được trả đủ tiên lương theo hợp đồng lao động: 2. Nếu do lỗi của người lao động thì người đó không được trả lương: những người lao động khác trong cùng đơn vị phải ngừng việc thì được trả lương theo mức do hai bên thỏa thuận nhưng không được thập hơn mức lương tối thiểu; 3. Nếu vì sự cố về điện, nước mà không do lỗi của người sử dụng lao động hoặc do thiên tại, hỏa hoạn, dịch bệnh nguy hiểm, địch họa, di dời địa điểm hoạt động theo yêu cầu của cơ quan nhà nước có thẩm quyền hoặc vì lý do kinh tế thì hai bên thỏa thuận về tiền lương ngừng việc như sau: a) Trường hợp ngừng việc từ 14 ngày làm việc trở xuống thì tiền lương ngừng việc được thỏa thuận không thấp hơn mức lương tôi thiêu; b) Trường hợp phải ngùng việc trên 14 ngày làm việc

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · t05 · status `abstain`

**Câu hỏi:** Mỗi tuần nhân viên được nghỉ liền một mạch ít nhất bao lâu?

**Kỳ vọng:** Ít nhất 24 giờ liên tục; nếu do chu kỳ lao động không thể nghỉ hằng tuần thì phải được nghỉ bình quân ít nhất 04 ngày trong 01 tháng (Điều 111 BLLĐ 2019; Điều 110 BLLĐ 2012).

**Agent trả lời:** Theo Bộ luật Lao động 2019 và 2012, mỗi tuần người lao động được nghỉ ít nhất 24 giờ liên tục [6049ee563eb186f4 | 866c5c3f06481ce3].

**Lượt tìm:** `nghỉ hàng tuần nghỉ liền một mạch` (filter None, none)

*Nháp AI:* grade=0 · citation= · abstention= · Nội dung ĐÚNG ('ít nhất 24 giờ liên tục') nhưng model cite dạng [id | id]; bộ đọc citation không nhận nên status = abstain (no_citation). Theo BENCHMARK, từ chối câu có đáp án chấm 0. Lỗi định dạng citation phát hiện trên test, xem hậu kiểm.

## agent_dense_k3 · t06 · status `answered`

**Câu hỏi:** Nhân viên lấy vợ hoặc lấy chồng thì được nghỉ mấy ngày mà vẫn hưởng nguyên lương?

**Kỳ vọng:** 03 ngày (nghỉ việc riêng hưởng nguyên lương khi kết hôn; Điều 115 BLLĐ 2019, Điều 116 BLLĐ 2012).

**Agent trả lời:** Theo quy định của Bộ luật Lao động, khi nhân viên kết hôn (lấy vợ hoặc lấy chồng), người lao động được nghỉ việc riêng mà vẫn hưởng nguyên lương trong thời gian **03 ngày**.

Căn cứ:
- Bộ luật Lao động 2012, Điều 116, Khoản 1, điểm a [c0f62e74f8e35ed8].
- Bộ luật Lao động 2019, Điều 115, Khoản 1, điểm a [f8e3497dc661587d].

**Lượt tìm:** `nghỉ lễ cưới vợ chồng hưởng lương` (filter None, none)

> **[c0f62e74f8e35ed8]** blld-2012 · Điều 116 · trang [33]
>
> Điều 116. Nghĩ việc riêng, nghĩ không hưởng lương 1. Người lao động được nghỉ việc riêng mà vẫn hưởng nguyên lương trong những trường hợp sau đây: a) Kết hôn: nghỉ 03 ngày; b) Con kết hôn: nghỉ 01 ngày; mm Bồ đẻ, mẹ đẻ, bố vợ, mẹ vợ hoặc bố chồng, mẹ chồng chết; vợ chết hoặc chông chêt; con chêt: nghỉ 03 ngày. 2. Người lao động được nghỉ không hưởng lương 01] ngày và phải thông báo với người sử dụng lao động khi ông nội, bà nội, ông ngoại, bà ngoại, anh, chị, em ruột chết; bố hoặc mẹ kết hôn; anh, chị, em ruột kết hôn. 3. Ngoài quy định tại khoản Ì và khoản 2 Điều này người lao động có thể thoả thuận với người sử dụng lao động đê nghỉ không hưởng lương.

> **[f8e3497dc661587d]** blld-2019 · Điều 115 · trang [43]
>
> Điều 115. Nghỉ việc riêng, nghỉ không hưởng lương 1. Người lao động được nghỉ việc riêng mà vẫn hưởng nguyên lương và phải thông báo với người sử dụng lao động trong trường hợp sau đây: a) Kết hôn: nghỉ 03 ngày; b) Con đẻ, con nuôi kết hôn: nghỉ 01 ngày; c) Cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi; cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi của vợ hoặc chồng; vợ hoặc chồng: con đẻ, con nuôi chết: nghỉ 03 ngày. 2. Người lao động được nghỉ không hưởng lương 01 ngày và phải thông báo với người sử dụng lao động khi ông nội, bà nội, ông ngoại, bà ngoại, anh, chị, em ruột chết; cha hoặc mẹ kết hôn; anh, chị, em ruột kết hôn. 3. Ngoài quy định tại khoản 1 và khoản 2 Điều này, người lao động có thể thỏa thuận với người sử dụng lao động để nghỉ không hưởng lương. Mục3 THỜI GIỜ LÀM VIỆC, THỜI GIỜ NGHĨ NGƠI ĐÓI VỚI NGƯỜI LÀM CÔNG VIỆC CÓ TÍNH CHẤT ĐẶC BIẾT

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · t07 · status `answered`

**Câu hỏi:** Người lao động chưa đủ 15 tuổi được làm việc tối đa bao nhiêu giờ trong một tuần?

**Kỳ vọng:** Không quá 20 giờ trong 01 tuần (và không quá 04 giờ trong 01 ngày; không được làm thêm giờ, làm việc ban đêm) — Điều 146 BLLĐ 2019; Điều 163 BLLĐ 2012.

**Agent trả lời:** Người lao động chưa đủ 15 tuổi được làm việc tối đa 20 giờ trong một tuần theo quy định tại Điều 146 của Bộ luật Lao động 2019 [47768509d6eee687].

**Lượt tìm:** `người lao động chưa đủ 15 tuổi làm việc tối đa bao nhiêu giờ một tuần` (filter None, none)

> **[47768509d6eee687]** blld-2019 · Điều 146 · trang [53]
>
> Điều 146. Thời giờ làm việc của người chưa thành niên 1. Thời giờ làm việc của người chưa đủ 15 tuổi không được quá 04 giờ trong 01 ngày và 20 giờ trong 01 tuần; không được làm thêm giờ, làm việc vào ban đêm. 2. Thời giờ làm việc của người từ đủ 15 tuổi đến chưa đủ 18 tuổi không được quá 08 giờ trong, 01 ngày và 40 giờ trong 01 tuần. Người từ đủ 15 tuổi đến chưa đủ 18 tuổi có thể được làm thêm giờ, làm việc vào ban đêm trong một số nghề, công việc theo danh mục do Bộ trưởng Bộ Lao động - Thương binh và Xã hội ban hành.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · t08 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, tổ chức đại diện người lao động được tiến hành thủ tục đình công trong những trường hợp nào?

**Kỳ vọng:** Khi là bên tranh chấp lao động tập thể về lợi ích và: (1) hòa giải không thành hoặc hết thời hạn hòa giải (khoản 2 Điều 188) mà hòa giải viên lao động không tiến hành hòa giải; hoặc (2) Ban trọng tài lao động không được thành lập, hoặc thành lập nhưng không ra quyết định, hoặc người sử dụng lao động không thực hiện quyết định của Ban trọng tài (Điều 199).

**Agent trả lời:** Theo Bộ luật Lao động 2019, tổ chức đại diện người lao động được tiến hành thủ tục đình công trong các trường hợp sau:

1. Hòa giải không thành hoặc hết thời hạn hòa giải quy định tại khoản 2 Điều 188 của Bộ luật này mà hòa giải viên lao động không tiến hành hòa giải [25405e0ca17c10c4].
2. Ban trọng tài lao động không được thành lập hoặc thành lập nhưng không ra quyết định giải quyết tranh chấp hoặc người sử dụng lao động là bên tranh chấp không thực hiện quyết định giải quyết tranh chấp của Ban trọng tài lao động [25405e0ca17c10c4].

**Lượt tìm:** `tổ chức đại diện người lao động tiến hành thủ tục đình công` (filter {'year': 2019}, user)

> **[25405e0ca17c10c4]** blld-2019 · Điều 199 · trang [74]
>
> Điều 199. Trường hợp người lao động có quyền đình công Tổ chức đại diện người lao động là bên tranh chấp lao động tập thể về lợi ích có quyên tiên hành thủ tục quy định tại các điều 200, 201 và 202 của Bộ luật này đê đình công trong trường hợp sau đây: mm 1. Hòa giải không thành hoặc hết thời hạn hòa giải quy định tại khoản 2 Điều 188 của Bộ luật này mà hòa giải viên lao động không tiên hành hòa giải; 2. Ban trọng tài lao động không được thành lập hoặc thành lập nhưng không ra quyết định giải quyêt tranh chập hoặc người sử dụng lao động là bên tranh chập không thực hiện quyết định giải quyết tranh châp của Ban trọng tài lao động.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_dense_k3 · t09 · status `answered`

**Câu hỏi:** Lao động nam được nghỉ bao nhiêu ngày khi vợ sinh con?

**Kỳ vọng:** (thiếu bằng chứng) BLLĐ 2019 chỉ dẫn chiếu: lao động nam khi vợ sinh con được nghỉ hưởng chế độ thai sản theo pháp luật về bảo hiểm xã hội; không nêu số ngày.

**Agent trả lời:** Theo Bộ luật Lao động 2019, lao động nam được nghỉ việc hưởng chế độ thai sản khi vợ sinh con [ecf85921ff039e14]. Thời gian nghỉ cụ thể được quy định trong pháp luật về bảo hiểm xã hội.

**Lượt tìm:** `nghỉ việc vợ sinh con nam` (filter None, none)

> **[ecf85921ff039e14]** blld-2019 · Điều 139 · trang [51]
>
> Điều 139. Nghỉ thai sắn 5. Lao động nam khi vợ sinh con, người lao động nhận nuôi con nuôi dưới 06 tháng tuổi, lao động nữ mang thai hộ và người lao động là người mẹ nhờ mang thai hộ được nghỉ việc hưởng chế độ thai sản theo quy định của pháp luật vềbảohiểmxãhội.

*Nháp AI:* grade= · citation=true · abstention=false · Không đưa số ngày, nói rõ thời gian do pháp luật BHXH quy định, tức nội dung đúng là thiếu bằng chứng. Nhưng agent TRẢ LỜI có citation (status answered) thay vì từ chối theo quy ước, nên abstention = false. Citation Điều 139 part 2 (khoản 5) đúng.

## agent_dense_k3 · t10 · status `abstain`

**Câu hỏi:** Trợ cấp thất nghiệp hằng tháng bằng bao nhiêu phần trăm mức lương bình quân đóng bảo hiểm thất nghiệp?

**Kỳ vọng:** (thiếu bằng chứng) Bộ luật chỉ nhắc nghĩa vụ tham gia bảo hiểm thất nghiệp; mức hưởng do Luật Việc làm quy định, không có trong corpus.

**Agent trả lời:** Trợ cấp thất nghiệp (trợ cấp mất việc làm) được tính bằng **01 tháng tiền lương** cho mỗi năm làm việc, nhưng **ít nhất phải bằng 02 tháng tiền lương** [e174576b407acec5 | blld-2012 | năm 2012 | trang 16 | Điều 49], [6f1cd836e77819ef | blld-2019 | năm 2019 | trang 19 | Điều 47].

Tiền lương để tính trợ cấp là **tiền lương bình quân** theo hợp đồng lao động của **06 tháng liền kề** trước khi người lao động mất việc làm [e174576b407acec5 | blld-2012 | năm 2012 | trang 16 | Điều 49], [6f1cd836e77819ef | blld-2019 | năm 2019 | trang 19 | Điều 47].

**Lượt tìm:** `trợ cấp thất nghiệp phần trăm mức lương bình quân` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=false · Status abstain là do lỗi đọc citation dạng [id | blld-2012 | …], không phải agent từ chối. Nội dung trả lời SAI: đồng nhất trợ cấp thất nghiệp với trợ cấp mất việc làm và đưa ra '01 tháng/năm, ít nhất 02 tháng'. Đây là khẳng định vô căn cứ cho câu hỏi này, nên abstention = false.

## agent_dense_k3 · t11 · status `abstain`

**Câu hỏi:** Tiền thưởng Tết tối thiểu mà doanh nghiệp phải trả cho người lao động là bao nhiêu tháng lương?

**Kỳ vọng:** (thiếu bằng chứng) Bộ luật chỉ quy định thưởng do người sử dụng lao động quyết định dựa trên kết quả kinh doanh; không có mức thưởng Tết tối thiểu.

**Agent trả lời:** Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời.

**Lượt tìm:** `tiền thưởng Tết tối thiểu người lao động` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối đúng câu chuẩn, không thêm khẳng định.

## agent_rerank_hybrid · t01 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2012, hợp đồng lao động xác định thời hạn có thời hạn trong khoảng nào?

**Kỳ vọng:** Từ đủ 12 tháng đến 36 tháng (Điều 22 BLLĐ 2012).

**Agent trả lời:** Theo Bộ luật Lao động 2012, hợp đồng lao động xác định thời hạn là hợp đồng mà trong đó hai bên xác định thời hạn, thời điểm chấm dứt hiệu lực của hợp đồng trong khoảng thời gian từ đủ 12 tháng đến 36 tháng [a30b357d86050788].

**Lượt tìm:** `hợp đồng lao động xác định thời hạn thời hạn` (filter {'year': 2012}, user)

> **[a30b357d86050788]** blld-2012 · Điều 22 · trang [7]
>
> Điều 22. Loại hợp đồng lao động 1. Hợp đồng lao động phải được giao kết theo một trong các loại sau đây: a) Hợp đồng lao động không xác định thời hạn; Hợp đồng lao động không xác định thời hạn là hợp đồng mà trong đó hai bên không xác định thời hạn, thời điểm chấm dứt hiệu lực của hợp đồng. b) Hợp đồng lao động xác định thời hạn; Hợp đồng lao động xác định thời hạn là hợp đồng mà trong đó hai bên xác định thời hạn, thời điểm chấm dứt hiệu lực của hợp đồng trong khoảng thời gian từ đủ 12 tháng đến 36 tháng. c) Hợp đồng lao động theo mùa vụ hoặc theo một công việc nhất định có thời hạn dưới 12 tháng.

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · t02 · status `answered`

**Câu hỏi:** Người lao động đang điều trị tai nạn lao động theo chỉ định của cơ sở khám bệnh, chữa bệnh thì người sử dụng lao động có được đơn phương chấm dứt hợp đồng lao động không?

**Kỳ vọng:** Không được (Điều 37 khoản 1 BLLĐ 2019; Điều 39 khoản 1 BLLĐ 2012), trừ trường hợp quy định tại điểm b khoản 1 Điều 36 BLLĐ 2019 (điểm b khoản 1 Điều 38 BLLĐ 2012).

**Agent trả lời:** Không, người sử dụng lao động không được đơn phương chấm dứt hợp đồng lao động khi người lao động đang điều trị tai nạn lao động theo chỉ định của cơ sở khám bệnh, chữa bệnh.

Căn cứ Điều 38 Bộ luật Lao động 2012 [f80dacb818c11417] và Điều 36 Bộ luật Lao động 2019 [9b7f39c87c08fb5c], người sử dụng lao động chỉ được đơn phương chấm dứt hợp đồng lao động khi người lao động bị ốm đau, tai nạn đã điều trị 12 tháng liên tục (với hợp đồng không xác định thời hạn) hoặc 06 tháng liên tục (với hợp đồng xác định thời hạn) mà khả năng lao động chưa hồi phục. Trong thời gian người lao động đang điều trị theo chỉ định của cơ sở y tế, chưa đạt đến thời hạn điều trị quy định nêu trên, người sử dụng lao động không có quyền đơn phương chấm dứt hợp đồng lao động.

**Lượt tìm:** `đơn phương chấm dứt hợp đồng lao động người lao động điều trị tai nạn lao động` (filter None, none)

> **[f80dacb818c11417]** blld-2012 · Điều 38 · trang [12, 13]
>
> Điều 38. Quyền đơn phương chấm dứt hợp đồng lao động của người sử dụng lao động 1. Người sử dụng lao động có quyền đơn phương chấm dứt hợp đồng lao động trong những trường hợp sau đây: a) Người lao động thường xuyên không hoàn thành công việc theo hợp đồng lao động; b) Người lao động bị ốm đau, tai nạn đã điều trị 12 tháng liên tục đối với người làm theo hợp đồng lao động không xác định thời hạn, đã điều trị 06 tháng liên tục, đối với người lao động làm theo hợp đồng lao động xác định thời hạn và quá nửa thời hạn hợp đồng lao động đối với người làm theo hợp đồng lao động theo mùa vụ hoặc theo một công việc nhất định có thời hạn dưới 12 tháng mà khả năng lao động chưa hồi phục. Khi sức khỏe của người lao động bình phục, thì người lao động được xem xét để tiếp tục giao kết hợp đồng lao động: c) Do thiên tai, hỏa hoạn hoặc những lý do bất khả kháng khác theo quy định của pháp luật, mà người

> **[9b7f39c87c08fb5c]** blld-2019 · Điều 36 · trang [15]
>
> Điều 36. Quyền đơn phương chấm dứt hợp đồng lao. động của người: sử dụng lao động 1. Người sử dụng lao động có quyền đơn phương chấm dứt hợp đồng lao động trong trường hợp sau đây: a) Người lao động thường xuyên không hoàn thành công việc theo hợp đồng lao động được xác định theo tiêu chí đánh giá mức độ hoàn thành công việc trong quy chế của người sử dụng lao động. Quy chế đánh giá mức độ hoàn thành công việc do người sử dụng lao động ban hành nhưng phải tham khảo ý kiến tổ chức đại diện người lao động tại cơ sở đối với nơi có tổ chức đại diện người lao động tại cơ SỞ; b) Người lao động bị ô ốm đau, tai nạn đã điều trị 12 tháng liên tục đối với người làm việc theo hợp đồng lao động không xác định thời hạn hoặc đã điều trị 06 tháng liên tục đối với người làm việc theo hợp đồng lao động xác định thời hạn có thời hạn từ 12 tháng đến 36 tháng hoặc quá nửa thời hạn hợp. đồng lao động đối với

*Nháp AI:* grade=1 · citation=true;true · abstention= · Kết luận 'không được' đúng, có giải thích ngoại lệ 12/06 tháng (đúng nội dung điểm b khoản 1 Điều 38/2012, 36/2019). Nhưng khẳng định 'NSDLĐ CHỈ được đơn phương chấm dứt khi…' là sai (Điều 36 còn các căn cứ khác), và context thiếu Điều 37 (final_context_has_evidence=false). Citation đúng với phần nội dung 12/06 tháng. CẦN NGƯỜI DUYỆT.

## agent_rerank_hybrid · t03 · status `answered`

**Câu hỏi:** Người lao động hưởng lương theo tháng được trả lương bao lâu một lần?

**Kỳ vọng:** Một tháng một lần hoặc nửa tháng một lần (Điều 97 BLLĐ 2019; Điều 95 BLLĐ 2012).

**Agent trả lời:** Người lao động hưởng lương theo tháng được trả lương một tháng một lần hoặc nửa tháng một lần. Thời điểm trả lương do hai bên thỏa thuận và phải được ấn định vào một thời điểm có tính chu kỳ.

Căn cứ:
- Bộ luật Lao động 2019, Điều 97, Khoản 2 [d9fce9afe9349ceb]
- Bộ luật Lao động 2012, Điều 95, Khoản 2 [0bb583836536212c]

**Lượt tìm:** `người lao động hưởng lương theo tháng được trả lương bao lâu một lần` (filter None, none)

> **[d9fce9afe9349ceb]** blld-2019 · Điều 97 · trang [37]
>
> Điều 97. Kỳ hạn trả lương 1. Người lao động hướng lương theo giờ, ngày, tuần thì được trả lương sau giờ, ngày, tuần làm việc hoặc được trả gộp do hai bên thỏa thuận nhưng không quá 15 ngày phải được trả gộp một lần. 2. Người lao động hưởng lương theo tháng được trả một tháng một lần hoặc nửa tháng một lần. Thời điểm trả lương do hai bên thỏa thuận và phải được ấn định vào một thời điểm có tính chu kỳ. 3. Người lao động hưởng lương theo sản phẩm, theo khoán được trả lương theo thỏa thuận của hai bên; nêu công việc phải làm trong nhiều tháng thì hằng tháng được tạm ứng tiền lương theo khối lượng công việc đã làm trong tháng. 4. Trường hợp vì lý do bất khả kháng mà người sử dụng lao động đã tìm mọi biện pháp khăc phục nhưng không thể trả lương đúng hạn thì không được chậm quá 30 ngày; nêu trả lương chậm từ 15 ngày trở lên thì người sử "dụng lao động phải đền bù cho người lao "động một khoản

> **[0bb583836536212c]** blld-2012 · Điều 95 · trang [28]
>
> Điều 95. Kỳ hạn trả lương 1. Người lao động hưởng lương giờ, ngày, tuần thì được trả lương sau giờ, ngày, tuần làm việc hoặc được trả gộp do hai bên thoả thuận, nhưng ít nhất 15 ngày phải được trả gộp một lần. 2. Người lao động hưởng lương tháng được trả lương tháng một lần hoặc nửa tháng một lần. 3. Người lao động hưởng lương theo sản phẩm, theo khoán được trả lương theo thoả thuận của hai bên; nếu công việc phải làm trong nhiều tháng thì hằng tháng được tạm ứng tiền lương theo khối lượng công việc đã làm trong tháng.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · t04 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, nếu phải ngừng việc vì sự cố điện, nước không do lỗi của người sử dụng lao động và thời gian ngừng việc từ 14 ngày làm việc trở xuống thì tiền lương ngừng việc được xác định thế nào?

**Kỳ vọng:** Hai bên thỏa thuận tiền lương ngừng việc nhưng không thấp hơn mức lương tối thiểu (Điều 99 khoản 3 điểm a BLLĐ 2019).

**Agent trả lời:** Theo Bộ luật Lao động 2019, nếu phải ngừng việc vì sự cố điện, nước không do lỗi của người sử dụng lao động và thời gian ngừng việc từ 14 ngày làm việc trở xuống, thì tiền lương ngừng việc được xác định như sau:

- Hai bên (người lao động và người sử dụng lao động) thỏa thuận về tiền lương ngừng việc.
- Mức tiền lương ngừng việc được thỏa thuận không thấp hơn mức lương tối thiểu [9f9b5412a3716c83].

**Lượt tìm:** `ngừng việc sự cố điện nước không do lỗi người sử dụng lao động tiền lương` (filter {'year': 2019}, user)

> **[9f9b5412a3716c83]** blld-2019 · Điều 99 · trang [38]
>
> Điều 99. Tiền lương ngừng việc Trường hợp phải ngừng việc, người lao động được trả lương như sau: 1. Nếu do lỗi của người sử dụng lao động thì người lao động được trả đủ tiên lương theo hợp đồng lao động: 2. Nếu do lỗi của người lao động thì người đó không được trả lương: những người lao động khác trong cùng đơn vị phải ngừng việc thì được trả lương theo mức do hai bên thỏa thuận nhưng không được thập hơn mức lương tối thiểu; 3. Nếu vì sự cố về điện, nước mà không do lỗi của người sử dụng lao động hoặc do thiên tại, hỏa hoạn, dịch bệnh nguy hiểm, địch họa, di dời địa điểm hoạt động theo yêu cầu của cơ quan nhà nước có thẩm quyền hoặc vì lý do kinh tế thì hai bên thỏa thuận về tiền lương ngừng việc như sau: a) Trường hợp ngừng việc từ 14 ngày làm việc trở xuống thì tiền lương ngừng việc được thỏa thuận không thấp hơn mức lương tôi thiêu; b) Trường hợp phải ngùng việc trên 14 ngày làm việc

*Nháp AI:* grade=2 · citation=true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · t05 · status `abstain`

**Câu hỏi:** Mỗi tuần nhân viên được nghỉ liền một mạch ít nhất bao lâu?

**Kỳ vọng:** Ít nhất 24 giờ liên tục; nếu do chu kỳ lao động không thể nghỉ hằng tuần thì phải được nghỉ bình quân ít nhất 04 ngày trong 01 tháng (Điều 111 BLLĐ 2019; Điều 110 BLLĐ 2012).

**Agent trả lời:** Theo Bộ luật Lao động 2012 và 2019, mỗi tuần người lao động được nghỉ ít nhất 24 giờ liên tục [866c5c3f06481ce3 | 6049ee563eb186f4].

**Lượt tìm:** `nghỉ hàng tuần nghỉ liền một mạch` (filter None, none)

*Nháp AI:* grade=0 · citation= · abstention= · Giống agent_dense_k3: nội dung đúng nhưng cite [id | id] nên bị chuyển thành từ chối; chấm 0.

## agent_rerank_hybrid · t06 · status `answered`

**Câu hỏi:** Nhân viên lấy vợ hoặc lấy chồng thì được nghỉ mấy ngày mà vẫn hưởng nguyên lương?

**Kỳ vọng:** 03 ngày (nghỉ việc riêng hưởng nguyên lương khi kết hôn; Điều 115 BLLĐ 2019, Điều 116 BLLĐ 2012).

**Agent trả lời:** Theo Bộ luật Lao động 2012 và 2019, người lao động được nghỉ việc riêng mà vẫn hưởng nguyên lương khi kết hôn (lấy vợ hoặc lấy chồng) là **03 ngày**.

Căn cứ:
- [c0f62e74f8e35ed8] Điều 116, khoản 1, điểm a) Bộ luật Lao động 2012.
- [f8e3497dc661587d] Điều 115, khoản 1, điểm a) Bộ luật Lao động 2019.

**Lượt tìm:** `nghỉ lễ cưới vợ chồng hưởng lương` (filter None, none)

> **[c0f62e74f8e35ed8]** blld-2012 · Điều 116 · trang [33]
>
> Điều 116. Nghĩ việc riêng, nghĩ không hưởng lương 1. Người lao động được nghỉ việc riêng mà vẫn hưởng nguyên lương trong những trường hợp sau đây: a) Kết hôn: nghỉ 03 ngày; b) Con kết hôn: nghỉ 01 ngày; mm Bồ đẻ, mẹ đẻ, bố vợ, mẹ vợ hoặc bố chồng, mẹ chồng chết; vợ chết hoặc chông chêt; con chêt: nghỉ 03 ngày. 2. Người lao động được nghỉ không hưởng lương 01] ngày và phải thông báo với người sử dụng lao động khi ông nội, bà nội, ông ngoại, bà ngoại, anh, chị, em ruột chết; bố hoặc mẹ kết hôn; anh, chị, em ruột kết hôn. 3. Ngoài quy định tại khoản Ì và khoản 2 Điều này người lao động có thể thoả thuận với người sử dụng lao động đê nghỉ không hưởng lương.

> **[f8e3497dc661587d]** blld-2019 · Điều 115 · trang [43]
>
> Điều 115. Nghỉ việc riêng, nghỉ không hưởng lương 1. Người lao động được nghỉ việc riêng mà vẫn hưởng nguyên lương và phải thông báo với người sử dụng lao động trong trường hợp sau đây: a) Kết hôn: nghỉ 03 ngày; b) Con đẻ, con nuôi kết hôn: nghỉ 01 ngày; c) Cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi; cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi của vợ hoặc chồng; vợ hoặc chồng: con đẻ, con nuôi chết: nghỉ 03 ngày. 2. Người lao động được nghỉ không hưởng lương 01 ngày và phải thông báo với người sử dụng lao động khi ông nội, bà nội, ông ngoại, bà ngoại, anh, chị, em ruột chết; cha hoặc mẹ kết hôn; anh, chị, em ruột kết hôn. 3. Ngoài quy định tại khoản 1 và khoản 2 Điều này, người lao động có thể thỏa thuận với người sử dụng lao động để nghỉ không hưởng lương. Mục3 THỜI GIỜ LÀM VIỆC, THỜI GIỜ NGHĨ NGƠI ĐÓI VỚI NGƯỜI LÀM CÔNG VIỆC CÓ TÍNH CHẤT ĐẶC BIẾT

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · t07 · status `answered`

**Câu hỏi:** Người lao động chưa đủ 15 tuổi được làm việc tối đa bao nhiêu giờ trong một tuần?

**Kỳ vọng:** Không quá 20 giờ trong 01 tuần (và không quá 04 giờ trong 01 ngày; không được làm thêm giờ, làm việc ban đêm) — Điều 146 BLLĐ 2019; Điều 163 BLLĐ 2012.

**Agent trả lời:** Người lao động chưa đủ 15 tuổi được làm việc tối đa 20 giờ trong một tuần.

Căn cứ:
- Bộ luật Lao động 2019, Điều 146, Khoản 1: "Thời giờ làm việc của người chưa đủ 15 tuổi không được quá 04 giờ trong 01 ngày và 20 giờ trong 01 tuần" [47768509d6eee687].
- Bộ luật Lao động 2012, Điều 163, Khoản 2: "Thời giờ làm việc của người dưới 15 tuổi không được quá 04 giờ trong 01 ngày và 20 giờ trong 01 tuần" [6f2bf56158b071b3].

**Lượt tìm:** `người lao động chưa đủ 15 tuổi làm việc tối đa bao nhiêu giờ một tuần` (filter None, none)

> **[47768509d6eee687]** blld-2019 · Điều 146 · trang [53]
>
> Điều 146. Thời giờ làm việc của người chưa thành niên 1. Thời giờ làm việc của người chưa đủ 15 tuổi không được quá 04 giờ trong 01 ngày và 20 giờ trong 01 tuần; không được làm thêm giờ, làm việc vào ban đêm. 2. Thời giờ làm việc của người từ đủ 15 tuổi đến chưa đủ 18 tuổi không được quá 08 giờ trong, 01 ngày và 40 giờ trong 01 tuần. Người từ đủ 15 tuổi đến chưa đủ 18 tuổi có thể được làm thêm giờ, làm việc vào ban đêm trong một số nghề, công việc theo danh mục do Bộ trưởng Bộ Lao động - Thương binh và Xã hội ban hành.

> **[6f2bf56158b071b3]** blld-2012 · Điều 163 · trang [45, 46]
>
> Điều 163. Nguyên tắc sử dụng lao động là người chưa thành niên 1. Không được sử dụng lao động chưa thành niên làm những công việc nặng nhọc, độc hại, nguy hiểm hoặc chỗ làm việc, công việc ảnh hưởng xâu tới nhân cách của họ theo danh mục do Bộ Lao động - Thương binh và Xã hội chủ trì phối hợp với Bộ Y tế ban hành. 2. Thời giờ làm việc của người lao động chưa thành niên từ đủ 15 tuổi đến dưới 18 tuôi không được quá 08 giờ trong 01 ngày và 40 giờ trong 01 tuân. Thời giờ làm việc của người dưới 15 tuổi không được quá 04 giờ trong 01 ngày và 20 giờ trong 01 tuân và không được sử dụng làm thêm giờ, làm việc vào ban đêm. 3. Người từ đủ 15 tuổi đến dưới 18 tuổi được làm thêm giờ, làm việc vào ban đêm trong một sô nghê và công việc theo quy định của Bộ Lao động - Thương binh và Xã hội. 4. Không được sử dụng người chưa thành niên sản xuất và kinh doanh cồn, rượu, bia, thuôc lá, chât tác động đên 

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó.

## agent_rerank_hybrid · t08 · status `answered`

**Câu hỏi:** Theo Bộ luật Lao động 2019, tổ chức đại diện người lao động được tiến hành thủ tục đình công trong những trường hợp nào?

**Kỳ vọng:** Khi là bên tranh chấp lao động tập thể về lợi ích và: (1) hòa giải không thành hoặc hết thời hạn hòa giải (khoản 2 Điều 188) mà hòa giải viên lao động không tiến hành hòa giải; hoặc (2) Ban trọng tài lao động không được thành lập, hoặc thành lập nhưng không ra quyết định, hoặc người sử dụng lao động không thực hiện quyết định của Ban trọng tài (Điều 199).

**Agent trả lời:** Theo Bộ luật Lao động 2019, tổ chức đại diện người lao động được tiến hành thủ tục đình công trong các trường hợp sau:

1. Hòa giải không thành hoặc hết thời hạn hòa giải quy định tại khoản 2 Điều 188 của Bộ luật này mà hòa giải viên lao động không tiến hành hòa giải [25405e0ca17c10c4].
2. Ban trọng tài lao động không được thành lập hoặc thành lập nhưng không ra quyết định giải quyết tranh chấp hoặc người sử dụng lao động là bên tranh chấp không thực hiện quyết định giải quyết tranh chấp của Ban trọng tài lao động [25405e0ca17c10c4].

Tuy nhiên, tổ chức đại diện người lao động không được tiến hành đình công trong thời gian Hội đồng trọng tài lao động đang tiến hành giải quyết tranh chấp [0ad185c46a15a18a].

**Lượt tìm:** `tổ chức đại diện người lao động tiến hành thủ tục đình công` (filter {'year': 2019}, user)

> **[25405e0ca17c10c4]** blld-2019 · Điều 199 · trang [74]
>
> Điều 199. Trường hợp người lao động có quyền đình công Tổ chức đại diện người lao động là bên tranh chấp lao động tập thể về lợi ích có quyên tiên hành thủ tục quy định tại các điều 200, 201 và 202 của Bộ luật này đê đình công trong trường hợp sau đây: mm 1. Hòa giải không thành hoặc hết thời hạn hòa giải quy định tại khoản 2 Điều 188 của Bộ luật này mà hòa giải viên lao động không tiên hành hòa giải; 2. Ban trọng tài lao động không được thành lập hoặc thành lập nhưng không ra quyết định giải quyêt tranh chập hoặc người sử dụng lao động là bên tranh chập không thực hiện quyết định giải quyết tranh châp của Ban trọng tài lao động.

> **[0ad185c46a15a18a]** blld-2019 · Điều 197 · trang [74]
>
> Điều 197. Giải quyết tranh chấp lao động tập thể về lợi ích của Hội đồng trọng tài lao động 4. Khi các bên lựa chọn giải quyết tranh chấp thông qua Hội đồng trọng tài lao động theo quy định tại Điều này thì tổ chức đại diện người lao động không được tiên hành đình công trong thời gian Hội đồng trọng tài lao động đang tiên hành giải quyết tranh chấp. Khi hết thời hạn quy định tại khoản 2 Điều này mà Ban trọng tài lao động không được thành lập hoặc hết thời hạn quy định tại khoản 3 Điều này mà Ban trọng tài không ra quyết định giải quyết tranh chấp hoặc người sử dụng lao động là bên tranh chấp không thực hiện quyết định giải quyết tranh chấp của Ban trọng tài lao động thì tổ chức đại diện người lao động là bên tranh chấp có quyền tiến hành thủ tục quy định tại các điều 200, 201 và 202 của Bộ luật này để đình công.

*Nháp AI:* grade=2 · citation=true;true · abstention= · Đủ cả hai trường hợp của Điều 199. Ý thêm 'không được đình công trong thời gian Hội đồng trọng tài đang giải quyết' đúng với khoản 4 Điều 197 được cite.

## agent_rerank_hybrid · t09 · status `answered`

**Câu hỏi:** Lao động nam được nghỉ bao nhiêu ngày khi vợ sinh con?

**Kỳ vọng:** (thiếu bằng chứng) BLLĐ 2019 chỉ dẫn chiếu: lao động nam khi vợ sinh con được nghỉ hưởng chế độ thai sản theo pháp luật về bảo hiểm xã hội; không nêu số ngày.

**Agent trả lời:** Theo Bộ luật Lao động 2019, lao động nam được nghỉ việc hưởng chế độ thai sản khi vợ sinh con theo quy định của pháp luật về bảo hiểm xã hội [ecf85921ff039e14].

Theo Bộ luật Lao động 2012, lao động nam cũng được nghỉ việc hưởng chế độ thai sản khi vợ sinh con theo quy định của pháp luật về bảo hiểm xã hội [7f0b75caccf16928].

Để biết chính xác số ngày nghỉ, bạn cần tham khảo quy định của pháp luật về bảo hiểm xã hội hiện hành.

**Lượt tìm:** `nghỉ việc vợ sinh con nam` (filter None, none)

> **[ecf85921ff039e14]** blld-2019 · Điều 139 · trang [51]
>
> Điều 139. Nghỉ thai sắn 5. Lao động nam khi vợ sinh con, người lao động nhận nuôi con nuôi dưới 06 tháng tuổi, lao động nữ mang thai hộ và người lao động là người mẹ nhờ mang thai hộ được nghỉ việc hưởng chế độ thai sản theo quy định của pháp luật vềbảohiểmxãhội.

> **[7f0b75caccf16928]** blld-2012 · Điều 157 · trang [44, 45]
>
> Điều 157. Nghỉ thai sản 1. Lao động nữ được nghỉ trước và sau khi sinh con là 06 tháng. Trường hợp lao động nữ sinh đôi trở lên thì tính từ con thứ 02 trở đi, cứ mỗi con, người mẹ được nghỉ thêm 01 tháng. Thời gian nghỉ trước khi sinh tối đa không quá 02 tháng. 2. Trong thời gian nghỉ thai sản, lao động nữ được hưởng chế độ thai sản theo quy định của pháp luật về bảo hiểm xã hội. 3. Hết thời gian nghỉ thai sản theo quy định tại khoản 1 Điều này, nếu có nhu cầu, lao động nữ có thể nghỉ thêm một thời gian không hưởng lương theo thoả thuận với người sử dụng lao động. 4. Trước khi hết thời gian nghỉ thai sản theo quy định tại khoản 1] Điều này, nếu có nhu cầu, có xác nhận của cơ sở khám bệnh, chữa bệnh có thẩm quyền về việc đi làm sớm không có hại cho sức khỏe của người lao động và được người sử dụng lao động đồng ý, lao động nữ có thể trở lại làm việc khi đã nghỉ ít nhât được 04 tháng. Tron

*Nháp AI:* grade= · citation=true;false · abstention=false · Không đưa số ngày nhưng status answered, nên abstention = false. Citation Điều 157/2012 part 1 chỉ nói về lao động NỮ, không hỗ trợ ý 'lao động nam cũng được nghỉ khi vợ sinh con', nên false.

## agent_rerank_hybrid · t10 · status `answered`

**Câu hỏi:** Trợ cấp thất nghiệp hằng tháng bằng bao nhiêu phần trăm mức lương bình quân đóng bảo hiểm thất nghiệp?

**Kỳ vọng:** (thiếu bằng chứng) Bộ luật chỉ nhắc nghĩa vụ tham gia bảo hiểm thất nghiệp; mức hưởng do Luật Việc làm quy định, không có trong corpus.

**Agent trả lời:** Trợ cấp thất nghiệp (trợ cấp mất việc làm) được tính dựa trên mức lương bình quân đóng bảo hiểm thất nghiệp, không phải là một phần trăm cố định của mức lương bình quân đóng bảo hiểm thất nghiệp.

Theo Điều 47 của Bộ luật Lao động 2019 [6f1cd836e77819ef], trợ cấp mất việc làm được tính bằng tiền lương bình quân của 06 tháng liền kề theo hợp đồng lao động trước khi người lao động mất việc làm.

Tuy nhiên, mức lương bình quân để tính trợ cấp mất việc làm là tiền lương bình quân của 06 tháng liền kề theo hợp đồng lao động trước khi người lao động mất việc làm, không phải là mức lương bình quân đóng bảo hiểm thất nghiệp.

Nếu bạn muốn biết mức lương bình quân đóng bảo hiểm thất nghiệp, đây là một khái niệm khác, liên quan đến mức đóng bảo hiểm thất nghiệp, không phải là trợ cấp mất việc làm.

Vì vậy, trợ cấp thất nghiệp không được tính bằng một phần trăm mức lương bình quân đóng bảo hiểm thất nghiệp, mà được tính bằng tiền lương bình quân của 06 tháng liền kề theo hợp đồng lao động trước khi người lao động mất việc làm.

**Lượt tìm:** `trợ cấp thất nghiệp phần trăm mức lương bình quân` (filter None, none)

> **[6f1cd836e77819ef]** blld-2019 · Điều 47 · trang [19]
>
> Điều 47. Trợ cấp mất việc làm 1. Người sử dụng lao động trả trợ cấp mất việc làm cho người lao động đã làm việc thường xuyên cho mình từ đủ 12 tháng trở lên mà bị mất việc làm theo. quy định tại khoản 11 Điều 34 của Bộ luật này, cứ mỗi năm làm việc trả 01 tháng tiền lương nhưng ít nhất bằng 02 tháng tiền lương. 2. Thời gian làm việc đề tính trợ cấp mắt việc làm là tổng thời gian người lao động đã làm việc thực tế cho người sử dụng lao động trừ đi thời gian người lao động đã tham gia bảo hiểm thất nghiệp theo quy định của pháp luật vê bảo hiểm thất nghiệp và thời gian làm việc đã được người sử dụng lao động chỉ trả trợ cấp thôi việc, trợ cấp mắt việc làm. 3. Tiền lương để tính trợ cấp mất việc làm là tiền lương bình quân của 06 tháng liền kề theo hợp đồng lao động trước khi người lao động mất việc làm. 4. Chính phủ quy định chỉ tiết Điều này.

*Nháp AI:* grade= · citation=true · abstention=false · Trả lời (status answered), đồng nhất trợ cấp thất nghiệp với trợ cấp mất việc làm (Điều 47), nên abstention = false. Citation Điều 47 đúng với ý 'tiền lương bình quân 06 tháng liền kề' của trợ cấp mất việc làm.

## agent_rerank_hybrid · t11 · status `abstain`

**Câu hỏi:** Tiền thưởng Tết tối thiểu mà doanh nghiệp phải trả cho người lao động là bao nhiêu tháng lương?

**Kỳ vọng:** (thiếu bằng chứng) Bộ luật chỉ quy định thưởng do người sử dụng lao động quyết định dựa trên kết quả kinh doanh; không có mức thưởng Tết tối thiểu.

**Agent trả lời:** Theo Bộ luật Lao động 2019 và 2012, không có quy định cụ thể về mức tiền thưởng Tết tối thiểu phải trả cho người lao động tính bằng số tháng lương.

- **Bộ luật Lao động 2019, Điều 98** quy định về tiền lương làm thêm giờ, làm việc vào ban đêm và ngày nghỉ lễ, Tết, nhưng không đề cập đến tiền thưởng Tết.
- **Bộ luật Lao động 2012, Điều 103** quy định tiền thưởng là khoản tiền thưởng cho người lao động căn cứ vào kết quả sản xuất kinh doanh hằng năm và mức độ hoàn thành công việc, do người sử dụng lao động quyết định.
- **Bộ luật Lao động 2012, Điều 113** quy định về tạm ứng tiền lương khi nghỉ hằng năm, không phải tiền thưởng Tết.

Do đó, không có quy định bắt buộc về mức tiền thưởng Tết tối thiểu bằng số tháng lương trong Bộ luật Lao động.

**Lượt tìm:** `tiền thưởng Tết tối thiểu người lao động` (filter None, none)

*Nháp AI:* grade= · citation= · abstention=true · Từ chối theo nội dung ('không có quy định… tối thiểu'), không đưa con số. Status abstain do không cite. Các mô tả Điều 98/2019, Điều 103 và Điều 113/2012 đúng với văn bản. CẦN NGƯỜI DUYỆT xem phần giải thích có bị coi là khẳng định thêm không.

