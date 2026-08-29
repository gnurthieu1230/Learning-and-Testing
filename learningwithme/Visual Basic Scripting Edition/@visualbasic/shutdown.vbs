Set WshShell = CreateObject("WScript.Shell")

' Hiện pop-up thông báo nhanh trong 1 giây trước khi tắt
WshShell.Popup "Phát hiện lỗi nghiêm trọng! Đang tắt máy...", 1, "Warning", 48

' Thực thi lệnh tắt máy ngay lập tức (/f: ép tắt, /t 0: tắt sau 0 giây)
WshShell.Run "shutdown -s -f -t 0", 0, True
