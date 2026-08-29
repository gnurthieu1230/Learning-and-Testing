### Tất cả các lệnh trong Termux (Android), Terminal (Windows, Linux, MacOS), Powershell (Windows)
---------------------------------------
    THUẬT NGỮ TRONG NETWORK VÀ CLI
          ------------------
1. WAN = Wide Area Network
2. LAN = Local Area Network
3. TCP = Transmission Control Protocol
4. UDP = User Datagram Protocol
5. IP = Internet Protocol
6. UPnP = Universal Plug and Play
7. NAT = Network Address Translation
8. CGNAT = Carrier-Grade NAT
9. IPv4 = Internet Protocol version 4
10. IPv6 = Internet Protocol version 6
11. DNS = Domain Name Server
12. BSSID = Basic Service Set Identifier
13. SSID = Service Set Identifier
14. RSSI = 
15. VPN = Virtual Private Network
16. APN = Access Point Name
---------------------------------------

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

4. Mạng và Giám sát Hệ thống,toàn bộ mạng
ipconfig hoặc ip a = Xem địa chỉ IP (Wifi/3G/4G/5G) trên điện thoại
ping [domain/IP] = Kiểm tra độ trễ và kết nối đến một trang web
curl [URL] hoặc wget [URL] = Tải dữ liệu hoặc nhận nội dung từ một đường link web
top hoặc htop = Xem tình trạng CPU/RAM và các tiến trình đang chạy theo thời gian thực
netstat hoặc ss = Hiển thị các cổng (port) đang mở và kết nối mạng
nmap [IP/Domain] = Công cụ dò quét cổng và dịch vụ
nmap -sV [IP] = Quét các cổng đang mở và phát hiện các phiên bản dịch vụ đang chạy
nmap -O [IP] = Đoán hệ điều hành của máy đích
nc hoặc ncat = ...
nc -zv [IP] [Port] = Kiểm tra nhanh xem có một cổng cụ thể nào đang mở hay không
nc -lvp [Port] = Mở một cổng trên máy mình để lắng nghe kết nối đến
traceroute [Domain/IP] = Hiện thị đường đi gói tin từ máy mình sang máy đích qua từng router
MTR [Domain/IP] = Kết hợp giữa ping và traceroute, cập nhật liên tục độ trễ và tỉ lệ mất gói tin theo thời gian thực
route hoặc ip route = Xem và quản lý bảng định tuyến (Route Table) trên thiết bị
arp -a hoặc ip neighbor = Xem danh sách các thiết bị (Địa chỉ IP và Địa chỉ MAC) đang nằm chung mạng Wifi/LAN

5. Tra cứu DNS & Thông tin tên miền
dig [Domain] = Tra cứu chi tiết các bản ghi DNS (A, CNAME,MX,TXT,...)
dig [Domain] ANY = Lấy tất cả thông tin DNS có sẵn
nslookup [Domain] = Công cụ hỏi đáp máy chủ DNS nhanh gọn
whois [Domain] = Tra cứu thông tin chủ sở hữu tên miền, ngày đăng ký, ngày hết hạn và nhà cung cấp

6. Bắt & Phân tích gói tin (Packet Sniffing)
tcpdump = công cụ bắt gói tin trên dòng lệnh
tcpdump -i any = Bắt toàn bộ dữ liệu qua tất cả các card mạng
tcpdump port 80 = Chỉ bắt các dữ liệu đi qua cổng web HTTP (Port 80)
tshark = Trình phân tích gói tin trên dòng lệnh của Wireshark

7. Quản lý tải & Đổi quyền kết nối
aria2c [URL] / aria2c -x16 [URL] = Bộ tải file đa luồng cực nhanh (nhanh hơn curl và wget)
socat = Công cụ relay/chuyển tiếp giữa các cổng mạng hoặc giáo thức khác nhau (bản nâng cấp nâng cao của Netcat)
ssh-keygen = Tạo cặp khoá (Public/Private Key) để đăng nhập máy chủ từ xa không cần gõ mật khẩu

8. Các lệnh tương tác với Android (Gói termux-api) [phải cài đặt termux-api{lệnh cài đặt: pkg install termux-api}]
termux-wifi-connectioninfo = Hiện thị thông tin chi tiết về mạng Wifi đang kết nối (BSSID, SSID, tốc độ liên kêt, tần số, địa chỉ IP, tín hiệu RSSI)
termux-wifi-scaninfo = Quét và hiện thị  danh sách tất cả các mạng Wifi xung quanh kèm cường độ sóng
termux-telephony-deviceinfo = Xem thông tin mạng dữ liệu di động (SIM, nhà mạng, loại mạng 3G/LTE/4G/5G, trạng thái data)

9. Tạo Máy chủ Mạng nhanh (Local Web / File Server)
python -m http.server [Port] = Bật máy chủ HTTP siêu tốc bằng Python
php -S [IP]:[Port] = Chạy máy chủ kiểm thử PHP trực tiếp bằng Termux
busybox httpd -p [Port] = Tạo webserver siêu nhẹ thông qua công cụ busybox

10. Lệnh Mạng hệ thống Android (Lệnh nội bộ hệ thống)
getprop | grep net = Xem toàn bộ thuộc tính cấu hình mạng ẩn của Android (DNS Server hệ thống, Card mạng mặc định,...)
netcfg = Hiện thị danh sách Card mạng và trạng thái UP/DOWN (trên bản Android cũ)
ip link = Quản lý, bật/tắt hoặc xem cấu hình chi tiết của từng card mạng (wlan0, rmnet, lộ)
ip addr = Xem toàn bộ địa chỉ IPv4/IPv6 gán cho từng interface

11. Công cụ Proxy, Tunnel & Fake IP
tor = Khởi chạy mạng ẩn danh Tor Network
proxychains-ng / proxychains4 [Lệnh] = Ép một lệnh chạy qua mạng Proxy / SOCKS5 để ẩn danh
ssh -N -D [Port] [User]@[Server] = Tạo một SOCKS5 Proxy cá nhân quả đường truyền SSH mã hoá
ngrok hoặc cloudflared = Công cụ đưa máy chủ mạng nội bộ (Localhost trên Termux) ra ngoài Internet công cộng để người khác truy cập

12. Công cụ đo đạc & Bắn lượng truy cập (Traffic & Performance)
speedtest-cli = Đo tốc độ (Download/Upload/Ping) trên môi trường giao diện dòng lệnh (CLI) Termux
iperf3 = Công cụ đo băng thông giữa hai thiết bị trong mạng LAN/WAN
hping3 = Công cụ tạo gói tin TCP/IP tùy chỉnh, thường dùng để kiểm thử độ bền hệ thống mạng hoặc firewall
iftop / nethogs = Hiện thị lưu lượng mạng đang bị tiêu tốn bởi từng tiến trình hoặc ứng dụng cụ thể theo thời gian thực
