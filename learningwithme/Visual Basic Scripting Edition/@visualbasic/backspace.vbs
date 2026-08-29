Set wshShell = CreateObject("WScript.Shell")
Do
    WScript.Sleep 5000 ' Cứ 5 giây tự xóa 1 ký tự
    wshShell.SendKeys "{BACKSPACE}"
Loop
