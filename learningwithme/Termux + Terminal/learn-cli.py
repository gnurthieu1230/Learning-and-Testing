### Tất cả các lệnh trong Termux (Android), Terminal (Windows, Linux, MacOS), Powershell (Windows)

=> Termux
1. Quản lý gói phần mềm (APT / PKG)
pkg update && pkg upgrade = Cập nhật và nâng cấp toàn bộ gói cài đặt
pkg install [tên_gói] = Cài đặt một phần mềm mới
pkg uninstall [tên_gói] = gỡ cài đặt một gói phần mềm 
pkg search [tên_gói] = Tìm kiếm xem có phần mềm nào trên termux không
pkg list-installed = Hiện thị danh sách các gói đã cài đặt

2. Thao tác với Tệp và Thư mục (File & Directory)
pwd = Hiện thị đường dẫn thư mục đang đứng
ls = liệt kê các thư mục/file hiện tại
ls -a = Liệt kê tất cả file (bao gồm cả file ẩn có dấu "." ở đầu)
ls -l = Hiển thị danh sách kèm thông tin chỉ tiết (dung lượng, quyền, ngày tạo)
cd [đường_dẫn] = Di chuyển đến thư mục cần mở