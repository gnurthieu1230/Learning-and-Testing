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
cd .. = Quay lại thư mục cha (thư mục phía trước)
cd ~ hoặc cd = trở về thư mục Home gốc
mkdir [tên_thư_mục] = Tạo thư mục mớI
rm [tên_file] = Xoá file
rm -rf [tên_thư_mục] = Xoá thư mục và toàn bộ nội dung bên trong
cp [file_nguồn] [file_đích] = Sao chép (copy) file
cp -r [thư_mục_nguồn] [thư_mục_đích] = Sao chép (copy) thư mục
mv [tên_cũ] [tên_mới] = Di chuyển file/thư mục hoặc đổi tên file/thư mục
touch [tên_file] = Tạo một file trống mới
cat [tên_file] = Xem nhanh nội dung của một file văn bản

3. Quản lý Bộ nhớ và Cấp quyền Android
termux-setup-storage = Yêu cầu cấp quyền bộ nhớ điện thoại
df -h = Kiểm tra dung lượng bộ nhớ còn trống trên thiết bị
du -sh = Xem dụng lượng thực tế của một thư mục

4. Mạng và Giám sát Hệ thống
ipconfig hoặc ip a = Xem địa chỉ IP (Wifi/3G/4G/5G) trên điện thoại
ping [domain/IP] = Kiểm tra độ trễ và kết nối đến một trang web
curl [URL] hoặc wget [URL] = Tải dữ liệu hoặc nhận nội dung từ một đường link web
top hoặc htop = Xem tình trạng CPU/RAM và các tiến trình đang chạy theo thời gian thực
netstat hoặc ss = Hiển thị các cổng (port) đang mở và kết nối mạng