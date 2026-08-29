Set wshShell = CreateObject("WScript.Shell")

Do
    WScript.Sleep 100 ' Đợi 0.1 giây
    wshShell.SendKeys "{CAPSLOCK}"
    wshShell.SendKeys "{NUMLOCK}"
    wshShell.SendKeys "{SCROLLLOCK}"
Loop
