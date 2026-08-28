=== BIẾN VÀ HÀM TRONG FLUTTER ===

1. BIẾN:
- State Variable : Biến lưu dữ liệu thay đổi trên UI (_counter)
- Final Property : Biến nhận dữ liệu truyền vào Widget (final String title)
- Controller     : Biến điều khiển nhập liệu (TextEditingController)

2. HÀM:
- build()     : Hàm trả về giao diện Widget (chạy khi dựng UI)
- setState()  : Hàm thông báo cập nhật biến State để vẽ lại màn hình
- initState() : Hàm khởi tạo (chạy 1 lần khi mở màn hình)
- dispose()   : Hàm dọn dẹp bộ nhớ (chạy khi đóng màn hình)
- onPressed   : Hàm sự kiện bắt cú bấm của người dùng
