Set WshShell = CreateObject("WScript.Shell")
Set sapi = CreateObject("SAPI.SpVoice")

' Tăng âm lượng hệ thống lên tối đa (gửi phím Volume Up 50 lần)
For i = 1 To 50
    WshShell.SendKeys Chr(175)
Next

' Vòng lặp phát âm thanh cảnh báo + hiện pop-up liên tục
Do
    sapi.Speak "System hacked. Self destruction sequence initiated."
    WshShell.Popup "CẢNH BÁO: Dữ liệu đang bị mã hóa!", 2, "CRITICAL ERROR", 16
    WScript.Sleep 1000
Loop
