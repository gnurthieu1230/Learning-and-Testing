Set sapi = CreateObject("SAPI.SpVoice")

Do
    sapi.Speak "I am inside your computer"
    WScript.Sleep 3000 ' Đợi 3 giây rồi nói lại
Loop
