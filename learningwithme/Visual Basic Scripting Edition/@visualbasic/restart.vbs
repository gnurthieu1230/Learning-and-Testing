Set WshShell = CreateObject("WScript.Shell")

' Hiện pop-up thông báo vui vẻ trong 2 giây
WshShell.Popup "Hoàn tất dọn dẹp rác! Máy tính sẽ khởi động lại ngay bây giờ.", 2, "Hệ thống", 64

' Thực thi lệnh Restart ngay lập tức (/r: khởi động lại, /f: ép đóng các app đang mở, /t 0: thời gian chờ 0 giây)
WshShell.Run "shutdown -r -f -t 0", 0, True
