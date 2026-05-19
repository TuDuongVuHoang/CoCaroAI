# CaroAI - Minimax và Alpha-Beta Pruning

## 1. Mô tả
Dự án xây dựng chương trình chơi cờ Caro giữa người chơi và máy tính. Máy tính sử dụng thuật toán Minimax hoặc Alpha-Beta pruning để chọn nước đi.

## 2. Luật chơi
- Bàn cờ kích thước 9x9.
- Người chơi là `X`, máy là `O`, ô trống là `.`.
- Hai bên lần lượt đánh vào ô trống.
- Người thắng là người có 4 quân liên tiếp theo hàng ngang, hàng dọc hoặc đường chéo.
- Không xét luật chặn hai đầu.
- Nếu bàn cờ đầy và không ai thắng thì hòa.

## 3. Cách chạy chương trình
Yêu cầu Python 3.10 trở lên.

```bash
cd source_code
python main.py
```

Sau đó chọn:
- `1` để dùng Minimax
- `2` để dùng Alpha-Beta

Nhập nước đi theo dạng:

```bash
row col
```

Ví dụ:

```bash
4 4
```

## 4. Chạy benchmark
```bash
cd source_code
python benchmark.py
```

Chương trình sẽ tạo file:

```text
benchmark_results.csv
```

File này ghi lại:
- trạng thái kiểm thử
- thuật toán
- độ sâu
- nước đi tốt nhất
- điểm đánh giá
- số trạng thái đã xét
- thời gian chạy

## 5. Cấu trúc thư mục
```text
source_code/
├── main.py
├── board.py
├── ai.py
├── evaluation.py
├── benchmark.py
```

## 6. Ghi chú
Chương trình có sinh nước đi ứng viên gần các quân đã đánh để giảm không gian tìm kiếm. Đây là cải tiến hợp lệ vì đề bài cho phép giới hạn danh sách nước đi cần xét.
